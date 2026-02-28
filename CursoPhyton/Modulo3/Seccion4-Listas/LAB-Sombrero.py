sombrero=[1,2,3,4,5] #lista llamada sombrero de longitud 5
n=int(input("Ingresa un numero para reemplazar la posicion central: "))#el usuario ingresa un numero para sustuir la posicion central
sombrero[2] = n 
del sombrero [4]#elimino la ultima posicion de la lista
print("Tu nueva lista es: ", sombrero, "\n La longitud es: ", len(sombrero))
#imprimo la nueva lista y su nueva longitud