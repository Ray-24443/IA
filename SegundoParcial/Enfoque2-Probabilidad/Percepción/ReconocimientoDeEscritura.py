# -----------------------------------------------------------
# RECONOCIMIENTO DE ESCRITURA
# -----------------------------------------------------------

# Importamos OpenCV
import cv2

# Importamos NumPy
import numpy as np

# Creamos una imagen negra
imagen = np.zeros((200, 600, 3), dtype="uint8")

# Escribimos texto blanco sobre la imagen
cv2.putText(
    imagen,
    "HOLA",
    (50, 120),
    cv2.FONT_HERSHEY_SIMPLEX,
    3,
    (255, 255, 255),
    5
)

# Convertimos a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicamos umbral binario
_, binaria = cv2.threshold(gris, 127, 255, cv2.THRESH_BINARY)

# Buscamos contornos de letras
contornos, _ = cv2.findContours(
    binaria,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Contamos letras detectadas
cantidad = len(contornos)

# Mostramos cantidad detectada
print("Cantidad de letras detectadas:", cantidad)

# Mostramos la imagen
cv2.imshow("Reconocimiento de Escritura", imagen)

# Esperamos tecla
cv2.waitKey(0)

# Cerramos ventanas
cv2.destroyAllWindows()