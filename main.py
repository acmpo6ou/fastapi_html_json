from fastapi import FastAPI, Request
from html_json import HtmlJson

app = FastAPI()
hj = HtmlJson()


@app.get("/")
@hj.html_or_json
async def root(request: Request):
    return {"message": "Hello World"}
