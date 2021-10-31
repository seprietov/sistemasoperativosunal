import os
#os.chdir cambia el directorio de trabajo al indicado en el path que incluye el nombre del nuevo directorio
path = os.path.join(os.getcwd(),"newDir")
os.mkdir(path)
print("aqui se prueba por primera vez")
print(os.chdir(path))
print(os.getcwd())