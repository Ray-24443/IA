# -----------------------------------------------------------
# FILTRO DE KALMAN
# -----------------------------------------------------------

# Importamos matplotlib
import matplotlib.pyplot as plt

# Mediciones del sensor
mediciones = [1, 2, 3, 2, 5, 6, 7]

# Estado inicial
estimacion = 0

# Error inicial
error_estimacion = 1

# Ruido del proceso
q = 0.1

# Ruido de medición
r = 1

# Lista resultados
estimaciones = []

# Recorremos mediciones
for medicion in mediciones:

    # ---------------------------------------------------
    # PREDICCION
    # ---------------------------------------------------

    # Predicción del estado
    prediccion = estimacion

    # Predicción del error
    error_prediccion = error_estimacion + q

    # ---------------------------------------------------
    # ACTUALIZACION
    # ---------------------------------------------------

    # Ganancia de Kalman
    k = error_prediccion / (error_prediccion + r)

    # Nueva estimación
    estimacion = (
        prediccion
        + k * (medicion - prediccion)
    )

    # Actualización del error
    error_estimacion = (
        (1 - k)
        * error_prediccion
    )

    # Guardamos resultado
    estimaciones.append(estimacion)

# -----------------------------------------------------------
# RESULTADOS
# -----------------------------------------------------------

print("\n--- FILTRO DE KALMAN ---")

# Recorremos resultados
for i in range(len(estimaciones)):

    print(
        "Medicion:",
        mediciones[i],
        "Estimacion:",
        round(estimaciones[i], 2)
    )

# -----------------------------------------------------------
# GRAFICA
# -----------------------------------------------------------

# Creamos figura
plt.figure(figsize=(10, 5))

# Dibujamos mediciones
plt.plot(mediciones, marker='o', label="Mediciones")

# Dibujamos estimaciones
plt.plot(estimaciones, marker='s', label="Kalman")

# Título
plt.title("Filtro de Kalman")

# Etiqueta X
plt.xlabel("Tiempo")

# Etiqueta Y
plt.ylabel("Valor")

# Mostramos leyenda
plt.legend()

# Cuadrícula
plt.grid()

# Mostramos
plt.show()