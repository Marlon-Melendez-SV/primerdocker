
#for linea in open("datospython.txt","r"):
#   print(linea)
#print("\n\nse ha desplegado el archivo.")
 
f=open("datospython.txt","r")
lineas=f.readlines()

for k in lineas:
  print (k)


 
