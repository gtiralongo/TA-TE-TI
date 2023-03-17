import random as R 

#LEER UN ENTERO CON CONTROL DE ERROR DE TIPO DE DATO declarar fichas!!
def leerInt(cartel,desde=-9999999999,hasta=9999999999):
    salir = False
    numero = 0
    while not salir:
        try:
            numero = int(input(cartel))
            if numero < desde or  numero > hasta:
                print("ERROR ==> numero fuera de rango\n")
            else:
                salir = True
        except:
            print("ERROR ==> Ingrese un numero entero\n")
    return numero


class Ficha:
    def __init__(self,caracter):
        self.caracter = caracter
    
    def __str__(self):
        return '['+self.caracter+']'


class Tablero:

    def __init__(self,filas=3,columnas=3):
        self.cf = filas
        self.cc = columnas
        self.mat = []
        for f in range(self.cf):
            col = []
            for c in range(self.cc):
                col.append(Ficha(' '))
            self.mat.append(col)

    def __str__(self):
        cadena = ""
        for f in range(self.cf):
            for c in range(self.cc):
                cadena += str(self.mat[f][c])
            cadena += "\n" 
        return cadena

    def poner(self,f,c,ficha):
        self.mat[f][c] = ficha

    def ver(self,f,c):
        return self.mat[f][c]
        
    # def tableroVacio(self):
    #     salir = False
    #     cont = 0
    #     while cont < 9 and salir:
    #         for f in range(self.cf):
    #             for c in range(self.cc):
    #                 if str(self.mat[f][c]) == str(Ficha(" ")):
    #                     cont += 1
    #                     if cont > 9:
    #                         salir = True
    #     return True  
    
    
    def existe(self,ficha):
        for f in range(self.cf):
            for c in range(self.cc):
                
                if str(ficha) == str(self.mat[f][c]):
                    return True
        return False

    def filaIgual(self,fila,ficha):
        for c in range(self.cc):
            if str(ficha) != str(self.mat[fila][c]):
                return False
        return True
    
    def columnaIgual(self,columna,ficha):
        for f in range(self.cf):
            if str(ficha) != str(self.mat[f][columna]):
                return False
        return True

    def digonalIgual(self,ficha):
        for x in range(self.cf):
            if str(self.mat[x][x]) != str(ficha):
                return False
        return True

    def digonalSecIgual(self,ficha):
        f = 0
        c = self.cc-1
        while f < self.cf:
            if str(self.mat[f][c]) != str(ficha):
                return False
            f += 1
            c -= 1
        return True
    

class Jugador(object):
    
    def __init__(self,nombre,ficha):
        self.nombre = nombre
        self.ficha = ficha

    def __str__(self):
        return self.nombre + " ==> "+str(self.ficha)

    def jugar(self,tablero):
        pass


class Humano(Jugador):

    def __init__(self,nombre,ficha):
        Jugador.__init__(self,nombre,ficha)

    def jugar(self,tablero):
        salir = False
        while not salir:
            fila = leerInt("Fila: ",0,tablero.cf-1)
            columna = leerInt("Columna: ",0,tablero.cc-1)
            if str(tablero.ver(fila,columna)) == str(Ficha(' ')):
                salir = True
        return Coordenada(fila,columna)


class Computadora(Jugador):

    def __init__(self,nombre,ficha):
        Jugador.__init__(self,nombre,ficha)

    def jugar(self,tablero):
        salir = False
        while not salir:
            fila = R.randint(0,tablero.cf-1)
            columna = R.randint(0,tablero.cc-1)
            if str(tablero.ver(fila,columna)) == str(Ficha(' ')):
                salir = True
        return Coordenada(fila,columna)

class IA(Jugador):

    def __init__(self,nombre,ficha):
        Jugador.__init__(self,nombre,ficha)

    def esTateti(self,ficha,tablero):
            for fila in  range(tablero.cf):
                if tablero.filaIgual(fila,ficha):
                    return True
            for columna in range(tablero.cc):
                if tablero.columnaIgual(columna,ficha):
                    return True
            return tablero.digonalIgual(ficha) or tablero.digonalSecIgual(ficha)

    def jugar(self,tablero):
        salir = False
        miFicha = self.ficha
        if str(self.ficha) == str(Ficha("X")):
            suFucha = Ficha('O')
        else:
            suFicha = Ficha("X")
        while not salir:
            for f in range(tablero.cf):
                for c in range(tablero.cc):
                    if str(tablero.ver(f,c)) == str(Ficha(" ")):
                        tablero.poner(f,c,miFicha)
                        if self.esTateti(miFicha,tablero):
                            tablero.poner(f,c,Ficha(" "))
                            return Coordenada(f,c) 
                        else:
                            tablero.poner(f,c,Ficha(" "))
            
            for f in range(tablero.cf):
                for c in range(tablero.cc):
                    if str(tablero.ver(f,c)) == str(Ficha(" ")):
                        tablero.poner(f,c,suFicha)
                        if self.esTateti(suFicha,tablero):
                            tablero.poner(f,c,Ficha(" "))
                            return Coordenada(f,c) 
                        else:
                            tablero.poner(f,c,Ficha(" "))

            fila = R.randint(0,tablero.cf-1)
            columna = R.randint(0,tablero.cc-1)
            if str(tablero.ver(fila,columna)) == str(Ficha(' ')):
                salir = True
        return Coordenada(fila,columna)


class SUPERIA(Jugador):

    def __init__(self,nombre,ficha):
        Jugador.__init__(self,nombre,ficha)

    def esTateti(self,ficha,tablero):
            for fila in  range(tablero.cf):
                if tablero.filaIgual(fila,ficha):
                    return True
            for columna in range(tablero.cc):
                if tablero.columnaIgual(columna,ficha):
                    return True
            return tablero.digonalIgual(ficha) or tablero.digonalSecIgual(ficha)

    def tableroVacio(self,tablero):
        salir = False
        cont = 0
        while cont < 9 and salir:
            for f in range(tablero.cf):
                for c in range(tablero.cc):
                    if str(tablero.mat[f][c]) == str(Ficha(" ")):
                        cont += 1
                        if cont > 9:
                            salir = True
        return True

    def dondepone(self,tablero):
        cont = 0
        for f in range(tablero.cf):
                for c in range(tablero.cc):
                    if str(tablero.ver(f,c)) != str(Ficha(" ")):
                        cont += 1
                        return tablero.ver(f,c)
         

    def jugar(self,tablero):
        salir = False
        miFicha = self.ficha
        dPone = self.dondepone(tablero)
        if str(self.ficha) == str(Ficha("X")):
            suFucha = Ficha('O')
        else:
            suFicha = Ficha("X")
        for f in range(tablero.cf):
            for c in range(tablero.cc):
                if self.tableroVacio(tablero):
                    jugada = R.randint(0,1)
                    if jugada == 0:
                        ub = R.randint(1,4)
                        if ub == 1:
                            f=0
                            c=0
                        else:
                            if ub == 2:
                                f=0
                                c=2
                            else:
                                if ub == 3:
                                    f=2
                                    c=0
                                else:
                                    if ub == 4:                                    
                                        f=2
                                        c=2
                                        return Coordenada(f,c)
                    else:
                        if jugada == 1:
                            ub = R.randint(1,4)
                            if ub == 1:
                                f=1
                                c=0
                            else:
                                if ub == 2:
                                    f=0
                                    c=1
                                else:
                                    if ub == 3:
                                        f=2
                                        c=1
                                    else:
                                        if ub == 4:                                    
                                            f=1
                                            c=2
                            return Coordenada(f,c)
                        else:
                            if dPone == tablero.ver(0,0):
                                return Coordenada(1,1)
                            else:
                                if dPone == tablero.ver(2,0):
                                    return Coordenada(1,1)
               
                                                            
                #REMATE                
        for f in range(tablero.cf):
            for c in range(tablero.cc):
                if str(tablero.ver(f,c)) == str(Ficha(" ")):
                    tablero.poner(f,c,miFicha)
                    if self.esTateti(miFicha,tablero):
                        tablero.poner(f,c,Ficha(" "))
                        return Coordenada(f,c)
                    else:
                        tablero.poner(f,c,Ficha(" "))
                #DEFENSA    
        for f in range(tablero.cf):
            for c in range(tablero.cc):
                if str(tablero.ver(f,c)) == str(Ficha(" ")):
                    tablero.poner(f,c,suFicha)
                    if self.esTateti(suFicha,tablero):
                        tablero.poner(f,c,Ficha(" "))
                        return Coordenada(f,c) 
                    else:
                        tablero.poner(f,c,Ficha(" "))
                #RANDOM
        fila = R.randint(0,tablero.cf-1)
        columna = R.randint(0,tablero.cc-1)
        if str(tablero.ver(fila,columna)) == str(Ficha(' ')):
            salir = True
        return Coordenada(fila,columna)


class Coordenada:
    def __init__(self,fila=0,columna=0):
        self.fila = fila
        self.columna = columna


class Tateti:

    def __init__(self,jug1,jug2):
        self.jug1 = jug1
        self.jug2 = jug2
        self.tablero = Tablero()

    def jugarTateti(self):
        
        if R.randint(0,1) == 0:
            jugAux = self.jug1
        else:
            jugAux = self.jug2

        ganar = False
        print(str(self.tablero))
        
        while not ganar and self.tablero.existe(Ficha(' ')):
            print("JUEGA: " + str(jugAux))
            coor = jugAux.jugar(self.tablero)
            self.tablero.poner(coor.fila,coor.columna,jugAux.ficha)
            print(str(self.tablero))
            if self.esTateti(jugAux.ficha):
                ganar = True
            else:
                jugAux = self.elOtro(jugAux)
        if ganar:
            print("Ganador: " + str(jugAux))
        else:
            print("Empate!!!!!!!") 

    def elOtro(self,humano):
        if humano == self.jug2:
            return self.jug1
        return self.jug2

    def esTateti(self,ficha):
        for fila in  range(self.tablero.cf):
            if self.tablero.filaIgual(fila,ficha):
                return True
        for columna in range(self.tablero.cc):
            if self.tablero.columnaIgual(columna,ficha):
                return True
        return self.tablero.digonalIgual(ficha) or self.tablero.digonalSecIgual(ficha)     


def main():

    """
    h = Humano("Juan",Ficha('O'))
    c = Computadora("CompuJuan",Ficha('X'))

    print(str(h))
    print(str(c))
    t = Tablero()
    t.poner(0,0,Ficha('X'))
    t.poner(1,1,Ficha('X'))
    t.poner(2,2,Ficha('X'))
    print(str(t))
    """
    print("---------------")
    print(f"Comienza el Juego de TA-TE-TI\nPara poder jugar primero debe indicarnos su nombre. \nPara poner una ficha debe indicar la fila y luego la columna (tenga en cuanta que para ambos casos se comienza a contar del 0 al 2) ")
    print("===============")
    name_p1 = input("Escribe tu nombre:")
    juego = Tateti(Humano(name_p1,Ficha('X')),SUPERIA("Computer",Ficha('O')))
    juego.jugarTateti()


main()


