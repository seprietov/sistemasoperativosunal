from socket import *
from typing import final
import asyncio as asy

def createServer():
    host = "localhost"
    port = 9000
    serversocket = socket(AF_INET, SOCK_STREAM)
    serversocket.bind((host,port))
    serversocket.listen()
    print("el servidor en el puerto 9000")


    while True:
        connection , address = serversocket.accept()
        request = connection.recv(1024).decode("utf-8")
        #print(request)
        string_list = request.split(" ")
        method = string_list[0]
        requesting_file = string_list[1]

        print("client request", requesting_file)

        myfile = requesting_file.split("?")[0]#no toma en cuenta las cosas despues de "?"
        myfile = myfile.lstrip("/")

        if(myfile == ""):
            myfile = "pagina.html"

        try: 
            file = open(myfile , "rb")
            response = file.read()
            file.close()
            
            header = "HTTP/1.1 200 OK\n"
            if(myfile.endswith(".jpg")):
                mimetype = "image.jpg"
            elif(myfile.endswith(".css")):
                mimetype = "text/css"
            elif(myfile.endswith(".pdf")):
                mimetype = "application/pdf"
            else:
                mimetype = "text/html"
            header += "Content-Type: "+str(mimetype)+"\n\n"

        except Exception as e:  
            header = "HTTP/1.1 404 Not Found\n"
            response = "<html><body>Eror 404: File not found</body></html>".encode("utf-8")

        final_response = header.encode("utf-8")
        final_response += response 
        connection.send(final_response)
        connection.close()

createServer()