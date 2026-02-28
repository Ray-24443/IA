nsecret = 16 #numero secreto del mago
#bienvenida del juego
print
( """Bienvenido a mi juego del numero secreto, tu tarea
es adivinar el numero o quedaras atrapado en el bucle"""
)
numero=int(input("Ingresa tu numero: "))#el usuario ingresa el numero que el cree es el ganador

while numero !=16:#mientras que el numero no sea 16 se entra al bucle
    numero=int(input("Ingresa un nuevo numero: "))

print("Excelente has adivinado el numero: ",numero)#si el numero es 16 es el fin del bucle