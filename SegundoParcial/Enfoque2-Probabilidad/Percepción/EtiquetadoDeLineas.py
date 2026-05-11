# -----------------------------------------------------------
# ETIQUETADO DE LINEAS
# -----------------------------------------------------------

# Importamos OpenCV
import cv2

# Importamos NumPy
import numpy as np

# Creamos imagen negra
imagen = np.zeros((400, 400, 3), dtype="uint8")

# Dibujamos líneas blancas
cv2.line(imagen, (50, 50), (350, 50), (255, 255, 255), 3)

cv2.line(imagen, (50, 150), (350, 300), (255, 255, 255), 3)

# Convertimos a gris
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Detectamos bordes
bordes = cv2.Canny(gris, 50, 150)

# Detectamos líneas usando Hough
lineas = cv2.HoughLinesP(
    bordes,
    1,
    np.pi / 180,
    50,
    minLineLength=50,
    maxLineGap=10
)

# Verificamos si hay líneas
if lineas is not None:

    # Recorremos cada línea
    for linea in lineas:

        # Extraemos coordenadas
        x1, y1, x2, y2 = linea[0]

        # Dibujamos línea detectada
        cv2.line(
            imagen,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

# Mostramos resultado
cv2.imshow("Etiquetado de Lineas", imagen)

# Esperamos tecla
cv2.waitKey(0)

# Cerramos ventanas
cv2.destroyAllWindows()