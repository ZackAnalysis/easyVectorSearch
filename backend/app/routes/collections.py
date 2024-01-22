from typing import List

import chromadb.utils.embedding_functions as ef
from chromadb import Collection
from fastapi import APIRouter, HTTPException
from models.chromadb import chroma_client
from pydantic import BaseModel

# sentence_transformer_ef = ef.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

router = APIRouter()


class CollectionInfo(BaseModel):
    name: str
    num_documents: int
    embedding_function_name: str

    @classmethod
    def from_collection(cls, collection: Collection):
        return cls(
            name=collection.name,
            num_documents=collection.count(),
            embedding_function_name=collection._embedding_function.__getattribute__(
                "MODEL_NAME"
            ),
        )


@router.get("/", response_model=List[CollectionInfo])
async def get_collections():
    collections = chroma_client.list_collections()
    return [CollectionInfo.from_collection(collection) for collection in collections]


@router.post("/create/{collection_name}")
async def create_collection(collection_name: str):
    result = chroma_client.create_collection(collection_name, embedding_function=ef.DefaultEmbeddingFunction())  # type: ignore
    if not result:
        raise HTTPException(status_code=400, detail="Collection creation failed")
    return {"message": "Collection created successfully"}


@router.delete("/{collection_name}")
async def delete_collection(collection_name: str):
    result = chroma_client.delete_collection(name=collection_name)
    if not result:
        raise HTTPException(status_code=404, detail="Collection not found")
    return {"message": "Collection deleted successfully"}
