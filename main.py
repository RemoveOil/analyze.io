from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/naber")
def read_root():
    return {"iyidir": True}
