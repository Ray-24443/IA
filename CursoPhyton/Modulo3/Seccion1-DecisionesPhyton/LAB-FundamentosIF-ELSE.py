ingreso=float(input("Escribe tu ingreso"))#ingresa el usuario
if ingreso < 85528:#se compara si el ingreso es menor
    total=round((ingreso*0.18-556.02),2)#se hace la operacion para calcular el total
    if total < 0:#si el total es numero negativo toma el valor de 0
        total = 0
else:#si el ingreso es mayor
    excedente=85528-ingreso#nueva variable a utilizar llamada excedente
    total=round(14839.02+((excedente*0.32)/85528),2)#operacion para calcular el total
    

print("Tu total a pagar es: ", total)#se imprime el total