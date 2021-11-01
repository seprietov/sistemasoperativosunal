import os
#imprime el arbl de todos los directorios y archivos a partir de un punto

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print("current path:", dirpath)
    print("directories:", dirnames)
    print("files:", filenames)
    print()