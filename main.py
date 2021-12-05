#!/usr/bin/python3

import uvicorn
from fastapi import FastAPI
from html_json import HtmlJson

app = FastAPI(debug=True)
hj = HtmlJson()


@app.get("/")
@hj.html_or_json
async def root(name: str):
    return {"message": f"Hello {name}"}

if __name__ == "__main__":
    uvicorn.run(app)
