from aiohttp import web
from aiohttp.web_request import Request


async def healthcheck(request: Request) -> web.Response:
    """
    View для проверки состояния сервиса
    """
    return web.json_response({})
