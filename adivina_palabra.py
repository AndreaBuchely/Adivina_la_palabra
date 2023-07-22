print("Bienvenid@ al Juego")
print("Tu objetivo es adivinar la palabra oculta, para lo cual tienes 8 intentos")

from random import choice

palabras = ["antebrazos", "asteroides", "brillantes", "bronceador", "aerolineas"]
letras_incorrectas = []
letras_correctas = []
intentos = 3
aciertos = 0
juego_terminado = False
lista_oculta = []
lista_letras = []

def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)

    return palabra_elegida

def mostrar_nuevo_tablero(palabra_elegida):
    
    
    for l in palabra_elegida:
        lista_oculta.append("-")
        lista_letras.append(l)
            
    print(lista_oculta)

def validacion_dato(mi_valor):
    letras_validas = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,z"
    if mi_valor in letras_validas:
        print("Puede continuar")
    else:
        print("El valor ingresado debe ser una letra")

def  buscarla_en_palabra (letra_a_validar):
    if  letra_a_validar  in  palabra_elegida :
       letras_correctas.append(letra_a_validar)
    else:
       letras_incorrectas.append(letra_a_validar)

def reemplazar_valor(letra_a_validar):
    i = 0
    
    for valor in lista_letras:
      if valor == letra_a_validar:
        lista_oculta[i] = letra_a_validar
      i +=1  
        
    print(lista_oculta)

palabra_elegida = elegir_palabra(palabras)

mostrar_nuevo_tablero(palabra_elegida)

while intentos >= 0:
  letra_a_validar = input("Ingrese una letra: ")
  letra_a_validar.lower()
  letra_a_validar.strip()
  buscarla_en_palabra(letra_a_validar)

  if letra_a_validar in palabra_elegida:
        aciertos +=1
        reemplazar_valor(letra_a_validar)
  else:
        intentos -=1
  print(f'LETRAS INCORRECTAS:{letras_incorrectas}')
  print(f'LETRAS CORRECTAS:{letras_correctas}')
  
  if intentos <= 3:
    print(f'Este tu intento #',{intentos})

print("Fin del juego")  
         

  







    



