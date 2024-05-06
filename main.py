import asyncio

import click
from aiohttp import web

from src.create_app import create_app


@click.command()
@click.option('--host', default='0.0.0.0', help='Host IP')
@click.option('--port', default=8000, help='Port number')
def run_server(host, port):
    app = create_app()
    web.run_app(app, host=host, port=port)


if __name__ == '__main__':
    asyncio.run(run_server())
