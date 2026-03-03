# Creamos una lista vacía donde se guardarán los números ingresados
my_list = []

# Variable booleana que controla el ciclo while
# Se usa para saber si hubo intercambios en la lista
swapped = True

# Se le pide al usuario cuántos elementos desea ordenar
num = int(input("¿Cuántos elementos deseas ordenar?: "))

# Ciclo for para pedir los valores al usuario
for i in range(num):
    # Se pide cada elemento y se convierte a tipo float
    val = float(input("Ingresa un elemento de la lista: "))
    
    # Se agrega el valor a la lista
    my_list.append(val)

# Ciclo while que se repetirá mientras haya intercambios
while swapped:
    
    # Se asume que no habrá intercambios en esta pasada
    swapped = False
    
    # Recorremos la lista hasta el penúltimo elemento
    # (porque se compara i con i+1)
    for i in range(len(my_list) - 1):
        
        # Si el elemento actual es mayor que el siguiente
        # significa que están en el orden incorrecto
        if my_list[i] > my_list[i + 1]:
            
            # Indicamos que sí hubo intercambio
            swapped = True
            
            # Intercambiamos los valores
            # Esta es una forma rápida en Python de hacerlo
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

# Cuando termina el ordenamiento, mostramos el resultado
print("\nOrdenada:")
print(my_list)