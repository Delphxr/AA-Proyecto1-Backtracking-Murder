import tkinter

# ojo, si este import no funciona tiene que usar esto en la terminal -> pip install pillow
from PIL import ImageTk, Image

#---------- Rutas Imagenes Cartas -------------- #
ruta_sospechosos = "../Assets/Images/Cartas/Sospechosos/"
ruta_armas = "../Assets/Images/Cartas/Armas/"
ruta_razon = "../Assets/Images/Cartas/Razon/"
ruta_cuerpo = "../Assets/Images/Cartas/Cuerpo/"
ruta_lugares = "../Assets/Images/Cartas/Lugares/"
# -----------------------------------------------#

# --------------pruebas --------------------#
test_array_cartas = ["novia", "bate", "dinero", "cabeza", "banno"]
test_array_cartas2 = ["mensajero", "bate", "dinero", "cabeza", "banno"]
test_array_cartas3 = ["amigo", "bate", "dinero", "cabeza", "banno"]
bool_test = 0





ventana = tkinter.Tk() #creamos la ventana
ventana.geometry("1280x720") #resolucion de la ventana
ventana.title("Pigclue") #titulo de la ventana



imagen_fondo = ImageTk.PhotoImage(Image.open("../Assets/Images/Fondo/fondo.png"))
fondo = tkinter.Label(ventana,image = imagen_fondo)
fondo.pack()


# ----------------- Inicializamos los labels de las primeras cartas ---------------------------#
posicion_y = 200 #posicion en y
posicion_x = 125 #pocision en x
#----------- sospechoso --------------#
label_sospechoso = tkinter.Label(ventana, text="") #creamos un label de prueba
label_sospechoso.place(x=posicion_x,y=posicion_y)
# ------------------------------------#

posicion_x += 210
#----------- armas --------------#
label_arma = tkinter.Label(ventana, text="") #creamos un label de prueba
label_arma.place(x=posicion_x,y=posicion_y)
# ------------------------------------#

posicion_x += 210
#----------- razon --------------#
label_razon = tkinter.Label(ventana, text="") #creamos un label de prueba
label_razon.place(x=posicion_x,y=posicion_y)
# ------------------------------------#

posicion_x += 210
#----------- cuerpo --------------#
label_cuerpo = tkinter.Label(ventana, text="") #creamos un label de prueba
label_cuerpo.place(x=posicion_x,y=posicion_y)
# ------------------------------------#

posicion_x += 210
#----------- lugar --------------#
label_lugar = tkinter.Label(ventana, text="") #creamos un label de prueba
label_lugar.place(x=posicion_x,y=posicion_y)
# ------------------------------------#
# ----------------------------------------------------------------------------------#


    



def actualizar_cartas(cartas):
    """[con esto actualizamos las imagenes de las cartas]

    Args:
        cartas ([list]): [recibimos el string de siempre que usamos en el backtracking y en el bruteforce, es importante 
                        que mantenga el orden de: [sospechoso, arma, razon, cuerpo, lugar]
    """    
    extencion = ".png" #formato de las imagenes

    #----------- sospechoso --------------#
    load1 = Image.open(ruta_sospechosos + cartas[0] + extencion)
    imagen1 = ImageTk.PhotoImage(load1)

    label_sospechoso.configure(image=imagen1)
    label_sospechoso.image = imagen1
    # ------------------------------------#

    #----------- armas --------------#
    load2 = Image.open(ruta_armas + cartas[1] + extencion)
    imagen2 = ImageTk.PhotoImage(load2)

    label_arma.configure(image=imagen2)
    label_arma.image = imagen2
    # ------------------------------------#

    #----------- razon --------------#
    load3 = Image.open(ruta_razon + cartas[2] + extencion)
    imagen3 = ImageTk.PhotoImage(load3)

    label_razon.configure(image=imagen3)
    label_razon.image = imagen3
    # ------------------------------------#


    #----------- cuerpo --------------#
    load4 = Image.open(ruta_cuerpo + cartas[3] + extencion)
    imagen4 = ImageTk.PhotoImage(load4)

    label_cuerpo.configure(image=imagen4)
    label_cuerpo.image = imagen4
    # ------------------------------------#


    #----------- lugar --------------#
    load5 = Image.open(ruta_lugares + cartas[4] + extencion)
    imagen5 = ImageTk.PhotoImage(load5)

    label_lugar.configure(image=imagen5)
    label_lugar.image = imagen5
    # ------------------------------------#


    
def callback(e):
    #esto se activa cada vez que apretamos enter, lo uso para probar la actualizacion de cartas
    global bool_test
    bool_test = (bool_test+1)%3

    if bool_test == 0:
        actualizar_cartas(test_array_cartas)
    elif bool_test == 1:
        actualizar_cartas(test_array_cartas2)
    else:
        actualizar_cartas(test_array_cartas3)





#para que tengamos unas imagenes al iniciar el programa
actualizar_cartas(test_array_cartas)


ventana.bind("<Return>",callback) #esto llama a callback cada vez que se apreta enter
ventana.mainloop() #hacemos el gameloop


