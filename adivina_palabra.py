print("Bienvenid@ al Juego")
print("Tu objetivo es adivina la palabra oculta, para lo cual tienes 5 intentos")

from random import choice

palabras = ["bosnia", "brasil", "tambien", "oculta", "precio"]
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

def validacion_dato(mi_valor):
    letras_validas = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,z"
    if mi_valor in letras_validas:
        print("Puede continuar")
    else:
        print("El valor ingresado debe ser una letra")

letra_a_validar = input("Ingrese una letra: ")
letra_a_validar.lower()
letra_a_validar.strip()
validacion_dato(letra_a_validar)

def buscarla_en_palabra (letra_a_validar):
    if letra_a_validar in palabra_elegida:
       letras_correctas.append(letra_a_validar)
    else:
       letras_incorrectas.append(letra_a_validar)
         
buscarla_en_palabra(letra_a_validar)
print(f'LETRAS INCORRECTAS:{letras_incorrectas}')
print(f'LETRAS CORRECTAS:{letras_correctas}')




    



