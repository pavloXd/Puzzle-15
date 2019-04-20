import pickle
from functools import partial
from tkinter import *
from juego import Puzzle
from pickle import *



puzzle = Puzzle()

tablero= puzzle.getTablero()
listaBotones=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

ventana = Tk()
ventana.title("PUZZLE 15")
ventana.resizable(0,0)
#ventana.geometry("600x600")

miFrame= Frame()
miFrame.pack()
miFrame.config(heigh="600")
miFrame.config(width="600")

miFrame2= Frame()
miFrame2.pack()
miFrame2.config(heigh="50")
miFrame2.config(width="80")

def actualizarBotones():
    tablero=puzzle.getTablero()
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            # usamos esto para poder pasar argumenos a funciones con command
            global miFrame
            accion = partial(codigoBoton, i, j)
            listaBotones[i][j] = Button(miFrame, text=tablero[i][j], command=accion)
            listaBotones[i][j].grid(row=i, column=j, padx="5", pady="5")

    labelTurno = Label(miFrame2, text="Turno  " + str(puzzle.contadorTurno()))
    labelTurno.grid(row="1", column="2", padx="5", pady="5")
    if puzzle.comprobar():
        global ventana
        ventana.destroy()
        ventana2 = Tk()
        ventana2.title("PUZZLE 15")
        ventana2.resizable(0, 0)
        ventana2.grid()
        miFrame = Frame()
        miFrame.pack()
        miFrame.config(heigh="600")
        miFrame.config(width="600")
        labelGanador = Label(miFrame, text="ENHORA BUENA, HA GANADO CON "+str(300-puzzle.contadorTurno())+" puntos")
        labelGanador.grid(row="0", column="0", padx="5", pady="5")


def codigoBoton(i, j):
    tablero=puzzle.getTablero()
    numAux = puzzle.buscaPosicionVacia()
    if puzzle.esPosibleMover(i, j):
        if puzzle.esColindante(i, j):
            if int(numAux/4)==i:
                if numAux%4==(j+1):
                    puzzle.moverDerecha()
                elif numAux%4==(j-1):
                    puzzle.moverIzquierda()
            elif int(numAux/4)==(i-1):
                puzzle.moverArriba()

            elif int(numAux/4)==(i+1):
                puzzle.moverAbajo()
            actualizarBotones()

def cerrarPrograma():
    ventana.destroy()

def guardarPuzzle():
    pickle_file = open('todo.pickle', 'wb')
    pickle.dump(puzzle, pickle_file)

def rescatarPuzzle ():
    pickle_file = open('todo.pickle', "rb")
    todo = pickle.load(pickle_file)
    global puzzle
    puzzle=todo
    actualizarBotones()
def nuevoPuzzle():
    puzzleAux= Puzzle()
    global puzzle
    puzzle=puzzleAux
    actualizarBotones()




for i in range(len(tablero)):
    for j in range(len(tablero[i])):
        #usamos esto para poder pasar argumenos a funciones con command
        accion= partial(codigoBoton, i, j)
        listaBotones[i][j]=Button(miFrame, text=tablero[i][j], command=accion)
        listaBotones[i][j].grid(row=i, column=j, padx="5", pady="5")

botonSalir =Button(miFrame2, text="salir", command=cerrarPrograma)
botonSalir.grid(row="0", column="0", padx="5", pady="5")
botonGuardar =Button(miFrame2, text="guardar", command=guardarPuzzle)
botonGuardar.grid(row="0", column="1", padx="5", pady="5")
botonCargar =Button(miFrame2, text="cargar", command=rescatarPuzzle)
botonCargar.grid(row="0", column="2", padx="5", pady="5")
botonNuevo =Button(miFrame2, text="nuevo", command=nuevoPuzzle)
botonNuevo.grid(row="1", column="0", padx="5", pady="5")

labelTurno =Label(miFrame2, text="Turno  "+str(puzzle.contadorTurno()))
labelTurno.grid(row="1", column="2", padx="5", pady="5")



ventana.mainloop()