# generar tic tac toe
import random

def mostrar_tablero():
   tablero = [[x for x in range (3)] for y in range(3)]

   for x in range (len(tablero)):
      if x != 0:
         print("")
         print("_"* 40)
         
      for y in range (len(tablero[x])):
        print (y, end="\t | \t")
        


    
mostrar_tablero()

""" opcion = 0
while opcion != 50002:
    print(opcion)
    opcion = opcion +2 """

""" 
    salir = "no"
    while salir != "si": 

    opcion = input("Elige piedra, papel o tijeras: ")

    opciones = ["piedra", "papel", "tijeras"]
    indice_aleatorio = random.randint(0, len(opciones) - 1) # Genera un entero entre 0 y 2 (incluidos)

    maquina = opciones[indice_aleatorio]

    if opcion == maquina:
        print("Empate")
    elif opcion == "piedra":
        if maquina == "papel":
            print("pierdes")
        elif maquina == "tijeras":
            print("ganas")
    elif opcion == "papel":
        if maquina == "piedra":
            print("ganas")
        elif maquina == "tijeras":
            print("pierdes")
    elif opcion == "tijeras":
        if maquina == "piedra":
            print("pierdes")
        elif maquina == "papel":
            print("ganas")

    salir = input("deseas salir: ") """