from fastapi import FastAPI

from concat_impl import pyconcat

app = FastAPI()


@app.get("/concatenate")
def concatenate(str1: str = '', str2: str = ''):
    return str1 + str2

@app.get("/concatenate_fast")
def concatenate_fast(str1: str = '', str2: str = ''):
    result = pyconcat(str1, str2)
    return result