def mensaje():#agrego mi funcion
    print("Ingresa un valor para comparar: ") #lo que tiene que hacer el programa cada que invocó mi funcion

mensaje()#invoco la funcion
a=int(input())#variable que guarda el valor del usuario
mensaje()#invoco la funcion
b=int(input())#variable que guarda el valor del usuario
mensaje()#invoco la funcion
c=int(input()) #variable que guarda el valor del usuario

print("El numero mas grande es: ", max(a,b,c))#comparo e imprimo el numero mayor
print("El numero mas pequeño es: ", min(a,b,c))#comparo e imprimo el numero menor