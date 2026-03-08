def funcion(): #defino la funcion
    global var #declaro la variable como global
    var=1 #declaro mi variable dentro de la funcion
    print("¿Conozco la variable? ", var) #instruccion de mi funcion

var=2 #variable que toma un valor diferente fuera de la funcion
funcion() #invoco la funcion
print(var) #imprimo la variable independiente de la funcion, se imprimira la definida como global