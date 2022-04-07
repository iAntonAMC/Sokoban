from os import system, name 
import random

class Sokoban:
  map = []
  posy = 0 #Posición muñeco en filas
  posx = 0 #Posición muñeco en columnas
 
  def __init__ (self):
    print ("Sokoban v0.2.1 Por Jesús Antonio Torres \na - Izquierda \nd - Derecha \nw - Arriba \ns - Abajo")

  def crearMapa (self):
    nivel = open("lv1.soko", "r")
    for row in nivel:
      linea = []
      for digito in row:
        if digito == "\n":
          continue
        linea.append(int(digito))
      self.map.append(linea)

  def imprimirMapa (self):
    print ("============================")  
    for fila in self.map:
      for casilla in fila:
        if casilla == 3:
          print(chr(128679), end="")
        elif casilla == 0:
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
    print ("============================")

  def clearsc (self):
    if name == 'nt':
      system('cls')
    else:
      system('clear')

  def encontrarPersonaje(self):
    for linea in self.map:
      if 1 in linea:
        self.posy = self.map.index(linea)
        self.posx = linea.index(1)
    print(self.posy)
    print(self.posx)

  def teleport (self):
    pass

  def moverDerecha (self):
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

  def moverIzquierda(self):
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

  def moverArriba(self):
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
      self.posy -=1
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

  def moverAbajo(self):
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

juego = Sokoban()
juego.crearMapa()
juego.imprimirMapa()
juego.encontrarPersonaje()

while True: #Bucle para jugar N veces
  print("Posición actual: ", "[", juego.posy, ",", juego.posx, "]")
  movimiento = input("Siguiente movimiento: ") #Lee el movimiento del muñeco
  if movimiento == "d": #Si es d - moverá a la derecha
    juego.moverDerecha()
    juego.clearsc()
    juego.imprimirMapa()
  elif movimiento == "a": #Si es a nos moverá a la izquierda
    juego.moverIzquierda()
    juego.clearsc()
    juego.imprimirMapa()
  elif movimiento == "w": #Si entramos w nos moverá arriba
    juego.moverArriba()
    juego.clearsc()
    juego.imprimirMapa()
  elif movimiento == "s": #Si pulsamo s nos moverá abajo
    juego.moverAbajo()
    juego.clearsc()
    juego.imprimirMapa()
  elif movimiento == "t": #Se teletransporta a posibles "random"
    juego.teleport()
    juego.clearsc()
    juego.imprimirMapa()
  else:
    juego.clearsc()
    print("============================")
    print ("Porfavor, verifique su entrada...")
    juego.imprimirMapa()
