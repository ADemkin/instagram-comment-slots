from pathlib import Path
import os

import aiohttp_jinja2
import jinja2
from aiohttp.web import Application

from lib import views
from lib.instagram import create_logged_in_client


lib = Path('lib')


def create_app() -> Application:
    app = Application()
    # setup routes
    app.router.add_view('', views.IndexView, name='index')
    # setup templates
    aiohttp_jinja2.setup(
        app=app,
        loader=jinja2.FileSystemLoader(lib / 'templates'),
    )
    # create api
    account = os.environ['INSTAGRAM_ACCOUNT']
    password = os.environ['INSTAGRAM_PASSWORD']
    app['api'] = create_logged_in_client(account, password)
    return app
