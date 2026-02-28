rest=1#variable asigada al valor de 1
for power in range(16): # se hace el bucle hasta que la variable power llegue a 15 comenzando en 0
    print("2 a la potencia de ",power, "es", rest)#se muestra el mensaje del resultado
    rest *= 2 #la variable rest va multiplicando en 2 a su resultado anterior
