
#for linea in open("datospython.txt","r"):
#   print(linea)
#print("\n\nse ha desplegado el archivo.")
 
f=open("datospython.txt","r")
lineas=f.readlines()

for k in lineas:
  print (k)

nombre=input("cual es tu nombre ")
print ("Entendiste el funcionamiento del programa ",nombre)
 
