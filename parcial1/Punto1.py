import os
import pandas as pd

########### PARTE EN ARCHIVO DE TEXTO
path = './archivo_texto.txt'
mode = 0o666

flags = os.O_RDWR | os.O_CREAT
fd = os.open(path, flags, mode)

chdir = 'El metodo "os.chdir(path)" solicita como argumento un str con la ruta a la cual se cambiará el espacio de tranajo'
environ = 'El metodo "os.environ" mapea las varibles del entorno retornando un diccionario de estas'
fs_encode = 'El metodo os.fsencode(filename) codifica el nombre del archivo retornando bytes. El proceso inverso lo realiza os.fsdecode(filename)'
get_exec = 'El metodo os.get_exec_path() retorn una lista de directorios donde se puede buscar un ejecutable por nombre'
get_cwd = 'El metodo "os.getcwd()" retorna un string con la ruta al directorio de trabajo actual'

str = chdir + "\n" + environ + "\n" + fs_encode + "\n" + get_exec + "\n" + get_cwd
os.write(fd, str.encode())

os.lseek(fd, 0, 0)
str = os.read(fd, os.path.getsize(fd))
print(str.decode())
os.close(fd)

########## PARTE EN ARCHIVO TIPO EXCEL
funciones = {
    'Función':['os.chdir', 'os.environ', 'os.fsencode', 'os.get_exec_path', 'os.getcwd'],
    'Descripción':[chdir, environ, fs_encode, get_exec, get_cwd]
}

frame_f = pd.DataFrame.from_dict(funciones)
st = frame_f.to_string().encode()

with pd.ExcelWriter('funciones.xlsx') as ex:
    frame_f.to_excel(ex)
frame_f.to_excel('funciones.xlsx')