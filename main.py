#!/usr/bin/python3

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from html_json import HtmlJson

app = FastAPI(debug=True)
hj = HtmlJson()


class User(BaseModel):
    name: str
    id: int


@app.get("/")
@hj.html_or_json('index.html')
async def root(name: str):
    return {"message": f"Hello {name}"}


@app.get("/user")
@hj.html_or_json('user.html')
async def user():
    return User(name="John", id=23)


@app.get("/users")
@hj.html_or_json('users.html')
async def users():
    return [
        User(name="John", id=23),
        User(name="Mike", id=98),
        User(name="Timmy", id=72),
    ]


if __name__ == "__main__":
    uvicorn.run(app)
