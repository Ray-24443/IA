# Se crea un diccionario donde:
# la clave es la palabra en español
# y el valor es su traducción al inglés
dictionary = {"gato":"cat","perro":"dog","caballo":"horse"}

# Se solicita al usuario que ingrese una palabra en español
palabra = input("Ingresa una palabra en español: ")

# Se verifica si la palabra ingresada existe como clave en el diccionario
if palabra in dictionary:
    
    # Si la palabra existe, se imprime su traducción al inglés
    print("En ingles es:", dictionary[palabra])

else:
    
    # Si la palabra no existe en el diccionario, se muestra un mensaje
    print("Palabra no encontrada")