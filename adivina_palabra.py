print("Bienvenid@ al Juego")
print("Tu objetivo es adivina la palabra oculta, para lo cual tienes 5 intentos")

from random import choice

palabras = ["diccionario", "cascabel", "mandarina", "camioneta", "cuaderno"]
letras_incorrectas = []
letras_correctas = []
intentos = 5
aciertos = 0
juego_terminado = False

def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)

    return palabra_elegida

palabra = elegir_palabra(palabras)


def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta =[]
    
    for l in palabra_elegida:
        lista_oculta.append("-")
    
    print(lista_oculta)

palabra_elegida = elegir_palabra(palabras)

mostrar_nuevo_tablero(palabra_elegida)



