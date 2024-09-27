# protocol.py
import asyncio
from aiohttp import web

from blockchain import Blockchain
from database import Database

class ElectrumProtocol:
    def __init__(self):
        self.database = Database("mydatabase.db")
        self.blockchain = Blockchain()

    async def handle_request(self, request):
        data = await request.json()
        method = data.get('method')

        if method == 'server.version':
            return self.handle_server_version(data)
        elif method == 'blockchain.address.get_balance':
            return self.handle_get_balance(data)
        # Add more methods as needed

    def handle_server_version(self, data):
        return {"result": ["ElectrumX", "1.4"], "id": data.get('id')}

    def handle_get_balance(self, data):
        address = data['params'][0]
        balance = self.database.get_balance(address)
        return {"result": balance, "id": data.get('id')}
