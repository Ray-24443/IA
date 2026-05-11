# ---------------------------------------------------------
# HW ROBOTICO: SENSORES Y ACTUADORES
# ---------------------------------------------------------

# Importamos la librería time
import time

# Variable que simula un sensor de distancia
sensor_distancia = 100

# Variable que representa el estado del motor
motor = "APAGADO"

# Mostramos mensaje inicial
print("Sistema Robótico Iniciado")

# Repetimos el proceso 5 veces
for i in range(5):

    # Simulamos lectura del sensor
    sensor_distancia = sensor_distancia - 15

    # Mostramos distancia detectada
    print("Distancia detectada:", sensor_distancia)

    # Verificamos si el objeto está cerca
    if sensor_distancia < 50:

        # Encendemos motor
        motor = "ENCENDIDO"

    else:

        # Apagamos motor
        motor = "APAGADO"

    # Mostramos estado del actuador
    print("Motor:", motor)

    # Esperamos 1 segundo
    time.sleep(1)