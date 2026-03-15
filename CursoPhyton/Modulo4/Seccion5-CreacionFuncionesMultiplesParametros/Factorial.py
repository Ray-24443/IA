# Funcion que calcula el factorial de un numero entero
# El factorial de un numero n (n!) es el producto de todos
# los numeros enteros positivos desde 1 hasta n.
def factorial(numero):

    # Si el numero es negativo, no existe factorial
    if numero < 0:
        return None
    
    # Si el numero es 0 o 1, su factorial es 1
    if numero < 2:
        return 1

    # Variable donde se guardara el resultado de la multiplicacion
    producto = 1

    # Ciclo que multiplica todos los numeros desde 2 hasta numero
    for i in range(2, numero + 1):
        producto *= i

    # Se regresa el resultado del factorial
    return producto


# Ciclo para probar la funcion con numeros del 1 al 5
for numero in range(1, 6):
    print(numero, factorial(numero))