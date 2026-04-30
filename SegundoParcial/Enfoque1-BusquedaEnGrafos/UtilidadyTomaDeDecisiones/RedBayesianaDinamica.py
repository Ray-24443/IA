# ================================
# RED BAYESIANA DINAMICA (DBN)
# ================================

# Grafo dinámico:
# Estado_t -> Estado_t+1
# Estado_t -> Observacion_t
grafo = {
    'Estado_t': ['Estado_t+1', 'Observacion_t'],  # Dependencias
    'Estado_t+1': ['Observacion_t+1'],            # Evolución
    'Observacion_t': [],
    'Observacion_t+1': []
}

# Estados posibles
estados = ['Sano', 'Enfermo']  # Estados ocultos

# Observaciones posibles
observaciones = ['Bien', 'Mal']  # Lo que vemos

# Probabilidad de transición P(Estado_t+1 | Estado_t)
transicion = {
    ('Sano', 'Sano'): 0.8,      # Probabilidad de seguir sano
    ('Sano', 'Enfermo'): 0.2,
    ('Enfermo', 'Sano'): 0.3,
    ('Enfermo', 'Enfermo'): 0.7
}

# Probabilidad de observación P(Obs | Estado)
sensor = {
    ('Sano', 'Bien'): 0.9,
    ('Sano', 'Mal'): 0.1,
    ('Enfermo', 'Bien'): 0.2,
    ('Enfermo', 'Mal'): 0.8
}

# Creencia inicial
creencia = {
    'Sano': 0.6,
    'Enfermo': 0.4
}

# Función de predicción (paso del tiempo)
def prediccion(creencia_actual):
    nueva = {}  # Nueva creencia

    for s2 in estados:  # Estado siguiente
        suma = 0  # Acumulador

        for s1 in estados:  # Estado actual
            suma += creencia_actual[s1] * transicion[(s1, s2)]  # Modelo de transición

        nueva[s2] = suma  # Guardamos

    return nueva  # Regresamos predicción

# Función de actualización (con observación)
def actualizacion(creencia_predicha, obs):
    nueva = {}  # Nueva creencia
    total = 0   # Para normalizar

    for s in estados:  # Para cada estado
        prob = sensor[(s, obs)] * creencia_predicha[s]  # Bayes
        nueva[s] = prob
        total += prob  # Sumamos

    for s in nueva:  # Normalizamos
        nueva[s] /= total

    return nueva

# Simulación de un paso
creencia_pred = prediccion(creencia)  # Paso temporal
creencia_final = actualizacion(creencia_pred, 'Mal')  # Observación

print("Creencia final:", creencia_final)