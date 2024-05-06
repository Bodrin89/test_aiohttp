from aiohttp import web

from src.routers import setup_routes


def create_app() -> web.Application:
    """
    Функция создания приложения
    """
    app = web.Application()
    setup_routes(app)
    return app
