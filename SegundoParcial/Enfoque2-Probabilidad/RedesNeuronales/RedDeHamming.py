# ==========================================
# RED DE HAMMING
# ==========================================

# Patrones
p1 = [1, 0, 1, 0]
p2 = [1, 1, 0, 0]

# Entrada
entrada = [1, 0, 1, 1]

# Distancia Hamming
contador1 = 0
contador2 = 0

# Comparación patrón 1
for i in range(len(p1)):

    if entrada[i] != p1[i]:
        contador1 += 1

# Comparación patrón 2
for i in range(len(p2)):

    if entrada[i] != p2[i]:
        contador2 += 1

# Resultado
print(contador1)
print(contador2)