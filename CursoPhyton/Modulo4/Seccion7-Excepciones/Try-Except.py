# Se utiliza un bloque try para intentar ejecutar código
# que podría generar errores durante su ejecución
try:
    
    # Se solicita al usuario que ingrese un número entero
    value = int(input("Ingresa un número entero: "))
    
    # Se divide el número entre sí mismo
    # Si el número es 0 se producirá un error de división entre cero
    print(value/value)

# Este bloque captura el error si el usuario no ingresa un número entero
except ValueError:
    print("Entrada incorrecta...")

# Este bloque captura el error cuando se intenta dividir entre 0
except ZeroDivisionError:
    print("Entrada errónea...")

# Este bloque captura cualquier otro error que no haya sido considerado
except:
    print("¡Buuuu!")