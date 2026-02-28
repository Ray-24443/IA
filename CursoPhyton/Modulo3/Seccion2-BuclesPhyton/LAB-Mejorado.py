word=input("Ingresa un mensaje: ")#el usuario ingresa un mensaje
word=word.upper()#mensaje se cambia a mayusculas
for letter in word:#ciclo for
    if letter in 'AEIOU':#si la palabra tiene A, E, I, O y U, se la salta
        continue
    else:
        word_without_vowels=letter #la palabra que resta se guarda a una variable llamada 'palabra sin vocales'
        print(word_without_vowels) #se imprime la palabra sin vocales