import json
from fastapi import UploadFile

async def parse_json_file(file: UploadFile):
    content = await file.read()
    data = json.loads(content)
    return data