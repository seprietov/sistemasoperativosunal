from io import BufferedIOBase
from socket import *
import os, sys, struct, time
from typing import Text

TCP_IP = "localhost"
TCP_PORT = 9000
BUFFER_SIZE = 1024

sock = socket(AF_INET, SOCK_STREAM) # creo objeto socket

    #funcion para conectar con el servidor
def conn():
    try:
        sock.connect((TCP_IP,TCP_PORT))
        print("connection succesful")
    except:
        print("connection couldn't be compleated. Make sure server is online")
    return


def upld(path_file):
    print("\nUploanging file:...{}".format(path_file))
    try:
        content = open(path_file, "rb")
    except:
        print("\nCouldn't open the file. Make sure the path is correct.")
        return
    try:
        sock.send("UPLD".encode())
    except:
        print("Couldn't make server request. Make sure a coneection has been established.")
        return
    try:
        sock.recv(BUFFER_SIZE)

        sock.send(struct.pack("h"), sys.getsizeof(path_file))
        sock.send(path_file)

        sock.recv(BUFFER_SIZE)
        sock.send(struct.pack("i", os.path.getsize(path_file)))
    except:
        print("Error sending file details")
    try:
        l = content.read(BUFFER_SIZE)
        print("\nSending...")
        while l:
            sock.send(l)
            l = content.read(BUFFER_SIZE)
        content.close()

        upload_size = struct.unpack("i", sock.recv(4))[0]
        print("\nSent file: {}\nFile size: {}b".format(path_file, upload_size))
    except:
        print("Error sending file")
        return
    return


def list_files():
    print("\nRequesting files:...")
    try:
        sock.send("LIST".encode())
    except:
        print("Couldn't make server request. Make sure a conection has been established.")
        return
    try:
        number_of_files = struct.unpack("i", sock.recv(4))[0]
        for i in range(int(number_of_files)):
            file_name_size = struct.unpack("i", sock.recv(4))[0]
            file_name = sock.recv(file_name_size)

            file_size = struct.unpack("i", sock.recv(4))[0]
            print("\t{} - {}b".format/file_name, file_size)

            sock.send("1")

        total_directory_size = struct.unpack("i", sock.recv(4))[0]
        print("\ntotal directory size: {}b".format(total_directory_size))
    except:
        print("\nCouldn't retrive listing")
        return
    try:
        sock.send("1")
        return
    except:
        print("Couldn't get final server confirmation")
        return

def quit():
    sock.send("QUIT")

    sock.recv(BUFFER_SIZE)
    sock.close()
    print("Server connection ended.")
    return
    



print("Welcome to the FTP CLIENT.\n\nYou can call one of the following options:\nCONN:          connection to server.\nUPLD file_path :         upload a file to server.\nLIST:          list all files in server.\nQUIT:         quitting connection with server.\n")
while True:
    #listening (waiting for command)
    prompt = input("\Enter a command: ")
    if prompt[:4].upper() == "CONN":
        conn()
    elif prompt[:4].upper() == "UPLD":
        upld(prompt[5:])
    elif prompt[:4].upper() == "LIST":
        list_files()
    elif prompt[:4].upper() == "QUIT":
        quit()
        break
    else:
        print("Command not identified, please try again")