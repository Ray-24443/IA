palabra=input("Ingresa una palabra: ") #el usuario ingresa un mensaje
palabra=palabra.upper()#el mensaje se convierte en mayusculas

for letra in palabra: #ciclo for
    if letra == 'A':#si la palabra contiene una A se salta
        continue
    elif letra =='E': #si la palabra contiene una E se salta
        continue
    elif letra == 'I':#si la palabra contiene una I se salta
        continue
    elif letra == 'O':#si la palabra contiene una O se salta
        continue
    elif letra == 'U':#si la palabra contiene una U se salta
        continue
    else:
        print(letra) #se imprime el mensaje con las palabras saltadas