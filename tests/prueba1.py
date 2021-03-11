import random
import os

sospechosos =  ["amigo", "novio", "vecino", "mensajero", "extranno", "hermanastro", "colega de trabajo"]
armas = ["pistola", "cuchillo", "machete", "pala", "bate", "botella", "tubo", "cuerda"]
motivos = ["venganza", "celos", "dinero", "accidente", "drogas", "robo"]
partes_del_cuerpo = ["cabeza", "pecho", "abdomen", "espalda", "piernas", "brazos"]
lugares = ["sala", "comedor", "banno", "terraza", "cuarto", "garage", "patio", "balcon", "cocina"]

cartas_juego = [sospechosos,armas,motivos,partes_del_cuerpo,lugares]

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



def solucion_backtracking(cartas, solucion=[]):
    global encontrado
    if encontrado == True:
        return
    solucion_temporal = []

    if len(solucion) == len(cartas_juego):
        if solucion == solucion_cartas:
            print ("------------------------------------------ WIN  ----------------------------------")
            encontrado = True
            return solucion
        else:
            #print("LOSE ")   
            pass
        print(solucion)
        
        solucion = []
    else:
        for i in cartas:
            cartas = cartas[1:]
            for j in i:
                
                solucion_backtracking(cartas, solucion + [j])
        

            
    

print(solucion_backtracking(cartas_juego))
input()
