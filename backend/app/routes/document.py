import enum
import json
from io import BytesIO, StringIO
from uuid import uuid4

import pandas as pd
from fastapi import APIRouter, File, HTTPException, UploadFile
from fastapi.responses import Response, StreamingResponse
from models.chromadb import chroma_client
from pydantic import BaseModel

router = APIRouter()


class SearchItem(BaseModel):
    text: str
    candidates: int = 10


class Document(BaseModel):
    text: str
    id: str
    metajson: dict

    @classmethod
    def from_dict(cls, doc: dict, text_field: str):
        return cls(
            text=doc[text_field],
            id=doc.get("id", str(uuid4())),
            metajson=doc,
        )


class OutPutFormat(enum.Enum):
    json = "json"
    excel = "xlsx"
    csv = "csv"


@router.post("/{collection_name}/search")
async def search_text(collection_name: str, search_text: str, limit: int = 10):
    try:
        collection = chroma_client.get_collection(collection_name)
        results = collection.query(query_texts=[search_text], n_results=limit)
        results = {k: v[0] if isinstance(v, list) else None for k, v in results.items()}
        df = pd.DataFrame(results)
        df.drop(columns=["documents"], inplace=True)
        results = df.to_dict(orient="records")
        return results
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/{collection_name}/add")
async def add_document(collection_name: str, doc: Document):
    try:
        collection = chroma_client.get_or_create_collection(collection_name)
        collection.add(
            documents=[doc.text],
            ids=[doc.id],
            metadatas=[doc.metajson] if doc.metajson else None,
        )
        return {"message": "Text added successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/{collection_name}/count")
async def count_documents(collection_name: str):
    try:
        collection = chroma_client.get_collection(collection_name)
        return {"count": collection.count()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/{collection_name}/export")
async def export_collection(
    collection_name: str,
    limit: int = 100,
    offset: int = 0,
    output_format: OutPutFormat = OutPutFormat.json,
):
    """
    export collection as json file
    """
    try:
        collection = chroma_client.get_collection(collection_name)
        docs = collection.get(limit=limit, offset=offset)
        # data = json.dumps(docs, indent=4, ensure_ascii=False)
        df = pd.DataFrame(docs)

        if output_format == OutPutFormat.json:
            headers = {
                "Content-Disposition": f"attachment; filename={collection_name}.json",
                "Content-Type": "text/json",
            }
            data = df.to_json(orient="records")
            return Response(content=data, headers=headers)
        else:
            if output_format == OutPutFormat.excel:
                data_bytes = BytesIO()
                df.to_excel(data_bytes, index=False)
                content_type = (
                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
                headers = {
                    "Content-Disposition": f"attachment; filename={collection_name}.xlsx",
                    "Content-Type": content_type,
                }
                return Response(content=data_bytes.getvalue(), headers=headers)

            else:
                data_bytes = StringIO()
                df.to_csv(data_bytes, index=False)
                content_type = "text/csv"
                headers = {
                    "Content-Disposition": f"attachment; filename={collection_name}.csv",
                    "Content-Type": content_type,
                }
                response = StreamingResponse(
                    iter([data_bytes.getvalue()]),
                    media_type="text/csv",
                    headers=headers,
                )
                return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/{collection_name}/upload")
async def upload_collection(
    collection_name: str, text_field: str, file: UploadFile = File(...)
):
    """
    upload json file to collection
    """
    try:
        collection = chroma_client.get_or_create_collection(collection_name)
        data = await file.read()
        docs = json.loads(data)
        df = pd.DataFrame(docs)
        df = df.dropna(subset=[text_field]).drop_duplicates(subset=[text_field])
        docs = df.to_dict(orient="records")
        documents = [Document.from_dict(doc, text_field) for doc in docs]
        batch_size = 100
        for i in range(0, len(documents), batch_size):
            batch = documents[i : i + batch_size]
            collection.add(
                documents=[doc.text for doc in batch],
                ids=[doc.id for doc in batch],
                metadatas=[doc.metajson for doc in batch],
            )
        return {"message": "documents added successfully"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))
