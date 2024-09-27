# server.py
import asyncio
from aiohttp import web
from config import Config
from protocol import ElectrumProtocol

async def start_server():
    protocol = ElectrumProtocol()
    protocol.blockchain.test_connection()  # Test connection to full node
    app = web.Application()
    app.router.add_post('/', protocol.handle_request)
    return app

if __name__ == "__main__":
    app = asyncio.run(start_server())
    web.run_app(app, port=Config.TCP_PORT)
