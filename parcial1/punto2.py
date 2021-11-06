import socket

target_host = "https://www.buda.com/api/v2/markets"

target_port = 80  # create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data
request = "GET /markets/btc-clp" % target_host
client.send(request.encode())

# receive some data
response = client.recv(4096)
http_response = repr(response)
http_response_len = len(http_response)

print(response)