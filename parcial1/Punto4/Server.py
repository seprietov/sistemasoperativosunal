from io import BufferedIOBase
from socket import *
import os, sys, struct, time
from typing import Text

print("\nThis is the FTP server.\n\nWaiting for a client to connect.")

TCP_IP = "localhost"
TCP_PORT = 9000
BUFFER_SIZE = 1024

s = socket(AF_INET, SOCK_STREAM)
s.bind((TCP_IP,TCP_PORT))
s.listen()
conn, addr = s.accept()

print("Connected to by address: {} and connection: {}".format(addr,conn))

def upld():
    conn.send("1")
    
    file_name_size = struct.unpack("h", conn.recv(2))[0]
    file_name = conn.recv(file_name_size)

    conn.send("1")

    file_size = struct.unpack("i", conn.recv(4))[0]

    output_file = open(file_name, "wb")

    bytes_received = 0
    print("\nRecieving...")
    while bytes_received < file_size:
        l = conn.recv(BUFFER_SIZE)
        output_file.write(l)
        bytes_received == BUFFER_SIZE
    output_file.close()
    print("\nRecieved file: {}".format(file_name))

    conn.send(struct.pack("i", file_size))
    return

def list_files():
    print("\nListing files:...")

    listing = os.listdir(os.getcwd())
    total_directory_size = 0
    for i in listing:
        conn.send(struct.pack("i", sys.getsizeof(i)))

        conn.send(i)

        conn.send(struct.pack("i",os.path.getsize(i)))
        total_directory_size += os.path.getsize(i)

        conn.recv(BUFFER_SIZE)
    conn.send(struct.pack("i", total_directory_size))

    conn.recv(BUFFER_SIZE)
    print("\nSuccesfully sent file listing to client")
    return

def quit():
    s.send("1")
    conn.close()
    s.close()
    os.execl(sys.excecutable, sys.executable, *sys.argv)



while True:
    print("\nWaintin from instrutions froms client")
    data = conn.recv(BUFFER_SIZE)
    print("\nThe received instrution is: {}".format(data))
    if data == "UPLD":
        upld()
    if data == "LIST":
        list_files()
    if data == "QUIT":
        quit()
    data = None