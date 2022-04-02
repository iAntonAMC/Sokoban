from os import system, name 

class Sokoban:
  map = [
    [3,3,3,3,3,3,3,3,3],
    [3,0,0,0,0,0,0,0,3],
    [3,0,0,0,1,0,2,4,3],
    [3,0,0,0,0,0,0,0,3],
    [3,3,3,3,3,3,3,3,3]
]

  posy = 2 #Posición muñeco en filas
  posx = 4 #Posición muñeco en columnas

  def __init__ (self):
    print ("Sokoban v0.2.1 by Jesús Antonio Torres \na - izquierda \nd - derecha \nw - arriba \ns - abajo")

  def imprimirMapa (self):
    print ("============================")  
    for fila in self.map:
      print(fila)
    print ("============================")
    print ()

  def clearsc (self):
    if name == 'nt':
      system('cls')
    else:
      system('clear')

  def teleport (self):
    if self.map[self.posy][self.posx] == 1 and self.map[self.posy - 1][self.posx + 2] == 0:
      self.map[self.posy - 1][self.posx + 2] = 1
      self.map[self.posy][self.posx] = 0
      self.posy -=1
      self.posx +=2
    elif self.map[self.posy][self.posx] == 1 and self.map[self.posy + 1][self.posx + 1] == 0:
      self.map[self.posy + 1][self.posx + 1] = 1
      self.map[self.posy][self.posx] = 0
      self.posy += 1
      self.posx += 1
    elif self.map[self.posy][self.posx] == 1 and self.map[self.posy + 2][self.posx + 2] == 0:
      self.map[self.posy + 2][self.posx + 2] = 1
      self.map[self.posy][self.posx] = 0
      self.posy += 2
      self.posx += 2
    elif self.map[self.posy][self.posx] == 1 and self.map[self.posy + 1][self.posx - 1] == 0:
      self.map[self.posy + 1][self.posx - 1] = 1
      self.map[self.posy][self.posx] = 0
      self.posy += 1
      self.posx -= 1
    elif self.map[self.posy][self.posx] == 1 and self.map[self.posy - 1][self.posx + 1] == 0:
      self.map[self.posy - 1][self.posx + 1] = 1
      self.map[self.posy][self.posx] = 0
      self.posy -= 1
      self.posx += 1
    elif self.map[self.posy][self.posx] == 1 and self.map[self.posy - 1][self.posx - 1] == 0:
      self.map[self.posy - 1][self.posx - 1] = 1
      self.map[self.posy][self.posx] = 0
      self.posy -= 1
      self.posx -= 1
    elif self.map[self.posy][self.posx] == 1 and self.map[self.posy - 2][self.posx - 3] == 0:
      self.map[self.posy - 2][self.posx - 3] = 1
      self.map[self.posy][self.posx] = 0
      self.posy -= 2
      self.posx -= 3
    elif self.map[self.posy][self.posx] == 1 and self.map[self.posy - 3][self.posx + 1] == 0:
      self.map[self.posy - 3][self.posx + 1] = 1
      self.map[self.posy][self.posx] = 0
      self.posy -= 3
      self.posx += 1
    elif self.map[self.posy][self.posx] == 1 and self.map[self.posy - 2][self.posx + 2] == 0:
      self.map[self.posy - 2][self.posx + 2] = 1
      self.map[self.posy][self.posx] = 0
      self.posy -= 2
      self.posx += 2
    elif self.map[self.posy][self.posx] == 1 and self.map[self.posy - 2][self.posx - 2] == 0:
      self.map[self.posy - 2][self.posx + 2] = 1
      self.map[self.posy][self.posx] = 0
      self.posy -= 2
      self.posx -= 2

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
    elif self.map[self.posy][self.posx] == 1 and self.map[self.posy][self.posx + 1] == 2 and self.map[self.posy + 2] == 0:
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
    elif self.map[self.posy][self.posx] ==  5 and self.map[self.posy][self.posx + 1] == 2 and self.mapa[self.posy][self.posx + 2] == 0:
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
    #Muñeco, Caja-meta, Meta
    elif self.map[self.posy][self.posx] == 1 and self.map[self.posy][self.posx + 1] == 6 and self.map[self.posy][self.posx + 2] == 4:
      self.map[self.posy][self.posx] = 0
      self.map[self.posy][self.posx + 1] = 5
      self.map[self.posy][self.posx + 2] = 6

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
    elif self.map[self.posy][self.posx] == 5 and self.map[self.posy][self.posy - 1] == 6 and self.map[self.posy][self.posx - 2] == 0:
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
    if self.map[self.posy][self.posx] == 1 and self.map[self.posy - 1][self.posx] == 0:
      self.map[self.posy][self.posx] = 0
      self.map[self.posy - 1][self.posx] = 1
      self.posy -= 1

juego = Sokoban()
juego.imprimirMapa()

while True: #Bucle para jugar N veces
  x = juego.posx
  y = juego.posy
  print("Cur position: ", "[", x, ",", y, "]")
  movimientos = input("Next move:") #Lee el movimiento del muñeco
  if movimientos == "d": #Si es d - moverá a la derecha
    juego.moverDerecha()
    juego.clearsc()
    juego.imprimirMapa()
  elif movimientos == "a": #Si es a nos moverá a la izquierda
    juego.moverIzquierda()
    juego.clearsc()
    juego.imprimirMapa()
  elif movimientos == "w": #Si entramos w nos moverá arriba
    juego.moverArriba()
    juego.clearsc()
    juego.imprimirMapa()
  elif movimientos == "t": #Se teletransporta a posibles "random"
    juego.teleport()
    juego.clearsc()
    juego.imprimirMapa()
