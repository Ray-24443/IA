# ================================
# POMDP
# ================================

# Grafo de estados ocultos
grafo = {
    'Sano': ['Sano', 'Enfermo'],
    'Enfermo': ['Sano', 'Enfermo']
}

# Creencia inicial
creencia = {
    'Sano': 0.6,
    'Enfermo': 0.4
}

# Modelo de observación
observacion = {
    ('Sano', 'Bien'): 0.8,
    ('Sano', 'Mal'): 0.2,
    ('Enfermo', 'Bien'): 0.3,
    ('Enfermo', 'Mal'): 0.7
}

# Función para actualizar creencia
def actualizar(obs):
    nueva = {}  # Nueva creencia
    total = 0   # Normalización

    for estado in grafo:  # Recorremos estados
        prob = observacion[(estado, obs)] * creencia[estado]  # Bayes
        nueva[estado] = prob  # Guardamos
        total += prob  # Sumamos

    for estado in nueva:  # Normalizamos
        nueva[estado] /= total

    return nueva  # Regresamos

# Ejemplo
print("Nueva creencia:", actualizar('Mal'))