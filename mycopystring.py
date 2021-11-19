def so_stringcopy(string1, string2):
  for i in range(len(string1)):
    string2 += string1[i]
    print(string2)
  return string2

def main():
  string2 = "hola mundo!"
  string2 = ""
  string2 = so_stringcopy(string1, string2)
  print("El string 2 es : ", string2)

  
main()
