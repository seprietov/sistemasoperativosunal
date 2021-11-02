#Un chat simple cliente-servidor de max 5 mensajes

import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((socket.gethostname(), 1234))
soc.listen(5)

while True:
    clientsocket, address = soc.accept()
    data = clientsocket.recv(1024)
    if not data:
        break

    print(f'user2: {data.decode("utf-8")}')
    text = input("You: ")
    clientsocket.sendall(str.encode(text))