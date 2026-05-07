# -----------------------------------------------------------
# NAIVE BAYES
# -----------------------------------------------------------

# Importamos librería matemática
import math

# -----------------------------------------------------------
# DATOS DEL MODELO
# -----------------------------------------------------------

# Probabilidad de spam
prob_spam = 0.5

# Probabilidad de no spam
prob_no_spam = 0.5

# Probabilidad de palabra GRATIS dado spam
prob_gratis_spam = 0.8

# Probabilidad de palabra GRATIS dado no spam
prob_gratis_no_spam = 0.1

# Probabilidad de palabra OFERTA dado spam
prob_oferta_spam = 0.7

# Probabilidad de palabra OFERTA dado no spam
prob_oferta_no_spam = 0.2

# -----------------------------------------------------------
# CALCULO PARA SPAM
# -----------------------------------------------------------

# Probabilidad conjunta spam
probabilidad_spam = (
    prob_spam
    *
    prob_gratis_spam
    *
    prob_oferta_spam
)

# -----------------------------------------------------------
# CALCULO PARA NO SPAM
# -----------------------------------------------------------

# Probabilidad conjunta no spam
probabilidad_no_spam = (
    prob_no_spam
    *
    prob_gratis_no_spam
    *
    prob_oferta_no_spam
)

# -----------------------------------------------------------
# CLASIFICACION
# -----------------------------------------------------------

# Verificamos cuál es mayor
if probabilidad_spam > probabilidad_no_spam:

    # Clasificación final
    resultado = "SPAM"

else:

    # Clasificación final
    resultado = "NO SPAM"

# -----------------------------------------------------------
# RESULTADOS
# -----------------------------------------------------------

# Mostramos encabezado
print("\n--- NAIVE BAYES ---")

# Mostramos probabilidad spam
print("Probabilidad SPAM:", probabilidad_spam)

# Mostramos probabilidad no spam
print("Probabilidad NO SPAM:", probabilidad_no_spam)

# Mostramos resultado final
print("Clasificación:", resultado)

# -----------------------------------------------------------
# GRAFO SIMPLE
# -----------------------------------------------------------

# Mostramos representación
print("\nGRAFO:")

# Relación de variables
print("GRATIS ---->")
print("             SPAM")
print("OFERTA ---->")