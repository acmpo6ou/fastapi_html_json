from fastapi import FastAPI
from html_json import HtmlJson

app = FastAPI()
hj = HtmlJson()


@app.get("/")
@hj.html_or_json
async def root(name: str):
    return {"message": f"Hello {name}"}
