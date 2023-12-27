import asyncio
import atexit
from typing import *

import aiohttp

from .missing import Missing
from .response_data import ResponseData
from .route import Route

MISSING: Any = Missing()


class HTTPClient:
    USER_AGENT: ClassVar[str] = "Mozilla/5.0"

    def __init__(self, loop: asyncio.AbstractEventLoop) -> None:
        self.loop: asyncio.AbstractEventLoop = loop
        self.session: aiohttp.ClientSession = MISSING
        self.lock: asyncio.Lock = asyncio.Lock()

        atexit.register(self.close)

    async def request(self, route: Route, headers: Optional[Dict[str, str]] = None) -> ResponseData:
        if not headers:
            headers = {}

        default_header = {"User-Agent": self.USER_AGENT, "Accept": "application/json"}

        headers.update(default_header)

        if self.session == MISSING:
            self.session = aiohttp.ClientSession()

        async with self.lock:
            async with self.session.request(method=route.method.name, url=route.url, headers=headers) as response:
                status: int = response.status
                text: str = await response.text(encoding="utf-8")
                return ResponseData(text, status)

    def close(self) -> None:
        try:
            if not self.session.closed:
                asyncio.run(self.session.close())
        except AttributeError:
            pass
