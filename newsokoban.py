from os import system, name
import random

class Sokoban:
    map = []
    posy = 0
    posx = 0
    nivel = open("lv0.soko", "r")

    def __init__(self):
        print("Sokoban v1.0.0 Por Jesús Antonio Torres \na - Izquierda \nd - Derecha \nw - Arriba \ns - Abajo")

    def crearMapa(self):
        for row in self.nivel:
            linea = []
            for digito in row:
                if digito == "\n":
                    continue
                linea.append(int(digito))
            self.map.append(linea)

    def imprimirMapa(self):
        for fila in self.map:
            for casilla in fila:
                if casilla == 0:
                    print("  ", end="")
                elif casilla == 1:
                    print(chr(128125), end="")
                elif casilla == 2:
                    print(chr(127921), end= "")
                elif casilla == 4:
                    print(chr(128142), end="")
                elif casilla == 5:
                    print(chr(128125), end="")
                elif casilla == 6:
                    print(chr(129535), end="")
                else:
                    print(casilla, end="")
            print()

    def limpiarPantalla(self):
        if name == "nt":
            system("cls")
        else:
            system("clear")

    def encontrarSoko(self):
        for linea in self.map:
            if 1 in linea:
                self.posy = self.map.index(linea)
                self.posx = linea.index(1)
            elif 5 in linea:
                self.posy = self.map.index(linea)
                self.posx = linea.index(5)

    def movDerecha(self):
        #Muñeco, Espacio
        if self.map[self.posy][self.posx] == 1 and self.map[self.posy][self.posx + 1] == 0:
            self.map[self.posy][self.posx] = 0
            self.map[self.posy][self.posx + 1] = 1
            self.posx += 1
        #Muñeco, Meta
        elif self.map[self.posy][self.posx] == 1 and self.map[self.posy][self.posx + 1] == 4:
            self.map[self.posy][self.posx] = 0
            self.map[self.posy][self.posx + 1] = 5
            self.posx += 1
        #Muñeco, Caja, Espacio
        elif self.map[self.posy][self.posx] == 1 and self.map[self.posy][self.posx + 1] == 2 and self.map[self.posy][self.posx + 2] == 0:
            self.map[self.posy][self.posx] = 0
            self.map[self.posy][self.posx + 1] = 1
            self.map[self.posy][self.posx + 2] = 2
            self.posx += 1
        #Muñeco, Caja, Meta
        elif self.map[self.posy][self.posx] == 1 and self.map[self.posy][self.posx + 1] == 2 and self.map[self.posy][self.posx + 2] == 4:
            self.map[self.posy][self.posx] = 0
            self.map[self.posy][self.posx + 1] = 1
            self.map[self.posy][self.posx + 2] = 6
            self.posx += 1
        #Muñeco-meta,  Espacio
        elif self.map[self.posy][self.posx] == 5 and self.map[self.posy][self.posx + 1] == 0:
            self.map[self.posy][self.posx] = 4
            self.map[self.posy][self.posx + 1] = 1
            self.posx += 1
        #Muñeco-meta, Meta
        elif self.map[self.posy][self.posx] == 5 and self.map[self.posy][self.posx + 1] == 4:
            self.map[self.posy][self.posx] = 4
            self.map[self.posy][self.posx + 1] = 5
            self.posx += 1
        #Muñeco-meta,  Caja, Espacio
        elif self.map[self.posy][self.posx] ==  5 and self.map[self.posy][self.posx + 1] == 2 and self.map[self.posy][self.posx + 2] == 0:
            self.map[self.posy][self.posx] = 4
            self.map[self.posy][self.posx + 1] = 1
            self.map[self.posy][self.posx + 2] = 2
            self.posx += 1
        #Muñeco-meta, Caja, Meta
        elif self.map[self.posy][self.posx] == 5 and self.map[self.posy][self.posx + 1] == 2 and self.map[self.posy][self.posx + 2] == 4:
            self.map[self.posy][self.posx] = 4
            self.map[self.posy][self.posx + 1] = 1
            self.map[self.posy][self.posx + 2] = 6
            self.posx += 1
        #Muñeco-meta, Caja-meta, Espacio
        elif self.map[self.posy][self.posx] == 5 and self.map[self.posy][self.posx + 1] == 6 and self.map[self.posy][self.posx + 2] == 0:
            self.map[self.posy][self.posx] = 4
            self.map[self.posy][self.posx + 1] = 5
            self.map[self.posy][self.posx + 2] = 2
            self.posx += 1
        #Muñeco-meta, Caja-meta, Meta
        elif self.map[self.posy][self.posx] == 5 and self.map[self.posy][self.posx + 1] == 6 and self.map[self.posy][self.posx + 2] == 4:
            self.map[self.posy][self.posx] = 4
            self.map[self.posy][self.posx + 1] = 5
            self.map[self.posy][self.posx + 2] = 6
            self.posx += 1
        #Muñeco, Caja-meta, Espacio
        elif self.map[self.posy][self.posx] == 1 and self.map[self.posy][self.posx + 1] == 6 and self.map[self.posy][self.posx + 2] == 0:
            self.map[self.posy][self.posx] = 0
            self.map[self.posy][self.posx + 1] = 5
            self.map[self.posy][self.posx + 2] = 2
            self.posx += 1
        #Muñeco, Caja-meta, Meta
        elif self.map[self.posy][self.posx] == 1 and self.map[self.posy][self.posx + 1] == 6 and self.map[self.posy][self.posx + 2] == 4:
            self.map[self.posy][self.posx] = 0
            self.map[self.posy][self.posx + 1] = 5
            self.map[self.posy][self.posx + 2] = 6
            self.posx += 1

    def movIzquierda(self):
        #Espacio, Muñeco
        if self.map[self.posy][self.posx] == 1 and self.map[self.posy][self.posx - 1] == 0:
            self.map[self.posy][self.posx] = 0
            self.map[self.posy][self.posx - 1] = 1
            self.posx -= 1
        #Meta, Muñeco
        elif self.map[self.posy][self.posx] == 1 and self.map[self.posy][self.posx - 1] == 4:
            self.map[self.posy][self.posx] = 0
            self.map[self.posy][self.posx - 1] = 5
            self.posx -= 1
        #Espacio, Caja, Muñeco
        elif self.map[self.posy][self.posx] == 1 and self.map[self.posy][self.posx - 1] == 2 and self.map[self.posy][self.posx - 2] == 0:
            self.map[self.posy][self.posx] = 0
            self.map[self.posy][self.posx - 1] = 1
            self.map[self.posy][self.posx - 2] = 2
            self.posx -= 1
        #Meta, Caja, Muñeco
        elif self.map[self.posy][self.posx] == 1 and self.map[self.posy][self.posx - 1] == 2 and self.map[self.posy][self.posx - 2] == 4:
            self.map[self.posy][self.posx] = 0
            self.map[self.posy][self.posx - 1] = 1
            self.map[self.posy][self.posx - 2] = 6
            self.posx -= 1
        #Espacio, Muñeco-meta
        elif self.map[self.posy][self.posx] == 5 and self.map[self.posy][self.posx - 1] == 0:
            self.map[self.posy][self.posx] = 4
            self.map[self.posy][self.posx - 1] = 1
            self.posx -= 1
        #Meta, Muñeco-meta
        elif self.map[self.posy][self.posx] == 5 and self.map[self.posy][self.posx - 1] == 4:
            self.map[self.posy][self.posx] = 4
            self.map[self.posy][self.posx - 1] = 5
            self.posx -= 1
        #Espacio, Caja, Muñeco-meta
        elif self.map[self.posy][self.posx] == 5 and self.map[self.posy][self.posx - 1] == 2 and self.map[self.posy][self.posx - 2] == 0:
            self.map[self.posy][self.posx] = 4
            self.map[self.posy][self.posx - 1] = 1
            self.map[self.posy][self.posx - 2] = 2
            self.posx -= 1
        #Meta, Caja, Muñeco-meta
        elif self.map[self.posy][self.posx] == 1 and self.map[self.posy][self.posx - 1] == 2 and self.map[self.posy][self.posx - 2] == 4:
            self.map[self.posy][self.posx] = 0
            self.map[self.posy][self.posx - 1] = 1
            self.map[self.posy][self.posx - 2] = 6
            self.posx -= 1
        #Espacio, Caja-meta, Muñeco-meta
        elif self.map[self.posy][self.posx] == 5 and self.map[self.posy][self.posx - 1] == 6 and self.map[self.posy][self.posx - 2] == 0:
            self.map[self.posy][self.posx] = 4
            self.map[self.posy][self.posx - 1] = 5
            self.map[self.posy][self.posx - 2] = 2
            self.posx -= 1
        #Meta, Caja-meta, Muñeco-meta
        elif self.map[self.posy][self.posx] == 5 and self.map[self.posy][self.posx - 1] == 6 and self.map[self.posy][self.posx - 2] == 4:
            self.map[self.posy][self.posx] = 4
            self.map[self.posy][self.posx - 1] = 5
            self.map[self.posy][self.posx - 2] = 6
            self.posx -=1
        #Espacio, Caja-meta, Muñeco
        elif self.map[self.posy][self.posx] == 1 and self.map[self.posy][self.posx - 1] == 6 and self.map[self.posy][self.posx - 2] == 0:
            self.map[self.posy][self.posx] = 0
            self.map[self.posy][self.posx - 1] = 5
            self.map[self.posy][self.posx - 2] = 2
            self.posx -= 1
        #Meta, Caja-meta, Muñeco
        elif self.map[self.posy][self.posx] == 1 and self.map[self.posy][self.posx - 1] == 6 and self.map[self.posy][self.posx - 2] == 4:
            self.map[self.posy][self.posx] = 0
            self.map[self.posy][self.posx - 1] = 5
            self.map[self.posy][self.posx - 2] = 6
            self.posx -= 1
