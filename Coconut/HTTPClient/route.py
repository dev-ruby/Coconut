from typing import *

from .request_method import RequestMethod


class Route:
    BASE_URL: ClassVar[str] = "https://api.upbit.com/v1/"

    @staticmethod
    def build_url(url: str, params: dict) -> str:
        first = True
        for key, val in params.items():
            url += "%s%s=%s" % ("?" if first else "&", key, str(val))
            first = False
        return url

    def __init__(self, method: RequestMethod, url: str, params: Optional[Dict[str, Any]] = None) -> None:
        if params:
            url = self.build_url(url, params)

        self.url: str = self.BASE_URL + url
        self.method: RequestMethod = method
