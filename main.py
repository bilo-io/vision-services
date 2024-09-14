import base64
import tempfile
import os

from urllib.request import urlopen
from fastapi import File, UploadFile, FastAPI, Body
from pydantic import BaseModel


class FileSizeResponse(BaseModel):
    size: int


app = FastAPI()


@app.get("/ping", status_code=200)
async def ping():
    return {"message": "pong"}

@app.get("/test", status_code=200)
async def test():
    return {
        "message": "test success",
        "type": "GET test endpoint"
    }

@app.post("/filesize/url", status_code=201)
async def post_url(url: str = Body(..., embed=True)):
    page = urlopen(url)

    return __get_size_file(page.read())


@app.post("/filesize/base64", status_code=201)
async def post_base64(base64_data: str = Body(...)):
    bhtml = base64.b64decode(base64_data)

    return __get_size_file(bhtml)


@app.post("/filesize/upload", status_code=201)
async def post_upload(file: UploadFile = File(...)):
    bhtml = file.file.read(1024 * 1024)

    return __get_size_file(bhtml)


def __get_size_file(bhtml: bytes) -> FileSizeResponse:
    with tempfile.NamedTemporaryFile() as t:
        t.write(bhtml)

        size = os.path.getsize(t.name)

    return FileSizeResponse(size=size)