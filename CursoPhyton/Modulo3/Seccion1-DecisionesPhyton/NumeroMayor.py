n1=int(input("Ingresa un numero")) #usuario ingresa primer numero
n2=int(input("Ingresa un segundo numero")) #usuario ingresa segundo numero
n3=int(input("Ingresa un tercer numero")) #usuario ingresa tecer numero

N=n1 #por el momento el numero 1 es el mayor

if n2 > N:#si el numero 2 es mayor que el numero 1
    N = n2

if n3 > N:#si el numero 3 es mayor que el numero 1
    N = n3
    
print("El numero mayor es: ", N) #se imprime el mayor de los numeros