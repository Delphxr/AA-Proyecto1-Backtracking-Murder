import random
import os
import sys
import time

sospechosos =  ["amigo", "novio", "vecino", "mensajero", "extranno", "hermanastro", "colega de trabajo"]
armas = ["pistola", "cuchillo", "machete", "pala", "bate", "botella", "tubo", "cuerda"]
motivos = ["venganza", "celos", "dinero", "accidente", "drogas", "robo"]
partes_del_cuerpo = ["cabeza", "pecho", "abdomen", "espalda", "piernas", "brazos"]
lugares = ["sala", "comedor", "banno", "terraza", "cuarto", "garage", "patio", "balcon", "cocina"]

cartas_juego = [sospechosos,armas,motivos,partes_del_cuerpo,lugares]
cartas_correctas = []
cartas_incorrectas = []
parejas_restringidas = []

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


def solucion_backtracking(cartas, cartas_escogidas, solucion, parejas):
    global encontrado
    global cartas_incorrectas
    global cartas_correctas
    global parejas_restringidas

    if encontrado == True:
        return

    if len(solucion) == len(cartas_juego):
        if solucion == cartas_escogidas:
            print(solucion)
            print("------------------------------------------ WIN  ----------------------------------")
            encontrado = True
            return solucion

        else:
            for x in solucion:
                if x in cartas_incorrectas:
                    return

            for z in parejas_restringidas:
                if all(item in solucion for item in z) == True: #si tiene una pareja que fue detectada como restringida entonces se retorna
                    return

            print(solucion)
            randomIncorrecta = random.choice(solucion)

            while randomIncorrecta in cartas_escogidas:
                randomIncorrecta = random.choice(solucion)

            cartas_incorrectas = cartas_incorrectas + [randomIncorrecta]
            print("Combinacion incorrecta. Carta marcada como incorrecta (se descartaran futuras soluciones con esta carta):",randomIncorrecta)

            for y in parejas: # y es una pareja de la lista de parejas
                if all(item in solucion for item in y) == True: #si tiene ambos objetos de la pareja en la solucion entonces no es una solucion valida
                    parejas_restringidas = parejas_restringidas + [y]
                    print("Combinacion contiene pareja restringida (se descartan futuras soluciones con esta pareja):",y)
                    return

        solucion = []
    else:
        for i in cartas: # cada i es una categoria de las cartas del juego
            cartas = cartas[1:]
            for j in i: # cada j es un item perteneciente a una categoria
                solucion_backtracking(cartas, cartas_escogidas, solucion + [j], parejas)

def crearParejas(numParejas, cartas_escogidas):
    parejas = []
    fullPareja = []

    while numParejas != 0:
        cartasPareja = random.choice(cartas_juego)
        pareja1 = random.choice(cartasPareja)

        cartasPareja = random.choice(cartas_juego)
        pareja2 = random.choice(cartasPareja)

        while pareja1 == pareja2:
            pareja2 = random.choice(cartasPareja)

        fullPareja = [[pareja1] + [pareja2]]

        while all(item in cartas_escogidas for item in fullPareja) == True: #si la solucion contiene las cartas de la pareja formada, entonces se crea otra pareja hasta que la pareja no invalide la solucion
            print("La pareja no puede contradecir a la solucion. Pareja que contradecia solucion:", fullPareja)
            cartasPareja = random.choice(cartas_juego)
            pareja1 = random.choice(cartasPareja)
            cartasPareja = random.choice(cartas_juego)
            pareja2 = random.choice(cartasPareja)
            while pareja1 == pareja2:
                pareja2 = random.choice(cartasPareja)
            fullPareja = [[pareja1] + [pareja2]]
            print("La nueva pareja es:",fullPareja)

        parejas = parejas + fullPareja
        numParejas = numParejas - 1

    print("parejas:",parejas)
    return parejas

def corrida_backtracking(numParejas):
    solucion_cartas = get_cartas_iniciales()
    parejas = crearParejas(numParejas, solucion_cartas)

    print(solucion_backtracking(cartas_juego, solucion_cartas, [], parejas))

timeBefore = time.time_ns()
corrida_backtracking(15)
timeAfter = time.time_ns()
print("Tiempo total de runtime:",timeAfter - timeBefore)