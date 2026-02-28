# Pedimos al usuario la cantidad total de bloques disponibles
bloques = int(input("Ingresa la cantidad de bloques: "))

# Variable que guardará la cantidad de capas completas construidas
altura = 0

# Variable que representa cuántos bloques necesita la capa actual
capa = 1

# Mientras haya suficientes bloques para construir la capa actual
while bloques >= capa:
    
    # Restamos los bloques usados para construir esta capa
    bloques = bloques - capa
    
    # Aumentamos en 1 la altura porque se completó una capa
    altura = altura + 1
    
    # La siguiente capa necesitará un bloque más
    capa = capa + 1

# Cuando ya no se pueden construir más capas completas,
# mostramos la altura final de la pirámide
print("La altura de la pirámide es:", altura)