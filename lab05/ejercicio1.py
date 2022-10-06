try:
  abrir = input("ingrese el nombre del archivo: ")
  ar = open(abrir)
  for linea in ar:
    print(linea.upper())
except:
     print("error, no se pudo abrir el archivo")