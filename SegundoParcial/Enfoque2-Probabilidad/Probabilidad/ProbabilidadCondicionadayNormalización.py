# Definimos probabilidades conjuntas (ejemplo: enfermedad y test)
# P(Enfermo y Positivo)
P_enfermo_y_pos = 0.08  # 8%

# P(Sano y Positivo)
P_sano_y_pos = 0.02  # 2%

# Calculamos P(Positivo)
P_pos = P_enfermo_y_pos + P_sano_y_pos  # Suma total

# Normalización: P(Enfermo | Positivo)
P_enfermo_dado_pos = P_enfermo_y_pos / P_pos  # División

# Normalización: P(Sano | Positivo)
P_sano_dado_pos = P_sano_y_pos / P_pos  # División

# Mostrar resultados
print("P(Enfermo | Positivo):", P_enfermo_dado_pos)
print("P(Sano | Positivo):", P_sano_dado_pos)