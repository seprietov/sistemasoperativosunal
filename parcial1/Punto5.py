import hashlib

path1 = r'C:\Users\Sergio\Documents\VSCodeGitHub\sistemasoperativosunal\parcial1\Punto1.py'
path2 = r'C:\Users\Sergio\Documents\VSCodeGitHub\sistemasoperativosunal\parcial1\Punto2.py'
path3 = r'C:\Users\Sergio\Documents\VSCodeGitHub\sistemasoperativosunal\parcial1\Punto3.py'
path4 = r'C:\Users\Sergio\Documents\VSCodeGitHub\sistemasoperativosunal\parcial1\Punto4\Client.py'
path_list = [path1, path2, path3, path4]
print("\n")

with open("hask.txt", "w") as my_file:

    for path in path_list:
        sha256 = hashlib.sha256()

        with open(path, "rb") as opened_file:
            content = opened_file.read()
            sha256.update(content)
            my_file.write("path:    {}\nformat:    sha256\nresult:    {}\n\n".format(path, sha256.hexdigest()))
            print("path:    {}\nformat:    sha256\nresult:    {}\n\n".format(path, sha256.hexdigest()))