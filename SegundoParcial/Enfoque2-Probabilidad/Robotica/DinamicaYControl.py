# ---------------------------------------------------------
# DINAMICA Y CONTROL
# ---------------------------------------------------------

# Posición inicial
posicion = 0

# Objetivo
objetivo = 100

# Ganancia proporcional
kp = 0.1

# Repetimos 20 veces
for i in range(20):

    # Calculamos error
    error = objetivo - posicion

    # Calculamos control
    control = kp * error

    # Actualizamos posición
    posicion = posicion + control

    # Mostramos estado
    print("Posicion:", round(posicion, 2))