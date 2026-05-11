# -----------------------------------------------------------
# DETECCION DE MOVIMIENTO
# -----------------------------------------------------------

# Importamos OpenCV
import cv2

# Abrimos la cámara
camara = cv2.VideoCapture(0)

# Leemos el primer cuadro
ret, cuadro1 = camara.read()

# Leemos el segundo cuadro
ret, cuadro2 = camara.read()

# Iniciamos ciclo infinito
while camara.isOpened():

    # Calculamos diferencia entre cuadros
    diferencia = cv2.absdiff(cuadro1, cuadro2)

    # Convertimos a escala de grises
    gris = cv2.cvtColor(
        diferencia,
        cv2.COLOR_BGR2GRAY
    )

    # Aplicamos desenfoque
    blur = cv2.GaussianBlur(
        gris,
        (5, 5),
        0
    )

    # Aplicamos umbral
    _, umbral = cv2.threshold(
        blur,
        20,
        255,
        cv2.THRESH_BINARY
    )

    # Dilatamos la imagen
    dilatada = cv2.dilate(
        umbral,
        None,
        iterations=3
    )

    # Buscamos contornos
    contornos, _ = cv2.findContours(
        dilatada,
        cv2.RETR_TREE,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # Recorremos contornos
    for contorno in contornos:

        # Ignoramos objetos pequeños
        if cv2.contourArea(contorno) < 700:
            continue

        # Obtenemos rectángulo
        x, y, w, h = cv2.boundingRect(contorno)

        # Dibujamos rectángulo
        cv2.rectangle(
            cuadro1,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        # Escribimos texto
        cv2.putText(
            cuadro1,
            "Movimiento",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    # Mostramos video
    cv2.imshow("Movimiento", cuadro1)

    # Actualizamos cuadros
    cuadro1 = cuadro2

    # Leemos nuevo cuadro
    ret, cuadro2 = camara.read()

    # Salimos con tecla ESC
    if cv2.waitKey(40) == 27:
        break

# Liberamos cámara
camara.release()

# Cerramos ventanas
cv2.destroyAllWindows()