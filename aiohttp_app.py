from aiohttp import web
import ssl
import config

app = web.Application()


async def index(request: web.Request):
    print(request.values())
    return web.Response(text='Hello, world!')


app.router.add_get('/', index)


def main():
    try:
        ssl_context = ssl.SSLContext()
        ssl_context.load_cert_chain(config.SSL_CERT_FILE, config.SSL_KEY_FILE)
    except OSError:
        ssl_context = None

    web.run_app(app, ssl_context=ssl_context)


if __name__ == '__main__':
    main()