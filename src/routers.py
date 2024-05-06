from aiohttp import web

from src.views import hash_string, healthcheck


def setup_routes(app: web.Application):
    """
    Функция для регистрации маршрутов
    """
    app.router.add_route('GET', '/healthcheck', healthcheck)
    app.router.add_route('POST', '/hash', hash_string)
