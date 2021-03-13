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


def solucion_backtracking(cartas, solucion, parejas):
    global encontrado
    global cartas_incorrectas
    global cartas_correctas

    if encontrado == True:
        return

    if len(solucion) == len(cartas_juego):
        if solucion == solucion_cartas:
            print(solucion)
            print("------------------------------------------ WIN  ----------------------------------")
            encontrado = True
            return solucion

        else:
            for x in solucion:
                if x in cartas_incorrectas:
                    return

            print(solucion)
            randomIncorrecta = random.choice(solucion)

            while randomIncorrecta in solucion_cartas:
                randomIncorrecta = random.choice(solucion)

            cartas_incorrectas = cartas_incorrectas + [randomIncorrecta]
            print("Incorrecta. Marcada:",randomIncorrecta)

            for y in parejas: # y es una pareja de la lista de parejas
                if all(item in solucion for item in y) == True: # si tiene ambos objetos de la pareja en la solucion entonces no es una solucion valida
                    print("Contiene pareja restringida")
                    return

        solucion = []
    else:
        for i in cartas: # cada i es una categoria de las cartas del juego
            cartas = cartas[1:]
            for j in i: # cada j es un item perteneciente a una categoria
                solucion_backtracking(cartas, solucion + [j], parejas)

def corrida_backtracking(numParejas):

    parejas = []
    while numParejas != 0:
        cartasPareja = random.choice(cartas_juego)
        pareja1 = random.choice(cartasPareja)

        cartasPareja = random.choice(cartas_juego)
        pareja2 = random.choice(cartasPareja)

        parejas = parejas + [[pareja1] + [pareja2]]

        numParejas = numParejas - 1

    print("parejas:",parejas)

    print(solucion_backtracking(cartas_juego, [], parejas))

corrida_backtracking(15)