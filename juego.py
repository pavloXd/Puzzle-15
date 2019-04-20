import random
class Puzzle:


    def __init__(self):
        self.tableroCorrecto = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, '*']]
        self.tablero= self.creaPuzzle()
        self.turno=0


    def creaPuzzle(self):
        matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        ##Rellenamos el array
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                checker = False
                while checker is False:
                    numeroAleatorio = random.randrange(17)
                    checker = True
                    for k in range(len(matriz)):
                        if numeroAleatorio in matriz[k]:
                            checker = False
                matriz[i][j]=numeroAleatorio

        for l in range(len(matriz)):
            for p in range(len(matriz[l])):
                if matriz[l][p] is 16:
                    matriz[l][p]='*'
        return matriz


    def imprimir(self ):
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero[i])):
                if self.tablero[i][j] is '*':
                    print(self.tablero[i][j], end='  ')
                elif self.tablero[i][j]  <10:
                    print(self.tablero[i][j], end='  ')
                else:
                    print(self.tablero[i][j], end=' ')
            print()

    def buscaPosicionVacia(self ):
        suma=0
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero[i])):
                if self.tablero[i][j] is '*':
                    return suma
                suma=suma+1

    def moverIzquierda(self):
        numero=self.buscaPosicionVacia()
        if(numero%4 is not 3):
            tmp=self.tablero[int(numero/4)][(numero%4)+1]
            self.tablero[int(numero/4)][(numero%4)+1]='*'
            self.tablero[int(numero / 4)][(numero % 4)]=tmp
            self.turno=self.turno+1

    def moverDerecha(self):
        numero=self.buscaPosicionVacia()
        if(numero%4 is not 0):
            tmp=self.tablero[int(numero/4)][(numero%4)-1]
            self.tablero[int(numero/4)][(numero%4)-1]='*'
            self.tablero[int(numero / 4)][(numero % 4)]=tmp
            self.turno=self.turno+1



    def moverAbajo(self):
        numero=self.buscaPosicionVacia()
        if(numero>3):
            tmp=self.tablero[int(numero/4)-1][(numero%4)]
            self.tablero[int(numero/4)-1][(numero%4)]='*'
            self.tablero[int(numero / 4)][(numero % 4)]=tmp
            self.turno=self.turno+1


    def moverArriba(self):
        numero=self.buscaPosicionVacia()
        if(numero<12):
            tmp=self.tablero[int(numero/4)+1][(numero%4)]
            self.tablero[int(numero/4)+1][(numero%4)]='*'
            self.tablero[int(numero / 4)][(numero % 4)]=tmp
            self.turno=self.turno+1


    def comprobar(self):
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero[i])):
                if self.tableroCorrecto[i][j] != self.tablero[i][j]:
                    return False
        print("FIN, ES CORRECTO")
        return True

    def getTablero(self):
        return self.tablero
    def setTablero(self, tablero):
        self.tablero= tablero

    def esColindante(self, i, j): #busca que la posicion seleccionada sea colindante a la vacia
        aux=self.buscaPosicionVacia()
        if (int(aux/4))==i:
            if(aux%4==j-1 or aux%4==j+1):
                return True
            else:
                return False
        if (int(aux/4))==(i-1):
            if(aux%4==j):
                return True
            else:
                return False
        if (int(aux/4))==(i+1):
            if (aux % 4 == j):
                return True
            else:
                return False
        return False

    def esPosibleMover(self, i, j): #comprobamos si se puede mover
        aux=self.buscaPosicionVacia()
        if ((i*4)+j)==aux: #estamos pulsando el vacio
            return False
        else:
            return True

    def setContadorTurno(self, i):
        self.turno=i
    def contadorTurno(self):
        return self.turno
