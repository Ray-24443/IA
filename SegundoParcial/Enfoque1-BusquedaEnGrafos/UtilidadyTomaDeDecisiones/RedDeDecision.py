# ================================
# RED DE DECISION
# ================================

# Grafo dirigido (influencia)
# Clima -> Decisión -> Resultado
grafo = {
    'Clima': ['Decision'],      # El clima influye en la decisión
    'Decision': ['Resultado'],  # La decisión afecta el resultado
    'Resultado': []             # Nodo final
}

# Probabilidades del clima
prob_clima = {
    'Soleado': 0.7,   # Probabilidad de sol
    'Lluvioso': 0.3   # Probabilidad de lluvia
}

# Decisiones posibles
decisiones = ['Salir', 'NoSalir']

# Utilidad según decisión y clima
utilidad = {
    ('Salir', 'Soleado'): 100,
    ('Salir', 'Lluvioso'): -50,
    ('NoSalir', 'Soleado'): 20,
    ('NoSalir', 'Lluvioso'): 10
}

# Función para calcular utilidad esperada
def utilidad_esperada(decision):
    total = 0  # Inicializamos acumulador

    for clima in prob_clima:  # Recorremos cada estado del clima
        prob = prob_clima[clima]  # Obtenemos probabilidad
        total += prob * utilidad[(decision, clima)]  # Sumamos utilidad ponderada

    return total  # Regresamos resultado

# Evaluamos cada decisión
for d in decisiones:  # Iteramos decisiones
    print("Decision:", d, "-> Utilidad esperada:", utilidad_esperada(d))

# Elegimos mejor decisión
mejor = max(decisiones, key=utilidad_esperada)  # Seleccionamos máximo
print("Mejor decision:", mejor)