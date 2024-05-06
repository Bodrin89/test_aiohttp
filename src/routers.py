from aiohttp import web

from src.views.helthcheck_view import healthcheck


def setup_routes(app: web.Application):
    """
    Функция для регистрации маршрутов
    """
    app.router.add_route('GET', '/healthcheck', healthcheck)
