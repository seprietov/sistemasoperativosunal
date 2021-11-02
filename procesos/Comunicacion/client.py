#Un chat simple cliente-servidor de max 5 mensajes

import socket

for i in range(5):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1234))
    text = input("You: ")
    s.sendall(str.encode(text))
    msg = s.recv(1024)
    print(f'user1: {msg.decode("utf-8")}')