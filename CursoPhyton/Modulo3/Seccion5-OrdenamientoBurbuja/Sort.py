# Se crea una lista vacía donde se almacenarán los valores ingresados
lista = []

# Se le pide al usuario la cantidad de elementos que tendrá la lista
# Se convierte a entero porque input() devuelve texto
lenlista = int(input("Ingresa la longitud de la lista: "))

# Ciclo for que se repetirá según la longitud indicada
for i in range(lenlista):
    
    # Se solicita un número al usuario
    # Se convierte a entero antes de guardarlo
    n = int(input("Ingresa tu valor el cual sera agregado al final de la lista: "))
    
    # Se agrega el número al final de la lista
    lista.append(n)

# Se muestra la lista final ingresada por el usuario
print("Tu lista quedo: ", lista)

# Se pregunta al usuario si desea ordenar la lista
r = input("Deseas ordenar tu lista y/n: ")

# Si el usuario responde 'y'
if r == 'y':
    
    # Se ordena la lista de menor a mayor
    lista.sort()
    
    # Se muestra la lista ya ordenada
    print("Tu lista ordenada quedo: ", lista)

# Si la respuesta no es ni 'y' ni 'n'
elif r != 'y' and r != 'n':
    
    # Se muestra mensaje de error
    print("Respuesta no valida")

# Si el usuario responde 'n'
elif r == 'n':
    
    # Se muestra la lista sin cambios
    print("Tu lista no ha cambiado: ", lista)