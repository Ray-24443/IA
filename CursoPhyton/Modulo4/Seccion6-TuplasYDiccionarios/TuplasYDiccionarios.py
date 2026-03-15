# Diccionario donde se guardarán los estudiantes y sus calificaciones
clase = {}

# Ciclo para ingresar datos hasta que el usuario deje el nombre vacío
while True:
    # Pedir el nombre del estudiante
    nombre = input("Ingresa el nombre del estudiante: ")
    
    # Si no se escribe nada, el programa termina la captura
    if nombre == '':
        break
    
    # Pedir la calificación del estudiante
    calificacion = int(input("Ingresa la calificación del estudiante (0-10): "))
    
    # Verificar que la calificación esté entre 0 y 10
    if calificacion not in range(0, 11):
        break
    
    # Si el estudiante ya existe en el diccionario,
    # se agrega la nueva calificación a su tupla
    if nombre in clase:
        clase[nombre] += (calificacion,)
    else:
        # Si el estudiante no existe, se crea con su primera calificación
        clase[nombre] = (calificacion,)

# Recorrer el diccionario ordenando los nombres
for nombre in sorted(clase.keys()):
    
    suma = 0
    contador = 0
    
    # Sumar todas las calificaciones del estudiante
    for calificacion in clase[nombre]:
        suma += calificacion
        contador += 1
    
    # Calcular e imprimir el promedio del estudiante
    print(nombre, ":", suma / contador)