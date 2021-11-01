import os
#cambia el nombre de un directorio

path = os.path.join(os.getcwd(),"newDir")
os.mkdir(path)
print(os.listdir())
os.rename("newDir", "pastDir")
print(os.listdir())