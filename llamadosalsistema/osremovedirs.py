import os
# borra los directorios y el camino que llevan a eso
path = os.path.join(os.getcwd(),"newDir")
os.mkdir(path)
os.removedirs(path)