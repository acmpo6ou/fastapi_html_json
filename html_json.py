from fastapi import Request
from functools import wraps
from fastapi.templating import Jinja2Templates


class HtmlJson:
    def __init__(self, templates_dir: str = "templates"):
        self.templates = Jinja2Templates(templates_dir)

    def html_or_json(self, f):
        @wraps(f)
        async def wrapper(request: Request):
            result = await f(request)
            accept = request.headers["accept"].split(",")[0]

            if accept == "text/html":
                result.update({"request": request})
                return self.templates.TemplateResponse("index.html", result)
            return result

        return wrapper
