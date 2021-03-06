from os import system, name
import random

class Sokoban:
    map = []
    posy = 0
    posx = 0
    nivel = ()
    completo = False

    def __init__(self):
        print("Sokoban v1.1.0 Por Jesús Antonio Torres \n")

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
                elif casilla == 7:
                    print("  ", end="")
                elif casilla == 1:
                    print(chr(128125), end="")
                elif casilla == 2:
                    print(chr(127921), end= "")
                elif casilla == 3:
                    print(chr(128679), end="")
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

    def evaluarMapa(self):
        verificador = []
        for linea in self.map:
            num2 = linea.count(2)
            verificador.append(num2)
        if sum(verificador) == 0:
            self.limpiarPantalla()
            print(chr(128125), chr(128142), chr(129535), '¡¡¡FELICIDADES!!! ¡¡¡COMPLETASTE EL NIVEL!!!',chr(129535), chr(128142), chr(128125))
            self.completo = True
        else:
            pass

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

    def movArriba(self):
        #Muñeco, Espacio
        if self.map[self.posy][self.posx] == 1 and self.map[self.posy - 1][self.posx] == 0:
            self.map[self.posy][self.posx] = 0
            self.map[self.posy - 1][self.posx] = 1
            self.posy -= 1
        #Muñeco, Meta
        elif self.map[self.posy][self.posx] == 1 and self.map[self.posy - 1][self.posx] == 4:
            self.map[self.posy][self.posx] = 0
            self.map[self.posy - 1][self.posx] = 5
            self.posy -= 1
        #Muñeco, Caja, Espacio
        elif self.map[self.posy][self.posx] == 1 and self.map[self.posy - 1][self.posx] == 2 and self.map[self.posy - 2][self.posx] == 0:
            self.map[self.posy][self.posx] = 0
            self.map[self.posy - 1][self.posx] = 1
            self.map[self.posy - 2][self.posx] = 2
            self.posy -= 1
        #Muñeco, Caja, Meta
        elif self.map[self.posy][self.posx] == 1 and self.map[self.posy - 1][self.posx] == 2 and self.map[self.posy - 2][self.posx] == 4:
            self.map[self.posy][self.posx] = 0
            self.map[self.posy - 1][self.posx] = 1
            self.map[self.posy - 2][self.posx] = 6
            self.posy -= 1
        #Muñeco-meta, Espacio
        elif self.map[self.posy][self.posx] == 5 and self.map[self.posy - 1][self.posx] == 0:
            self.map[self.posy][self.posx] = 4
            self.map[self.posy - 1][self.posx] = 1
            self.posy -= 1
        #Muñeco-meta, Meta
        elif self.map[self.posy][self.posx] == 5 and self.map[self.posy - 1][self.posx] == 4:
            self.map[self.posy][self.posx] = 4
            self.map[self.posy - 1][self.posx] = 5
            self.posy -= 1
        #Muñeco-meta, Caja, Espacio
        elif self.map[self.posy][self.posx] == 5 and self.map[self.posy - 1][self.posx] == 2 and self.map[self.posy - 2][self.posx] == 0:
            self.map[self.posy][self.posx] = 4
            self.map[self.posy - 1][self.posx] = 1
            self.map[self.posy - 2][self.posx] = 2
            self.posy -= 1 
        #Muñeco-meta, Caja, Meta
        elif self.map[self.posy][self.posx] == 5 and self.map[self.posy - 1][self.posx] == 2 and self.map[self.posy - 2][self.posx] == 4:
            self.map[self.posy][self.posx] = 4
            self.map[self.posy - 1][self.posx] = 1
            self.map[self.posy - 2][self.posx] = 6
            self.posy -= 1
        #Muñeco-meta, Caja-meta, Espacio
        elif self.map[self.posy][self.posx] == 5 and self.map[self.posy - 1][self.posx] == 6 and self.map[self.posy - 2][self.posx] == 0:
            self.map[self.posy][self.posx] = 4
            self.map[self.posy - 1][self.posx] = 5
            self.map[self.posy - 2][self.posx] = 2
            self.posy -= 1
        #Muñeco-meta, Caja-meta, Meta
        elif self.map[self.posy][self.posx] == 5 and self.map[self.posy - 1][self.posx] == 6 and self.map[self.posy - 2][self.posx] == 4:
            self.map[self.posy][self.posx] = 4
            self.map[self.posy - 1][self.posx] = 5
            self.map[self.posy - 2][self.posx] = 6
            self.posy -= 1
        #Muñeco, Caja-meta, Espacio
        elif self.map[self.posy][self.posx] == 1 and self.map[self.posy - 1][self.posx] == 6 and self.map[self.posy - 2][self.posx] == 0:
            self.map[self.posy][self.posx] = 0
            self.map[self.posy - 1][self.posx] = 5
            self.map[self.posy - 2][self.posx] = 2
            self.posy -= 1
        #Muñeco, Caja-meta, Meta
        elif self.map[self.posy][self.posx] == 1 and self.map[self.posy - 1][self.posx] == 6 and self.map[self.posy - 2][self.posx] == 4:
            self.map[self.posy][self.posx] = 0
            self.map[self.posy - 1][self.posx] = 5
            self.map[self.posy - 2][self.posx] = 6
            self.posy -= 1

    def movAbajo(self):
        #Muñeco, Espacio
        if self.map[self.posy][self.posx] == 1 and self.map[self.posy + 1][self.posx] == 0:
            self.map[self.posy][self.posx] = 0
            self.map[self.posy + 1][self.posx] = 1
            self.posy += 1
        #Muñeco, Meta
        elif self.map[self.posy][self.posx] == 1 and self.map[self.posy + 1][self.posx] == 4:
            self.map[self.posy][self.posx] = 0
            self.map[self.posy + 1][self.posx] = 5
            self.posy += 1
        #Muñeco, Caja, Espacio
        elif self.map[self.posy][self.posx] == 1 and self.map[self.posy + 1][self.posx] == 2 and self.map[self.posy + 2][self.posx] == 0:
            self.map[self.posy][self.posx] = 0
            self.map[self.posy + 1][self.posx] = 1
            self.map[self.posy + 2][self.posx] = 2
            self.posy += 1
        #Muñeco, Caja, Meta
        elif self.map[self.posy][self.posx] == 1 and self.map[self.posy + 1][self.posx] == 2 and self.map[self.posy + 2][self.posx] == 4:
            self.map[self.posy][self.posx] = 0
            self.map[self.posy + 1][self.posx] = 1
            self.map[self.posy + 2][self.posx] = 6
            self.posy += 1
        #Muñeco-meta, Espacio
        elif self.map[self.posy][self.posx] == 5 and self.map[self.posy + 1][self.posx] == 0:
            self.map[self.posy][self.posx] = 4
            self.map[self.posy + 1][self.posx] = 1
            self.posy += 1
        #Muñeco-meta, Meta
        elif self.map[self.posy][self.posx] == 5 and self.map[self.posy + 1][self.posx] == 4:
            self.map[self.posy][self.posx] = 4
            self.map[self.posy + 1][self.posx] = 5
            self.posy += 1
        #Muñeco-meta, Caja, Espacio
        elif self.map[self.posy][self.posx] == 5 and self.map[self.posy + 1][self.posx] == 2 and self.map[self.posy + 2][self.posx] == 0:
            self.map[self.posy][self.posx] = 4
            self.map[self.posy + 1][self.posx] = 1
            self.map[self.posy + 2][self.posx] = 2
            self.posy +=1
        #Muñeco-meta, Caja, Meta
        elif self.map[self.posy][self.posx] == 5 and self.map[self.posy + 1][self.posx] == 2 and self.map[self.posy + 2][self.posx] == 4:
            self.map[self.posy][self.posx] = 4
            self.map[self.posy + 1][self.posx] = 1
            self.map[self.posy + 2][self.posx] = 6
            self.posy += 1
        #Muñeco-meta, Caja-meta, Espacio
        elif self.map[self.posy][self.posx] == 5 and self.map[self.posy + 1][self.posx] == 6 and self.map[self.posy + 2][self.posx] == 0:
            self.map[self.posy][self.posx] = 4
            self.map[self.posy + 1][self.posx] = 5
            self.map[self.posy + 2][self.posx] = 2
            self.posy += 1
        #Muñeco-meta, Caja-meta, Meta
        elif self.map[self.posy][self.posx] == 5 and self.map[self.posy + 1][self.posx] == 6 and self.map[self.posy + 2][self.posx] == 4:
            self.map[self.posy][self.posx] = 4
            self.map[self.posy + 1][self.posx] = 5
            self.map[self.posy + 2][self.posx] = 6
            self.posy += 1
        #Muñeco, Caja-meta, Espacio
        elif self.map[self.posy][self.posx] == 1 and self.map[self.posy + 1][self.posx] == 6 and self.map[self.posy + 2][self.posx] == 0:
            self.map[self.posy][self.posx] = 0
            self.map[self.posy + 1][self.posx] = 5
            self.map[self.posy + 2][self.posx] = 2
            self.posy += 1
        #Muñeco, Caja-meta, Meta
        elif self.map[self.posy][self.posx] == 1 and self.map[self.posy + 1][self.posx] == 6 and self.map[self.posy + 2][self.posx] == 4:
            self.map[self.posy][self.posx] = 0
            self.map[self.posy + 1][self.posx] = 5
            self.map[self.posy + 2][self.posx] = 6
            self.posy += 1

    def teleport(self):
        if self.map[self.posy][self.posx] == 1:
            teleporty = 0
            teleportx = 0
            libre = False
            while libre == False:
                teleporty = random.randint(1, len(self.map)-1)
                for linea in self.map:
                    teleportx = random.randint(1,len(linea)-1)
                if self.map[teleporty][teleportx] == 0:
                    libre = True
            self.map[self.posy][self.posx] = 0
            self.posy = teleporty
            self.posx = teleportx
            self.map[self.posy][self.posx] = 1
        elif self.map[self.posy][self.posx] == 5:
            teleporty = 0
            teleportx = 0
            libre = False
            while libre == False:
                teleporty = random.randint(1, len(self.map)-1)
                for linea in self.map:
                    teleportx = random.randint(1,len(linea)-1)
                if self.map[teleporty][teleportx] == 0:
                    libre = True
            self.map[self.posy][self.posx] = 4
            self.posy = teleporty
            self.posx = teleportx
            self.map[self.posy][self.posx] = 1

    def juegoContinuo(self):
        self.map = []
        print('=========================================')
        comienza = False
        while comienza == False:
            nuevo = input('¿Qué nivel deseas abrir ahora?\n\t[ 1 | 2 | 3 | 4 ]\n: ')
            if nuevo == '1':
                self.nivel = open("lv0.soko", "r")
                comienza = True
            elif nuevo == '2':
                self.nivel = open("lv1.soko", "r")
                comienza = True
            elif nuevo == '3':
                self.nivel = open("lv2.soko", "r")
                comienza = True
            elif nuevo == '3':
                self.nivel = open("lv2.soko", "r")
                comienza = True
            else:
                self.limpiarPantalla()
                print('Actualmente el juego no dispone del nivel seleccionado...\n')
        self.limpiarPantalla()
        self.crearMapa()
        self.encontrarSoko()
        self.imprimirMapa()
        while self.completo == False:
            print("Posición actual: ", "[", self.posy, ",", self.posx, "]")
            movimiento = input('Siguiente movimiento: ')
            if movimiento == "w":
                self.movArriba()
                self.limpiarPantalla()
                self.imprimirMapa()
                self.evaluarMapa()
            elif movimiento == 's':
                self.movAbajo()
                self.limpiarPantalla()
                self.imprimirMapa()
                self.evaluarMapa()
            elif movimiento == 'd':
                self.movDerecha()
                self.limpiarPantalla()
                self.imprimirMapa()
                self.evaluarMapa()
            elif movimiento == 'a':
                self.movIzquierda()
                self.limpiarPantalla()
                self.imprimirMapa()
                self.evaluarMapa()
            elif movimiento == 't':
                self.teleport()
                self.limpiarPantalla()
                self.imprimirMapa()
            elif movimiento == "p":
                self.map=[]
                self.limpiarPantalla()
                self.crearMapa()
                self.encontrarSoko()
                self.imprimirMapa()
            else:
                self.limpiarPantalla()
                print('Porfavor, verifica tu entrada... \n')
                self.imprimirMapa()

juego = Sokoban()
print(chr(127921), chr(128125), chr(127921), chr(128125),chr(128142), chr(128125), chr(129535), chr(128125), chr(127921), chr(128125),chr(128142), chr(128125))
print(chr(128142), ' Bienvenide a Sokoban v1.1.0 ', chr(128142))
print(chr(127921), chr(128125), chr(127921), chr(128125),chr(128142), chr(128125), chr(129535), chr(128125), chr(127921), chr(128125),chr(128142), chr(128125))
print('\nActualmente el juego cuenta con 3 niveles')
juego.juegoContinuo()
continua = input('¿Deseas continuar? \n\t[s/n]\n:')
while continua != 'n' or continua != "N" and continua == 's':
    juego.completo = False
    juego.juegoContinuo()
    continua = input('¿Deseas continuar? \n\t[s/n]\n:')

print('\nGracias por jugar a Sokoban v1.1.0\nNo olvides dejar tus comentarios en Replit: https://replit.com/@iAntonAMC/Sokoban\n\nATTE: iAntonAMC©')
