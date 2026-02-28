# Pedimos al usuario que ingrese un número entero
c0 = int(input("Ingresa el numero: "))

# Variable que contará la cantidad de pasos realizados
pasos = 0

# El ciclo se ejecuta mientras el número sea diferente de 1
while c0 != 1:
    
    # Si el número es menor o igual a 0, el proceso no es válido
    if c0 <= 0:
        print("Este proceso solo esta disponible para numeros positivos")
        break  # Rompe el ciclo inmediatamente
    
    # Si el número es par (residuo 0 al dividir entre 2)
    if c0 % 2 == 0:
        c0 = c0 // 2  # Se divide entre 2
        print(c0)     # Se muestra el nuevo valor
        pasos += 1    # Se aumenta el contador de pasos
    
    # Si el número es impar
    else:
        c0 = (3 * c0) + 1  # Se multiplica por 3 y se suma 1
        print(c0)          # Se muestra el nuevo valor
        pasos += 1         # Se aumenta el contador de pasos

# Se imprime el valor final (normalmente será 1)
print(c0)

# Se muestra el total de pasos realizados
print("Pasos: ", pasos)