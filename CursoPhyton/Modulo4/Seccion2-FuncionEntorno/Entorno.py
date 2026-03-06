# Definición de la función llamada "mensaje"
# La función recibe dos parámetros:
# what   -> indica qué tipo de dato se está solicitando (por ejemplo: teléfono, cosa, número)
# number -> indica el número o identificador del dato solicitado
def mensaje(what, number):
    
    # La función imprime un mensaje combinando texto con los valores recibidos
    # Se usa print para mostrar en pantalla el mensaje
    print("Ingresa", what, "numero", number)


# Llamada a la función pasando los argumentos:
# what = 'telefono'
# number = 1
# La salida será: Ingresa telefono numero 1
mensaje('telefono',1)


# Segunda llamada a la función:
# what = 'cosa'
# number = 2
# La salida será: Ingresa cosa numero 2
mensaje('cosa',2)


# Tercera llamada a la función:
# what = 'numero'
# number = 'number' (en este caso se pasa una cadena de texto)
# La salida será: Ingresa numero numero number
mensaje('numero','number')