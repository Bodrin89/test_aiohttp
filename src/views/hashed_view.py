import hashlib
from json import JSONDecodeError

from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response


async def hash_string(request: Request) -> Response:
    """
    View для хэширования строки.
    """
    try:
        data = await request.json()
    except JSONDecodeError:
        return web.json_response({'validation_errors': 'Invalid JSON'}, status=400)
    if 'string' not in data:
        return web.json_response({'validation_errors': 'Field "string" is required'}, status=400)
    string_to_hash = data['string']
    hashed_string = hashlib.sha256(string_to_hash.encode()).hexdigest()
    return web.json_response({'hash_string': hashed_string})
