import random
import string
from typing import Annotated

from fastapi import FastAPI, Cookie, Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ['http://localhost:8080']
# origins = []
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials=True,
    allow_methods = ['*'],
    allow_headers = ['*'],
)

@app.get("/")
async def root(dammy_id: int = None, cors_app_id: Annotated[str | None, Cookie()] = None):
    return {
        "message": "問題なし！あやちゃん！",
        "dammy_id": dammy_id,
        "cors_app_id": cors_app_id,
    }

@app.get("/set-cookie")
async def set_cookie(response: Response, cors_app_id: Annotated[str | None, Cookie()] = None):
    if cors_app_id is None or len(cors_app_id) == 0:
        response.set_cookie(key="cors_app_id", value=''.join(random.choices(string.ascii_letters + string.digits, k=12)), httponly=True)
    
    return {
        "message": "success"
    }
