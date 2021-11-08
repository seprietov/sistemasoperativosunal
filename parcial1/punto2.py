import socket
import asyncio as asy
import json
import ssl

def rcv(socket):
    while True:
        data = socket.recv(512)
        if len(data) < 1:
            break
        print(data.decode())

def get_buda():
    host = 'www.buda.com'
    request = ['/api/v2/markets', '/api/v2/markets/BTC-CLP', '/api/v2/markets/eth-btc/ticker']
    port = 443
    get = 'GET {} HTTP/1.0\r\nHost: {}\r\n\r\n'.format(request[0], host)

    ctx = ssl.create_default_context()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(15)
        
        with ctx.wrap_socket(sock, server_hostname=host) as ssock:
            ssock.connect((host, port))
            ssock.send(get.encode())
            rcv(ssock)
        

get_buda()