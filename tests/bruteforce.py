import random
import os
import time

cartas_incorrectas = []
parejas_restringidas = []
encontrado = False

lista_soluciones_brute_force = []  # lista con todas las opciones que dio el algoritmo
cartas_juego = []


def create_cartas():
    """[Funcion que crea las cartas que se usaran en la corrida]
    Args:
        Ninguno
    Returns:
        [array]: [Array con las 5 categorias de cartas diferentes]
    """
    global cartas_juego

    sospechosos = ["amigo", "novia", "vecino", "mensajero", "extranno", "hermanastro", "colegaDeTrabajo"]
    armas = ["pistola", "cuchillo", "machete", "pala", "bate", "botella", "tubo", "cuerda"]
    motivos = ["venganza", "celos", "dinero", "accidente", "drogas", "robo"]
    partes_del_cuerpo = ["cabeza", "pecho", "abdomen", "espalda", "piernas", "brazos"]
    lugares = ["sala", "comedor", "banno", "terraza", "cuarto", "garage", "patio", "balcon", "cocina"]

    cartas_juego = [sospechosos, armas, motivos, partes_del_cuerpo, lugares]


def get_cartas_iniciales():
    """[Funcion que retorna la combinacion de cartas iniciales que debemos buscar]
        Args:
            Ninguno
        Returns:
            [array]: [Array con las cartas obtenidas]
        """
    random.seed(time.time_ns())
    create_cartas()
    new_cartas = []

    for elemento in cartas_juego:
        new_cartas += [random.choice(elemento)]

    print("\nCartas escogidas: ", new_cartas)
    return new_cartas


def get_incorrecta(cartas, solucion, respuesta):
    """[summary]
    Args:
        cartas ([list]): [cartas que usamos en el juego]
        solucion ([list]): [opcion de solucion que vamos a revisar si tiene una respuesta incorrecta]
        respuesta ([list]): [respuesta del juego que vamos a usar para comparar]
    Returns:
        [list]: [cartas que usamos durante el juego, pero sin la opcion incorrecta]
    """
    global cartas_incorrectas

    if solucion == respuesta:
        return cartas

    while True:
        carta = random.choice(solucion)

        if carta not in respuesta:
            carta_a_eliminar = carta
            cartas_incorrectas += [carta_a_eliminar]

            break
    for i in range(0, len(cartas)):
        if carta_a_eliminar in cartas[i]:
            cartas[i].remove(carta_a_eliminar)
            return cartas


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

def todas_combinaciones(cartas, solucion):
    """[Funcion para calcular todas las posibles combinaciones de cartas para usarlas en el algoritmo de fuerza bruta]
        Args:
            cartas ([list]): [Todas las cartas del juego]
            solucion ([list]): [La combinacion actual]
        Returns:
            lista_combinaciones_posibles ([list]): [Lista con todas las combinaciones posibles del juego]
    """

    global encontrado
    global cartas_juego
    global lista_combinaciones_posibles

    if encontrado == True:
        return

    if len(solucion) == 5:
        if len(lista_combinaciones_posibles) == 18144:
            lista_combinaciones_posibles = lista_combinaciones_posibles + [solucion]
            encontrado = True
            return lista_combinaciones_posibles

        lista_combinaciones_posibles = lista_combinaciones_posibles + [solucion]
        solucion = []
    else:
        for i in cartas:
            cartas = cartas[1:]
            for j in i:
                todas_combinaciones(cartas, solucion + [j])

def corrida_bruteforce(respuesta_juego):
    """[Funcion en donde se hace la corrida del algoritmo de fuerza bruta y se corren todas las funciones necesarias para hacer esto]
    Args:
        respuesta_juego ([list]): [Las cartas iniciales que se escogieron como solucion]
    Returns:
        [list]: [Lista con las combinaciones formadas para llegar a la solucion deseada]
    """

    global encontrado
    global lista_soluciones_brute_force
    global cartas_incorrectas
    global cartas_juego
    global lista_combinaciones_posibles

    lista_soluciones_brute_force = []
    lista_combinaciones_posibles = []
    cartas_escogidas = respuesta_juego
    todas_combinaciones(cartas_juego, [])

    solucion = []
    cartas_incorrectas = []
    contador = 0
    while solucion != cartas_escogidas:
        for combinacion in lista_combinaciones_posibles:
            for carta in combinacion:
                if carta not in cartas_incorrectas:
                    contador = contador + 1
            if contador == 5:
                solucion = combinacion
                lista_soluciones_brute_force = lista_soluciones_brute_force + [solucion]
                break
            contador = 0
        contador = 0
        carta_eliminar = random.choice(solucion)
        if carta_eliminar in cartas_escogidas:
            while carta_eliminar in cartas_escogidas:
                carta_eliminar = random.choice(solucion)
                if solucion == cartas_escogidas:
                    print("bruteforce: ", lista_soluciones_brute_force)
                    return lista_soluciones_brute_force
        cartas_incorrectas = cartas_incorrectas + [carta_eliminar]

    print("bruteforce: " , lista_soluciones_brute_force)
    return lista_soluciones_brute_force
