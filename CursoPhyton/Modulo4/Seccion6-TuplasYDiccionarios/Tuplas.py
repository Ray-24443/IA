# Se crea una tupla llamada 'tupla' con varios valores enteros
tupla = (1,2,3,4,5,10)

# Se crea una nueva tupla llamada t1 agregando los valores 100 y 1000
# a la tupla original mediante la concatenación
t1 = tupla + (100,1000)

# Se crea una nueva tupla llamada t2 repitiendo la tupla original dos veces
t2 = tupla * 2

# Imprime la cantidad de elementos que tiene la tupla original
print(len(tupla))

# Imprime la nueva tupla t1 (tupla original + nuevos elementos)
print(t1)

# Imprime la cantidad de elementos que tiene t1
print(len(t1))

# Imprime la tupla t2 que contiene los elementos repetidos
print(t2)

# Imprime la cantidad de elementos que tiene t2
print(len(t2))

# Verifica si el número 2 se encuentra dentro de la tupla
# Regresa True si está presente
print(2 in tupla)

# Verifica si el número 0 se encuentra dentro de la tupla
# Regresa False porque no existe en la tupla
print(0 in tupla)