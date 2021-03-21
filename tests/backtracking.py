import random
import os
import sys
import time

sospechosos =  ["amigo", "novia", "vecino", "mensajero", "extranno", "hermanastro", "colegaDeTrabajo"]
armas = ["pistola", "cuchillo", "machete", "pala", "bate", "botella", "tubo", "cuerda"]
motivos = ["venganza", "celos", "dinero", "accidente", "drogas", "robo"]
partes_del_cuerpo = ["cabeza", "pecho", "abdomen", "espalda", "piernas", "brazos"]
lugares = ["sala", "comedor", "banno", "terraza", "cuarto", "garage", "patio", "balcon", "cocina"]

cartas_juego = [sospechosos,armas,motivos,partes_del_cuerpo,lugares]
cartas_correctas = []
cartas_incorrectas = []
parejas_restringidas = []

lista_soluciones = []
respuesta_final = []

lista_parejas_restringidas = [] #lista con todas las parejas



encontrado = False


def get_cartas_iniciales():
    """[Funcion en donde se obtienen la combinacion de cartas iniciales que debemos buscar]

    Args:
        Ninguno

    Returns:
        [list]: [Lista con las cartas obtenidas]
    """

    new_cartas = []
    for elemento in cartas_juego:
        new_cartas += [random.choice(elemento)]
    print ("cartas: ",new_cartas)
    return new_cartas

# El algoritmo de backtracking
def solucion_backtracking(cartas, cartas_escogidas, solucion, parejas):
    """[Funcion en donde se forman combinaciones recursivamente mediante backtracking hasta obtener la solucion]

    Args:
        cartas ([list]): [La lista de todas las cartas posibles]
        cartas_escogidas ([list]): [La lista de cartas que se escogieron como la solucion que se busca]
        solucion ([list]): [La lista con las cartas escogidas, es la combinacion que se desea probar]
        parejas ([list]): [La lista con todas las parejas restringidas que no pueden estar presentes en la solucion]

    Returns:
        [list]: [Lista con la solucion obtenida]
    """

    global encontrado
    global cartas_incorrectas
    global cartas_correctas
    global parejas_restringidas
    global lista_soluciones
    global respuesta_final

    if encontrado == True: # Si se encontro la solucion, se termina el algoritmo
        return

    if len(solucion) == len(cartas_juego): # Si se tiene la combinacion con las 5 cartas
        if solucion == cartas_escogidas: # Si la combinacion es igual a la solucion entonces se ha ganado

            lista_soluciones = lista_soluciones + [solucion]
            print("------------------------------------------ WIN  ----------------------------------")
            encontrado = True
            respuesta_final = solucion
            return solucion

        else: # Si la combinacion usa una de las cartas que han sido marcadas, se descarta
            for x in solucion:
                if x in cartas_incorrectas:
                    return

            for z in parejas_restringidas: # Si la combinacion tiene una de las parejas restringidas, se descarta
                if all(item in solucion for item in z) == True: #si tiene una pareja que fue detectada como restringida entonces se retorna
                    
                    return

            for y in parejas: # y es una pareja de la lista de parejas
                if all(item in solucion for item in y) == True: # Si tiene ambos objetos de la pareja en la solucion entonces no es una solucion valida
                    parejas_restringidas = parejas_restringidas + [y] # Se agrega la pareja restringida a la lista de parejas restringidas conocidas
                    return
            
            lista_soluciones = lista_soluciones + [solucion]

            randomIncorrecta = random.choice(solucion) # Se marca una carta aleatoriamente como incorrecta

            while randomIncorrecta in cartas_escogidas: # Si la carta que se escogio es parte de la solucion entonces se escoge otra
                randomIncorrecta = random.choice(solucion)

            cartas_incorrectas = cartas_incorrectas + [randomIncorrecta] # Se agrega la carta marcada a la lista de cartas marcadas como incorrectas

        solucion = []
    else:
        for i in cartas: # cada i es una categoria de las cartas del juego
            cartas = cartas[1:]
            for j in i: # cada j es un item perteneciente a una categoria
                solucion_backtracking(cartas, cartas_escogidas, solucion + [j], parejas) # Se forman las combinaciones recursivamente

# Se crean las parejas restringidas
def crearParejasAux():
    """[Funcion auxiliar para la funcion crearParejas. Crea una pareja restringida.]

    Args:
        Ninguno

    Returns:
        [list]: [Lista con la pareja restringida creada.]
    """

    cartasPareja = random.choice(cartas_juego)
    pareja1 = random.choice(cartasPareja)

    cartasPareja = random.choice(cartas_juego)
    pareja2 = random.choice(cartasPareja)

    while pareja1 == pareja2:
        pareja2 = random.choice(cartasPareja)
    fullPareja = [[pareja1] + [pareja2]]
    return fullPareja

def crearParejas(numParejas, cartas_escogidas):
    """[Funcion que crea la lista con todas las parejas restringidas]

    Args:
        numParejas (int): [La cantidad solicitada de parejas restringidas que se desea crear]
        cartas_escogidas ([list]): [La lista de cartas que se escogieron como la solucion que se busca]

    Returns:
        [list]: [Lista con las parejas restringidas]
    """

    parejas = []

    while numParejas != 0:
        fullPareja = crearParejasAux()

        while all(item in cartas_escogidas for item in
                  fullPareja) == True:  # si la solucion contiene las cartas de la pareja formada, entonces se crea otra pareja hasta que la pareja no invalide la solucion
            fullPareja = crearParejasAux()

        parejas = parejas + fullPareja
        numParejas = numParejas - 1

    return parejas

# La funcion de la corrida en si
def corrida_backtracking(numParejas,respuesta_juego):
    """[Funcion en donde se hace la corrida del algoritmo de backtracking y se corren todas las funciones necesarias para hacer esto]

    Args:
        numParejas (int): [La cantidad de parejas restringidas que se desea formar]
        respuesta_juego ([list]): [Las cartas iniciales que se escogieron como solucion]

    Returns:
        [list]: [Lista con las combinaciones formadas para llegar a la solucion deseada]
    """

    global encontrado
    global cartas_incorrectas
    global cartas_correctas
    global parejas_restringidas
    global lista_parejas_restringidas
    global lista_soluciones
    global respuesta_final

    encontrado = False    
    cartas_incorrectas = []
    cartas_correctas = []
    parejas_restringidas = []
    lista_parejas_restringidas = []
    lista_soluciones = []
    respuesta_final = []
    


    solucion_cartas = respuesta_juego # Se obtiene la solucion
    parejas = crearParejas(numParejas, solucion_cartas) # Y luego se hacen las parejas
    lista_parejas_restringidas = parejas

    solucion_backtracking(cartas_juego, solucion_cartas, [], parejas) # Para luego obtener la solucion mediante backtracking
    
    print("backtracking: ", lista_soluciones)
    return lista_soluciones

