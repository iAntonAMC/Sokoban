from os import system, name
import random

class Sokoban:
    map = []
    posy = 0
    posx = 0
    nivel = open("lv0.soko", "r")

    def __init__(self):
        print("Sokoban v0.2.1 Por Jesús Antonio Torres \na - Izquierda \nd - Derecha \nw - Arriba \ns - Abajo")

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
