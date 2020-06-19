from aiohttp import web
from routes import setup_routes
import datetime
import logging

LOG_FILENAME = f'git_hub_{datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S")}.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)

app = web.Application()
setup_routes(app)
web.run_app(app, host='127.0.0.1', port=8080)

