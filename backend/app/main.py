from fastapi import FastAPI
from routes import collections, document

app = FastAPI()

app.include_router(collections.router, prefix="/collections", tags=["collections"])
app.include_router(document.router, prefix="/documents", tags=["search"])