import hashlib

from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response


async def hash_string(request: Request) -> Response:
    """
    View для хэширования строки.
    """
    data = await request.json()
    if 'string' not in data:
        return web.json_response({'validation_errors': 'Field "string" is required'}, status=400)
    string_to_hash = data['string']
    hashed_string = hashlib.sha256(string_to_hash.encode()).hexdigest()
    return web.json_response({'hash_string': hashed_string})
