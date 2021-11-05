import os
# os.path.join une los caminos para hacer solo uno largo Ej: file_path = os.path.join(os.environ.get("HOME"), "test.txt")

file_path = os.path.join(os.environ.get("HOME"), "test.txt")

print(file_path)