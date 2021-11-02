#ejemplos de como se escribe y se leen archivos

with open("newfile.txt", "w") as file:
    file.write("esta es la prueba de escritura en un archivo que tambien ha sido recien creado")
    file.close()
    pass

with open("newfile.txt", "r") as file:
    var = file.read()
    print(var)
    file.close()
    pass

with open("newfile.txt", "a") as file:
    file.write(" Aqui vemos append siendo utilizado para agregar a lo ultimo")
    file.close
    pass

with open("newfile.txt", "r") as file:
    var = file.read()
    print(var)
    file.close()
    pass

with open("newfile.txt", "w") as file:
    file.write("por ultimo aqui estamos borrando todo y sobreescribiendo en write mode")
    file.close()
    pass

with open("newfile.txt", "r") as file:
    var = file.read()
    print(var)
    file.close()
    pass