# ================================
# MDP
# ================================

# Grafo: estado -> acciones -> posibles estados
grafo = {
    'A': {'ir_B': [('B', 1.0)], 'ir_C': [('C', 1.0)]},
    'B': {'ir_D': [('D', 1.0)]},
    'C': {'ir_D': [('D', 1.0)]},
    'D': {}
}

# Recompensas
recompensa = {
    'A': 1,
    'B': 5,
    'C': 2,
    'D': 10
}

# Factor de descuento
gamma = 0.9

# Función de valor
def valor_estado(estado):
    if not grafo[estado]:  # Si es terminal
        return recompensa[estado]  # Regresa recompensa

    valores = []  # Lista de valores

    for accion in grafo[estado]:  # Recorremos acciones
        total = 0  # Acumulador

        for siguiente, prob in grafo[estado][accion]:  # Transiciones
            total += prob * (recompensa[siguiente])  # Valor esperado

        valores.append(total)  # Guardamos

    return max(valores)  # Mejor acción

# Evaluamos todos los estados
for estado in grafo:
    print("Estado:", estado, "Valor:", valor_estado(estado))