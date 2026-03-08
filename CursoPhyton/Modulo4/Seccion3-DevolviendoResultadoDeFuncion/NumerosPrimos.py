# Se solicita al usuario que ingrese un número entero
# Este número será evaluado para saber si es primo
n = int(input("Ingresa un numero para comprobar si es numero primo: "))


# Definición de la función es_primo
# La función recibe un número n como parámetro
def es_primo(n):

    # Se recorre un ciclo desde 2 hasta n-1
    # Esto sirve para comprobar si el número tiene divisores
    for i in range(2, n):

        # Se verifica si n es divisible entre i
        # Si el residuo de la división es 0, significa que
        # el número tiene otro divisor además de 1 y él mismo
        if n % i == 0:
            return False  # El número no es primo

    # Si el ciclo termina y no se encontró ningún divisor,
    # significa que el número solo es divisible entre 1 y él mismo
    return True


# Se llama a la función es_primo enviando el número ingresado
# y se imprime el resultado (True si es primo, False si no lo es)
print(es_primo(n))