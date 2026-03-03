lista=[1,2,3,4,5,6,7,8]#imprimo la lista original
lista2=lista[:]#copeo toda la lista completa
#imprimo ambas listas para comprobar que se copearon de manera exitosa
print(lista)
print(lista2)
#de la lista 2 copeo las posiciones 0 a la 4
lista3=lista2[0:5]
print(lista3)#imprimo la nueva lista
lista3[0]=0#la posicion 0 de la nueva lista toma el valor de 0
print(lista3)#imprimo lista3