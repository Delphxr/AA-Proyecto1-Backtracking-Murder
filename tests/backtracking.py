import random
import os
import sys

sospechosos =  ["amigo", "novio", "vecino", "mensajero", "extranno", "hermanastro", "colega de trabajo"]
armas = ["pistola", "cuchillo", "machete", "pala", "bate", "botella", "tubo", "cuerda"]
motivos = ["venganza", "celos", "dinero", "accidente", "drogas", "robo"]
partes_del_cuerpo = ["cabeza", "pecho", "abdomen", "espalda", "piernas", "brazos"]
lugares = ["sala", "comedor", "banno", "terraza", "cuarto", "garage", "patio", "balcon", "cocina"]

cartas_juego = [sospechosos,armas,motivos,partes_del_cuerpo,lugares]
cartas_correctas = []
cartas_incorrectas = []

encontrado = False


def get_cartas_iniciales():
    """[obtenemos la combinacion de cartas iniciales que debemos buscar]
    Returns:
        [array]: [array con las cartas obtenidas]
    """
    new_cartas = []
    for elemento in cartas_juego:
        new_cartas += [random.choice(elemento)]
    print ("cartas: ",new_cartas)
    return new_cartas

solucion_cartas = get_cartas_iniciales()


def solucion_backtracking(cartas, solucion):
    global encontrado
    global cartas_incorrectas
    global cartas_correctas

    if encontrado == True:
        return

    print(solucion)

    for z in solucion:
        if z in cartas_incorrectas:
            return

    if len(solucion) == len(cartas_juego):
        if solucion == solucion_cartas:
            print("------------------------------------------ WIN  ----------------------------------")
            encontrado = True
            return solucion
        else:
            randomIncorrecta = random.choice(solucion)
            cartas_incorrectas = cartas_incorrectas + [randomIncorrecta]

        solucion = []
    else:
        for i in cartas: # cada i es una categoria de las cartas del juego
            cartas = cartas[1:]
            for j in i: # cada j es un item perteneciente a una categoria
                if j in solucion_cartas: # Si el item es parte de la solucion
                    if j not in cartas_correctas:
                        cartas_correctas = cartas_correctas + [j]
                else:
                    if j not in cartas_incorrectas:
                        cartas_incorrectas = cartas_incorrectas + [j]

                solucion_backtracking(cartas, solucion + [j])

def corrida_backtracking(numParejas):

    parejas = []
    while numParejas != 0:
        cartasPareja = random.choice(cartas_juego)
        pareja = random.choice(cartasPareja)
        parejas = parejas + [pareja]

        cartasPareja = random.choice(cartas_juego)
        pareja = random.choice(cartasPareja)
        parejas = parejas + [pareja]

        numParejas = numParejas - 1

    print("parejas:",parejas)

    print(solucion_backtracking(cartas_juego, []))

corrida_backtracking(1)