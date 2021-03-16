import tkinter
from tkinter import ttk
import backtracking
import bruteforce

# ojo, si este import no funciona tiene que usar esto en la terminal -> pip install pillow
from PIL import ImageTk, Image

global lista_soluciones
global lista_soluciones_BF
global contador_solucion
global lista_parejas_restringidas

contador_solucion = 0
respuesta_juego = []
lista_soluciones = []
lista_soluciones_BF = []
lista_parejas_restringidas = []



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
cartas_vacias = ["nada","nada","nada","nada","nada"]
# ------------------------------------------#



# ------------- Creamos la ventana del programa ------------------ #
ventana = tkinter.Tk() #creamos la ventana
ventana.geometry("1280x720") #resolucion de la ventana
ventana.title("Pigclue") #titulo de la ventana

# ----------------------------------------------------------------#

# ------------- Colocamos el fondo del programa -------------------------------------- #
imagen_fondo = ImageTk.PhotoImage(Image.open("../Assets/Images/Fondo/fondoInfo.png"))
fondo = tkinter.Label(ventana,image = imagen_fondo)
fondo.pack()
# ------------------------------------------------------------------------------------- #

# -------------- Creamos los labels de informacion -------------- #

#intentos
cantidad_intentos =0
variable_intentos = tkinter.StringVar()
variable_intentos.set(cantidad_intentos)
label_intentos = tkinter.Label(ventana,textvariable=variable_intentos,bg="#2c0317",fg="White")
label_intentos.config(font=("Consolas", 28))
label_intentos.place(x=1225,y=162)

#% acierto backtracking
porcentage_backtracking =0
variable_porcentage_backtracking = tkinter.StringVar()
variable_porcentage_backtracking.set(porcentage_backtracking)
label_porcentage_backtracking = tkinter.Label(ventana,textvariable=variable_porcentage_backtracking,bg="#3c0620",fg="White")
label_porcentage_backtracking.config(font=("Consolas", 24))
label_porcentage_backtracking.place(x=1225,y=214)

#% acierto fuerza bruta
porcentage_bf =0
variable_porcentage_bf = tkinter.StringVar()
variable_porcentage_bf.set(porcentage_bf)
label_porcentage_bf = tkinter.Label(ventana,textvariable=variable_porcentage_bf,bg="#2c0317",fg="White")
label_porcentage_bf.config(font=("Consolas", 28))
label_porcentage_bf.place(x=1225,y=260)

# no de restrucciones
cantidad_restricciones =0
variable_restricciones = tkinter.StringVar()
variable_restricciones.set(cantidad_restricciones)
label_restricciones = tkinter.Label(ventana,textvariable=variable_restricciones,bg="#3c0620",fg="White")
label_restricciones.config(font=("Consolas", 28))
label_restricciones.place(x=1225,y=310)


# ---------------------------------------------------------------- #

# ----------------- Lista con las cartas incorrectas --------------------------- #

scrollbar = tkinter.Scrollbar(ventana, orient=tkinter.VERTICAL)

lista_incorrectas = tkinter.Listbox(ventana, yscrollcommand=scrollbar.set, bg="#530d2c",fg="White",selectbackground="#530d2c",width="34",height="6",font=("Consolas", 15),activestyle="none",borderwidth="0",highlightcolor="#530d2c",relief="flat", highlightbackground="#530d2c")

scrollbar.config(command=lista_incorrectas.yview)

scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
lista_incorrectas.place(x=909,y=498)

# metemos unos elementos de prueba
for i in range(50):
    lista_incorrectas.insert(tkinter.END, i)

# ---------------------------------------------------------------- #

# ----------------- Lista con las cartas parejas restringidas --------------------------- #

scrollbar2 = tkinter.Scrollbar(ventana, orient=tkinter.VERTICAL)

lista_restringidas = tkinter.Listbox(ventana, yscrollcommand=scrollbar2.set, bg="#3f071e",fg="White",selectbackground="#3f071e",width="40",height="5",font=("Consolas", 20),activestyle="none",borderwidth="0",highlightcolor="#3f071e",relief="flat", highlightbackground="#3f071e")

scrollbar2.config(command=lista_incorrectas.yview)

scrollbar2.pack(side=tkinter.RIGHT, fill=tkinter.Y)
lista_restringidas.place(x=160,y=550)

def insertar_lista_retringida(lista_parejas):
    index = 1
    for pareja in lista_parejas:
        juntas = str(index) + ") " + pareja[0].capitalize() + " - " + pareja[1].capitalize()
        lista_restringidas.insert(tkinter.END, juntas)
        index+=1

# ---------------------------------------------------------------- #

# ---------------- insertar el numero de resticciones ---------- #
frame_texto = tkinter.Frame(ventana,width=64,height=32)
frame_texto.place(x=900,y=640)
frame_texto.columnconfigure(0,weight=10)
frame_texto.grid_propagate(False)
frame_texto.place(x=1000,y=677)


caja_texto = tkinter.Text(frame_texto,width="64",height="64",font=("Consolas", 20),bg="#3f071e",fg="White",borderwidth="0",highlightcolor="#3f071e",relief="flat", highlightbackground="#3f071e")
caja_texto.grid()
caja_texto.insert(tkinter.INSERT, "2")


# ---------------------------------------------------------------- #


# ---------------- funcion para obtener porcentaje ---------- #
def get_porcentage(cartas):
    porcentage = 0
    for carta in cartas:
        if carta in respuesta_juego:
            porcentage += 1
    return porcentage

# ---------------------------------------------------------------- #

# -------------- Creamos el boton de siguiente paso -------------- #
def boton_siguiente():
    """[funcion que decide lo que sucede al presionar el boton de siguiente]
    """
    global cantidad_intentos
    global contador_solucion
    

    new_cartas = []
    if contador_solucion < len(lista_soluciones):
        cartas_backtracking.actualizar_cartas(lista_soluciones[contador_solucion])
        cartas_fuerza_bruta.actualizar_cartas(lista_soluciones_BF[contador_solucion])

        variable_porcentage_backtracking.set(get_porcentage(lista_soluciones[contador_solucion]))
        variable_porcentage_bf.set(get_porcentage(lista_soluciones_BF[contador_solucion]))

        #lista_incorrectas.insert(tkinter.END, incorecta) #cuando se tenga una lista de las incorrectas se añade aquí

        print(contador_solucion)
        contador_solucion = contador_solucion + 1
        variable_intentos.set(contador_solucion)

        
load_siguiente = Image.open("../Assets/Images/Botones/siguiente.png")
imagen_siguiente = ImageTk.PhotoImage(load_siguiente)
boton_siguiente = tkinter.Button(ventana,image=imagen_siguiente, command=boton_siguiente)
boton_siguiente.place(x=1200,y=640)
# ---------------------------------------------------------------- #



# -------------- Creamos el boton de reinicio -------------------- #
def boton_reinicio():
    """[funcion que decide lo que sucede al presionar el boton de reinicio]
    """
    nuevo_juego()
    

load_reinicio = Image.open("../Assets/Images/Botones/reiniciar.png")
imagen_reinicio = ImageTk.PhotoImage(load_reinicio)
boton_reinicio = tkinter.Button(ventana,image=imagen_reinicio, command=boton_reinicio)
boton_reinicio.place(x=1100,y=640)
# ---------------------------------------------------------------- #

def nuevo_juego():
    global contador_solucion
    global respuesta_juego
    global lista_soluciones
    global lista_soluciones_BF

    numero_restricciones = caja_texto.get("1.0", "end-1c")

    if numero_restricciones.isnumeric() == True:
        numero_restricciones = int(numero_restricciones)
    else:
        numero_restricciones = 0


    contador_solucion = 0
    respuesta_juego = bruteforce.get_cartas_iniciales()
    
    lista_soluciones = backtracking.corrida_backtracking(numero_restricciones,respuesta_juego)
    lista_soluciones_BF = bruteforce.corrida_bruteforce(respuesta_juego)

    cartas_respuesta.actualizar_cartas(respuesta_juego)
    cartas_fuerza_bruta.actualizar_cartas(cartas_vacias)
    cartas_backtracking.actualizar_cartas(cartas_vacias)

    variable_porcentage_backtracking.set(0)
    variable_porcentage_bf.set(0)
    variable_intentos.set(0)

    lista_restringidas.delete('0','end') #con esto vaciamos las restringidas
    insertar_lista_retringida(list(backtracking.lista_parejas_restringidas))
    #lista_incorrectas.delete('0','end') #con esto vaciamos las incorrectas


class Cartas():
    """[esta clase la usamos cuando queremos crear otro conjunto de 5 cartas]
    """
    def __init__(self,posicionx,posiciony,tamanno=[180,280],espacio=20):
        """[creacion de un objeto cartas]

        Args:
            posicionx ([int]): [la posicion en x de la carta inicial]
            posiciony ([int]): [la pocision en y de la carta inicial]
            tamanno (list, optional): [el tamaño que van a tener las cartas, en pixeles]. Defaults to [180,280].
            espacio ([int]): [la cantidad de pixeles entre cada carta]. Defaults to 20
        """
        self.posicion_y = posiciony
        self.posicion_x = posicionx
        self.size_x = tamanno[0]
        self.size_y = tamanno[1]
        self.separacion = self.size_x + espacio

        #inicializamos los valores de las cartas:

        #----------- sospechoso --------------#
        self.label_sospechoso = tkinter.Label(ventana, text="") #creamos un label de prueba
        self.label_sospechoso.place(x=self.posicion_x,y=self.posicion_y)
        # ------------------------------------#

        self.posicion_x += self.separacion
        #----------- armas --------------#
        self.label_arma = tkinter.Label(ventana, text="") #creamos un label de prueba
        self.label_arma.place(x=self.posicion_x,y=self.posicion_y)
        # ------------------------------------#

        self.posicion_x += self.separacion
        #----------- razon --------------#
        self.label_razon = tkinter.Label(ventana, text="") #creamos un label de prueba
        self.label_razon.place(x=self.posicion_x,y=self.posicion_y)
        # ------------------------------------#

        self.posicion_x += self.separacion
        #----------- cuerpo --------------#
        self.label_cuerpo = tkinter.Label(ventana, text="") #creamos un label de prueba
        self.label_cuerpo.place(x=self.posicion_x,y=self.posicion_y)
        # ------------------------------------#

        self.posicion_x += self.separacion
        #----------- lugar --------------#
        self.label_lugar = tkinter.Label(ventana, text="") #creamos un label de prueba
        self.label_lugar.place(x=self.posicion_x,y=self.posicion_y)

    def actualizar_cartas(self,cartas):
        """[con esto actualizamos las imagenes de las cartas]

        Args:
            cartas ([list]): [recibimos el string de siempre que usamos en el backtracking y en el bruteforce, es importante
                            que mantenga el orden de: [sospechoso, arma, razon, cuerpo, lugar]
        """
        extencion = ".png" #formato de las imagenes

        #----------- sospechoso --------------#
        self.load1 = Image.open(ruta_sospechosos + cartas[0] + extencion)
        self.load1 = self.load1.resize((self.size_x, self.size_y), Image.NEAREST)
        self.imagen1 = ImageTk.PhotoImage(self.load1)

        self.label_sospechoso.configure(image=self.imagen1)
        self.label_sospechoso.image = self.imagen1
        # ------------------------------------#

        #----------- armas --------------#
        self.load2 = Image.open(ruta_armas + cartas[1] + extencion)
        self.load2 = self.load2.resize((self.size_x, self.size_y), Image.NEAREST)
        self.imagen2 = ImageTk.PhotoImage(self.load2)

        self.label_arma.configure(image=self.imagen2)
        self.label_arma.image = self.imagen2
        # ------------------------------------#

        #----------- razon --------------#
        self.load3 = Image.open(ruta_razon + cartas[2] + extencion)
        self.load3 = self.load3.resize((self.size_x, self.size_y), Image.NEAREST)
        self.imagen3 = ImageTk.PhotoImage(self.load3)

        self.label_razon.configure(image=self.imagen3)
        self.label_razon.image = self.imagen3
        # ------------------------------------#


        #----------- cuerpo --------------#
        self.load4 = Image.open(ruta_cuerpo + cartas[3] + extencion)
        self.load4 = self.load4.resize((self.size_x, self.size_y), Image.NEAREST)
        self.imagen4 = ImageTk.PhotoImage(self.load4)

        self.label_cuerpo.configure(image=self.imagen4)
        self.label_cuerpo.image = self.imagen4
        # ------------------------------------#


        #----------- lugar --------------#
        self.load5 = Image.open(ruta_lugares + cartas[4] + extencion)
        self.load5 = self.load5.resize((self.size_x, self.size_y), Image.NEAREST)
        self.imagen5 = ImageTk.PhotoImage(self.load5)

        self.label_lugar.configure(image=self.imagen5)
        self.label_lugar.image = self.imagen5
        # ------------------------------------#


# ------------- generamos los sets de cartas necesarios para el programa -------- #
cartas_backtracking = Cartas(160,45,[125,195])
cartas_fuerza_bruta = Cartas(160,300,[125,195])
cartas_respuesta = Cartas(918,358,[57,89],15)

#cartas_restriccion1 = Cartas(190,580,[82,127],60)
#cartas_restriccion2 = Cartas(160,555,[82,127],60)
# --------------------------------------------------------------------------------#

#para que tengamos unas imagenes al iniciar el programa
cartas_fuerza_bruta.actualizar_cartas(cartas_vacias)
cartas_backtracking.actualizar_cartas(cartas_vacias)
cartas_respuesta.actualizar_cartas(cartas_vacias)
#cartas_restriccion1.actualizar_cartas(cartas_vacias)
#cartas_restriccion2.actualizar_cartas(cartas_vacias)



nuevo_juego()
ventana.mainloop() #hacemos el gameloop


