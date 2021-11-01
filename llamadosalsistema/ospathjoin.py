import os
# une los caminos para hacer solo uno largo

file_path = os.path.join(os.environ.get("HOME"), "test.txt")

print(file_path)