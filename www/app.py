import logging, asyncio, json
from aiohttp import web
from util.db import Pool, release
from util.decimal_encoder import DecimalEncoder

logging.basicConfig(level = logging.INFO)

def index(request):
   conn = Pool.connection()
   cur = conn.cursor()
   cur.execute('select * from plant_app_core.tb_unit')
   res = cur.fetchall()
   release(cur, conn)
   data_list = [str(u) for u in res]
   print(data_list)
   data_json = json.dumps(data_list, cls = DecimalEncoder)
   print(data_json)
   # return web.Response(body = b'<h1>Home</h1>', content_type = 'text/html')
   return web.json_response(data_json)

async def init(loop):
   app = web.Application(loop = loop)
   app.router.add_route('GET', '/', index)
   server = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
   logging.info('server started at http//127.0.0.1:9000...')

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

