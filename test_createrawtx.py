import json

class Blockchain:
    def __init__(self, rpc_user, rpc_password, rpc_host='127.0.0.1', rpc_port='7332'):
        self.rpc_user = rpc_user
        self.rpc_password = rpc_password
        self.rpc_host = rpc_host
        self.rpc_port = rpc_port
        self.rpc_url = f"http://{self.rpc_user}:{self.rpc_password}@{self.rpc_host}:{self.rpc_port}"

    def rpc_call(self, method, params):
        import requests
        headers = {'content-type': 'text/plain;'}
        payload = json.dumps({"jsonrpc": "1.0", "id": "curltest", "method": method, "params": params})
        
        response = requests.post(self.rpc_url, headers=headers, data=payload)
        return response.json()

    def createrawtransaction(self, inputs, outputs, locktime=0):
        return self.rpc_call('createrawtransaction', [inputs, outputs, locktime])

# Example usage
if __name__ == "__main__":
    blockchain = Blockchain(rpc_user='user', rpc_password='pass')
    
    # Define inputs
    inputs = [{"txid": "f503eec4934c7fb5cdc8f82eaab024a357eecb0fed6838156dc9408e74c2ec9b", "vout": 0}]
    
    # Define outputs
    outputs = [{"1RXD919mdLWUHYZ6tNaFHNbHb2CzDwHhu": 3.5}, {"data": "00010203"}]  # Use a valid address

    # Create raw transaction
    raw_transaction = blockchain.createrawtransaction(inputs, outputs)
    print(f"Raw Transaction: {raw_transaction}")
