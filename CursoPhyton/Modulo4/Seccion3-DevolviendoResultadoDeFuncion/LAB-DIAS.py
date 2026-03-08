# Definición de la función "dias"
# Recibe dos parámetros:
# año -> el año que se quiere evaluar
# mes -> el mes del cual se quiere saber cuántos días tiene
def dias(año, mes):

    # Se verifica si el mes pertenece al grupo de meses que tienen 31 días
    # Los meses con 31 días son: enero, marzo, mayo, julio, agosto, octubre y diciembre
    if mes in (1,3,5,7,8,10,12):
        return 31

    # Se verifica si el mes pertenece al grupo de meses que tienen 30 días
    # Los meses con 30 días son: abril, junio, septiembre y noviembre
    if mes in (4,6,9,11):
        return 30

    # Si el mes es febrero, se debe verificar si el año es bisiesto
    if mes == 2:

        # Si el año no es divisible entre 4, febrero tiene 28 días
        if año % 4 != 0:
            return 28

        # Si es divisible entre 4 pero no entre 100,
        # entonces es un año bisiesto y febrero tiene 29 días
        elif año % 100 != 0:
            return 29

        # Si es divisible entre 100 pero no entre 400,
        # entonces no es bisiesto y febrero tiene 28 días
        elif año % 400 != 0:
            return 28

        # Si es divisible entre 400, el año sí es bisiesto
        # y febrero tiene 29 días
        else:
            return 29