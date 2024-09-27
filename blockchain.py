# blockchain.py
import requests
import json
from config import Config

class Blockchain:
    def __init__(self):
        self.daemon_url = Config.DAEMON_URL

    def rpc_call(self, method, params=None):
        headers = {'content-type': 'application/json'}
        payload = {
            "method": method,
            "params": params or [],
            "id": 1
        }
        response = requests.post(self.daemon_url, headers=headers, data=json.dumps(payload))
        response_data = response.json()
        if 'error' in response_data and response_data['error'] is not None:
            raise Exception(f"RPC Error: {response_data['error']}")
        return response_data['result']

    def get_block_count(self):
        return self.rpc_call("getblockcount")

    def get_transaction(self, txid):
        return self.rpc_call("getrawtransaction", [txid, 1])

    def get_balance(self, address):
        # Adjust according to how your blockchain manages addresses and balances
        return self.rpc_call("getbalance", [address])
    
    def get_block_header(self, block_hash):
        return self.rpc_call("getblockheader", [block_hash])
    
    def get_transaction_history(self, address):
    # This method may require custom logic depending on how your blockchain tracks transactions.
        return self.rpc_call("getreceivedbyaddress", [address])
    
    def get_unspent_outputs(self, address):
        return self.rpc_call("listunspent", [0, 9999999, [address]])
    
    def broadcast_transaction(self, raw_tx):
        return self.rpc_call("sendrawtransaction", [raw_tx])
    def get_block_by_height(self, height):
        block_hash = self.rpc_call("getblockhash", [height])
        return self.rpc_call("getblock", [block_hash])
    




    
    def test_connection(self):
     try:
        block_count = self.get_block_count()
        

        print(f"Connected to full node, current block count: {block_count}")
     except Exception as e:
        print(f"Error connecting to full node: {e}")

