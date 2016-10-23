import asyncio
from aiohttp import web
async def index(request):
    await asyncio.sleep(10)
    return web.Response(headers={'a':'1','Server':'yuanzhang'}, content_type='text/html',body=b'<h1>index</h1>')
async def hello(request):
    await asyncio.sleep(0.5)
    text='<h1>hello,%s'%request.match_info['name']
    return web.Response(content_type='text/html',body=text.encode('utf-8'))

async def init(loop):
    app=web.Application(loop=loop)
    app.router.add_route('GET','/hello/{name}',hello)
    app.router.add_route('GET','/',index)
    server=await loop.create_server(app.make_handler(),'127.0.0.1',8123)
    print('server running at http://127.0.0.1:8123...')
    return server
loop=asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()