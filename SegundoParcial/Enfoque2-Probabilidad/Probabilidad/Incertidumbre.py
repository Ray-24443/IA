# Definimos los posibles estados del mundo (posiciones del robot)
estados = ['A', 'B', 'C']  # Tres posibles ubicaciones

# Definimos creencias iniciales (incertidumbre)
# Esto representa lo que el robot "cree" antes de observar algo
creencias = {
    'A': 0.33,  # 33% de probabilidad de estar en A
    'B': 0.33,  # 33% en B
    'C': 0.34   # 34% en C
}

# Mostramos el estado inicial
print("Estado de incertidumbre inicial:")  # Título
for estado in creencias:  # Recorremos cada estado
    print("P(estar en", estado, ") =", creencias[estado])  # Mostrar probabilidad

# Supongamos que el robot recibe evidencia (sensor detecta algo)
# Ejemplo: el sensor indica que probablemente está en B
evidencia = {
    'A': 0.2,  # Baja probabilidad de detectar esto en A
    'B': 0.7,  # Alta probabilidad en B
    'C': 0.1   # Muy baja en C
}

# Actualizamos creencias (sin normalizar aún)
nuevas_creencias = {}  # Diccionario vacío

for estado in estados:  # Recorremos estados
    # Multiplicamos creencia previa por evidencia
    nuevas_creencias[estado] = creencias[estado] * evidencia[estado]

# Calculamos suma total (para normalizar)
suma = 0  # Inicializamos suma

for valor in nuevas_creencias.values():  # Recorremos valores
    suma += valor  # Sumamos

# Normalizamos las probabilidades
for estado in nuevas_creencias:  # Recorremos estados
    nuevas_creencias[estado] = nuevas_creencias[estado] / suma  # Dividir entre total

# Mostramos nuevas creencias (menos incertidumbre)
print("\nEstado después de observar evidencia:")  # Título
for estado in nuevas_creencias:  # Recorremos
    print("P(estar en", estado, ") =", nuevas_creencias[estado])  # Mostrar