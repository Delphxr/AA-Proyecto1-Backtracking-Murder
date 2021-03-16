import random
import os
import time


cartas_correctas = []
cartas_incorrectas = []
parejas_restringidas = []
encontrado = False


lista_soluciones_brute_force = [] #lista con todas las opciones que dio el algoritmo
cartas_juego = []


def create_cartas():
    global cartas_juego

    sospechosos =  ["amigo", "novia", "vecino", "mensajero", "extranno", "hermanastro", "colegaDeTrabajo"]
    armas = ["pistola", "cuchillo", "machete", "pala", "bate", "botella", "tubo", "cuerda"]
    motivos = ["venganza", "celos", "dinero", "accidente", "drogas", "robo"]
    partes_del_cuerpo = ["cabeza", "pecho", "abdomen", "espalda", "piernas", "brazos"]
    lugares = ["sala", "comedor", "banno", "terraza", "cuarto", "garage", "patio", "balcon", "cocina"]

    cartas_juego = [sospechosos, armas, motivos, partes_del_cuerpo, lugares]

def get_cartas_iniciales():
    random.seed(time.time_ns())
    create_cartas()
    """[obtenemos la combinacion de cartas iniciales que debemos buscar]

    Returns:
        [array]: [array con las cartas obtenidas]
    """
    new_cartas = []

    for elemento in cartas_juego:
        new_cartas += [random.choice(elemento)]

    print("\n\n",new_cartas)
    return new_cartas


def get_incorrecta(cartas,solucion,respuesta):
    """[summary]

    Args:
        cartas ([list]): [cartas que usamos en el juego]
        solucion ([list]): [opcion de solucion que vamos a revisar si tiene una respuesta incorrecta]
        respuesta ([list]): [respuesta del juego que vamos a usar para comparar]

    Returns:
        [list]: [cartas que usamos durante el ju, pero sin la opcin incorrecta]
    """    
    if solucion == respuesta:
        return cartas
    
    carta_a_eliminar = ""
    while True:
        carta = random.choice(solucion)

        if carta not in respuesta:
            carta_a_eliminar = carta
            #print("opcion a incorrecta: ",carta_a_eliminar)
            break
    for i in range(0,len(cartas)):
        if carta_a_eliminar in cartas[i]:
            cartas[i].remove(carta_a_eliminar)
            #print("carta eliminada: ", cartas)
            return cartas
            
            

def solucion_bruteforce(cartas, cartas_escogidas, solucion):
    """[solucion usando fuerza bruta]

    Args:
        cartas ([list]): [las cartas que usamos para encontrar la solucion]
        cartas_escogidas ([list]): [la respuesta final del problema]
        solucion ([lsit]): [la solucion temporal]
        parejas ([list]): [las parejas restringuidas]

    Returns:
        [list]: [propuesta de solución]
    """    
    global encontrado
    global cartas_incorrectas
    global cartas_correctas
    global parejas_restringidas

    if encontrado == True:
        return
    solucion_temporal = []

    if len(solucion) == len(cartas_juego):
        #if solucion == cartas_escogidas:
        if True:
            encontrado = True
            return solucion
        else:
            # print("LOSE ")
            pass
        #print(solucion)

        solucion = []
    else:
        for i in cartas:
            cartas = cartas[1:]
            for j in i:
                j = random.choice(i) # Hace una combinacion al azar de cartas y de ahi se va refinando con las cartas incorrectas
                return solucion_bruteforce(cartas, cartas_escogidas, solucion + [j])


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

        while all(item in cartas_escogidas for item in
                  fullPareja) == True:  # si la solucion contiene las cartas de la pareja formada, entonces se crea otra pareja hasta que la pareja no invalide la solucion
            print("La pareja no puede contradecir a la solucion. Pareja que contradecia solucion:", fullPareja)
            cartasPareja = random.choice(cartas_juego)
            pareja1 = random.choice(cartasPareja)
            cartasPareja = random.choice(cartas_juego)
            pareja2 = random.choice(cartasPareja)
            while pareja1 == pareja2:
                pareja2 = random.choice(cartasPareja)
            fullPareja = [[pareja1] + [pareja2]]
            print("La nueva pareja es:", fullPareja)

        parejas = parejas + fullPareja
        numParejas = numParejas - 1

    #print("parejas:", parejas)
    return parejas


def corrida_bruteforce(respuesta_juego):
    global encontrado
    global lista_soluciones_brute_force 

    lista_soluciones_brute_force = []

    solucion_cartas = respuesta_juego
    cartas_juego_aux = cartas_juego
    solucion = []
    while solucion != solucion_cartas:

        solucion = solucion_bruteforce(cartas_juego_aux, solucion_cartas, [])
        lista_soluciones_brute_force += [solucion]
        #print(solucion)

        cartas_juego_aux = get_incorrecta(cartas_juego_aux,solucion,solucion_cartas) #eliminamos una carta incorrecta de la lista de cartas viables
        #input()
        encontrado = False
    print("bruteforce: ",lista_soluciones_brute_force)
    return lista_soluciones_brute_force




