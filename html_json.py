from inspect import signature, Parameter, _ParameterKind
from typing import Callable

from fastapi import Request
from functools import wraps
from fastapi.templating import Jinja2Templates


class HtmlJson:
    def __init__(self, templates_dir: str = "templates"):
        self.templates = Jinja2Templates(templates_dir)

    @staticmethod
    def add_request_param(wrapper: Callable, f: Callable):
        sig = signature(f)
        if 'request' in sig.parameters:
            return

        params = list(sig.parameters.values())
        request_param = Parameter("request", _ParameterKind.POSITIONAL_OR_KEYWORD,
                                  annotation=Request)
        params.append(request_param)
        wrapper.__signature__ = sig.replace(parameters=params)

    def html_or_json(self, f: Callable):
        @wraps(f)
        async def wrapper(*args, **kwargs):
            request = kwargs['request']

            try:
                result = await f(*args, **kwargs)
            except TypeError:
                kwargs.pop('request')
                result = await f(*args, **kwargs)

            accept = request.headers["accept"].split(",")[0]
            if accept == "text/html":
                result.update({"request": request})
                return self.templates.TemplateResponse("index.html", result)

            return result

        self.add_request_param(wrapper, f)
        return wrapper
