# Definición de la función llamada "año"
# Esta función recibe un número n que representa un año
def año(n):

    # Si el año no es divisible entre 4, no es año bisiesto
    if n % 4 != 0:
        return False

    # Si es divisible entre 4 pero no entre 100,
    # entonces sí es un año bisiesto
    elif n % 100 != 0:
        return True

    # Si es divisible entre 100 pero no entre 400,
    # entonces NO es bisiesto
    elif n % 400 != 0:
        return False

    # Si es divisible entre 400,
    # entonces sí es un año bisiesto
    else:
        return True


# Se imprime el resultado de verificar si cada año es bisiesto
print(año(1900))  # 1900 no es bisiesto (False)
print(año(2010))  # 2010 no es bisiesto (False)
print(año(2026))  # 2026 no es bisiesto (False)
print(año(2028))  # 2028 sí es bisiesto (True)
print(año(2030))  # 2030 no es bisiesto (False)