# Definición de la función llamada valor, que recibe un parámetro n
def valor(n):
    # Se verifica si el número n es divisible entre 2
    # El operador % obtiene el residuo de la división
    if n % 2 == 0:
        # Si el residuo es 0, significa que el número es par
        # La función regresa el valor True
        return True

# Se llama a la función valor enviando el número 1
# Como 1 no es par, la función no retorna nada (None)
print(valor(1))

# Se llama a la función valor enviando el número 2
# Como 2 es par, la función retorna True
print(valor(2))

# Se llama a la función valor enviando el número 3
# Como 3 no es par, la función no retorna nada (None)
print(valor(3))