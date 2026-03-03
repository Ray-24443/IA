# Se crea una lista vacía donde se guardarán los elementos
lista = []

# El usuario ingresa la cantidad de elementos que tendrá la lista
# Se convierte a entero porque input() devuelve texto
l = int(input("Dime la longitud de tu lista: "))

# Ciclo for que se repite según la longitud indicada
for i in range(l):
    
    # El usuario ingresa cada elemento de la lista
    n = input("Crea un elemento de la lista: ")
    
    # Se agrega el elemento al final de la lista
    lista.append(n)

# Se imprime la lista original ingresada por el usuario
print("Tu lista es:", lista)

# Variable booleana que nos ayudará a saber si existen repetidos
repetido = False

# Recorremos cada elemento de la lista
for elemento in lista:
    
    # count() cuenta cuántas veces aparece el elemento en la lista
    if lista.count(elemento) >= 2:
        
        # Si aparece dos o más veces, hay repetidos
        repetido = True
        
        # Se detiene el ciclo porque ya sabemos que hay repetidos
        break

# Si existen elementos repetidos
if repetido:
    
    # Se le pregunta al usuario si desea eliminarlos
    r = input("Deseas eliminar los elementos repetidos? y/n: ")
    
    # Si responde 'y'
    if r == "y":
        
        # Se eliminan los repetidos convirtiendo la lista en un conjunto (set)
        # Luego se vuelve a convertir en lista
        lista = list(set(lista))
        
        # Se imprime la lista sin repetidos
        print("Lista sin repetidos:", lista)
    
    # Si responde cualquier cosa distinta de 'y'
    else:
        # La lista permanece igual
        print("La lista no fue modificada:", lista)

# Si no existen repetidos
else:
    print("No hay elementos repetidos.")