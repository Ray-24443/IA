# Funcion que verifica si tres lados pueden formar un triangulo
# Se basa en la desigualdad triangular:
# La suma de dos lados siempre debe ser mayor que el tercero
def triangulo(a,b,c): 
    return a + b > c and b + c > a and c + a > b 

# Solicita al usuario las medidas de los tres lados del triangulo
a = float(input("Ingresa la medida del primer lado: "))
b = float(input("Ingresa la medida del segundo lado: "))
c = float(input("Ingresa la medida del tercer lado: "))

# Se llama a la funcion para verificar si los lados forman un triangulo
if triangulo(a,b,c):
    print("Si puede ser un triangulo")
    
    # Pregunta al usuario si desea calcular el area
    r = input("¿Deseas conocer su area? y/n: ")
    
    # Si el usuario responde 'y', se calcula el area
    if r == 'y':
        
        # Calculo del semiperimetro (s)
        # s = (a + b + c) / 2
        s = (a+b+c)/2
        
        # Calculo del area usando la formula de Heron
        # A = sqrt(s(s-a)(s-b)(s-c))
        A = (s*(s-a)*(s-b)*(s-c))**0.5
        
        # Muestra el resultado
        print("El area del triangulo es:", A)

# Si los lados no cumplen la condicion de triangulo
else:
    print("No cumple las condiciones para ser un triangulo")
