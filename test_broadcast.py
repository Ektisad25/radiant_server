import ssl
import socket
import json
# pip install ssl
# pip install socket
# pip install json

# ElectrumX server details
HOST = 'electrumx.radiant4people.com'
PORT = 50012

# Create an SSL context that does not verify certificates
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# Establish SSL connection
conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=HOST)
conn.connect((HOST, PORT))

# Send ElectrumX protocol request (example: subscribing to blockchain headers)
request = json.dumps({
    "id": 1,
    "method": "blockchain.transaction.broadcast",
    "params": ["put_your signed_raw_transaction_her"]
}) + '\n'

conn.send(request.encode('utf-8'))

response = conn.recv(4096)
print(response.decode('utf-8'))

# Close the connection
conn.close()
