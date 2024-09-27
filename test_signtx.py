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

    def signrawtransactionwithkey(self, hexstring, privkeys, prevtxs=None):
        params = [hexstring, privkeys]

    # Ensure prevtxs is an array or None
        if prevtxs is not None:
         params.append(prevtxs)  # prevtxs should be a JSON array, can be empty
        else:
         params.append([])  # Passing an empty array if None is given

    
        return self.rpc_call('signrawtransactionwithkey', params)


# Example usage
if __name__ == "__main__":
    blockchain = Blockchain(rpc_user='user', rpc_password='pass')
    
    # Create a raw transaction first
    inputs = [{"txid": "f503eec4934c7fb5cdc8f82eaab024a357eecb0fed6838156dc9408e74c2ec9b", "vout": 0}]
    outputs = [{"add_recieve_address_her": 3.5}]  # 3.5 is amount test
    raw_transaction = blockchain.createrawtransaction(inputs, outputs)
    
    # Define private keys for signing (base58-encoded)
    privkeys = ["add_your_sender_private_key_her"]
    
    # Sign the raw transaction
    signed_transaction = blockchain.signrawtransactionwithkey(raw_transaction['result'], privkeys, prevtxs=None)
    print(f"Signed Transaction: {signed_transaction}")
