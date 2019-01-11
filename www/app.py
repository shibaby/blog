import logging
import asyncio
from aiohttp import web

logging.basicConfig(level = logging.INFO)

def index(request):
   return web.Response(body = 'Home')

async def init(loop):
   app = web.Application(loop = loop)
   app.router.add_route('GET', '/', index)
   server = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
   logging.info('server started at http//127.0.0.1:9000...')

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()