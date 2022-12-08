from pprint import pprint

from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def root(request: Request):
    print(f"request:\n{request}\ndict:\n")
    pprint(request.__dict__)
    return {"message": "Hello World"}
