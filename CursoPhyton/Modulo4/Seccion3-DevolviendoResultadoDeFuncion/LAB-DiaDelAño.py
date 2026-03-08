def dias(año, mes): #defino la funcion dias con 2 parametros

    if mes in (1,3,5,7,8,10,12): #si el mes pertenece a estos meses, tiene 31 dias
        return 31

    if mes in (4,6,9,11): #si el mes pertenece a estos meses, tiene 30 dias
        return 30

    if mes == 2: #si el mes es febrero tocá comprobar si el año es bisiesto
        if año % 4 != 0: #si el año no es bisiesto tiene 28 dias
            return 28
        elif año % 100 != 0: #si el año es bisiesto tiene 29 dias
            return 29
        elif año % 400 != 0: #si el año no es bisiesto tiene 28 dias
            return 28
        else:
            return 29 #si el año es bisiesto tiene 29 dias


def day_of_year(año, mes, dia):

    # validar mes
    if mes < 1 or mes > 12:
        return None

    # validar día
    if dia > dias(año, mes):
        return None

    total = 0

    # sumar los días de los meses anteriores
    for m in range(1, mes):
        total += dias(año, m)

    total += dia

    return total


# pruebas
print(day_of_year(2026,1,1))   # 1
print(day_of_year(2026,3,1))   # 60
print(day_of_year(2028,3,1))   # 61 (bisiesto)
print(day_of_year(2026,12,31)) # 365