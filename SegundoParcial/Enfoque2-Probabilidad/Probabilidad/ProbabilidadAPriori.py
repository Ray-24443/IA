# Definimos eventos posibles (clima)
eventos = ['Soleado', 'Lluvioso']  # Dos posibles estados

# Probabilidades a priori (antes de observar algo)
probabilidades = {
    'Soleado': 0.7,  # 70% de probabilidad
    'Lluvioso': 0.3  # 30% de probabilidad
}

# Mostramos resultados
print("Probabilidades a priori:")  # Título
for evento in probabilidades:  # Recorremos eventos
    print(evento, ":", probabilidades[evento])  # Imprimir probabilidad