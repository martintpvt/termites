class Termite:

    def __init__(self, posicion=(0, 0), color="red"):
        self.posicion = posicion
        self.color = color

    def getPos(self):
        return self.posicion

    def getColor(self):
        return self.color

    def moveUp(self, interval=1):
        self.posicion = (self.posicion[0], self.posicion[1] + interval)

    def moveDown(self, interval=1):
        self.posicion = (self.posicion[0], self.posicion[1] - interval)

    def moveRight(self, interval=1):
        self.posicion = (self.posicion[0] + interval, self.posicion[1])

    def moveLeft(self, interval=1):
        self.posicion = (self.posicion[0] - interval, self.posicion[1])

    def move(self, r, limits, interval=1):
        mov = r.randint(0, 3)
        if mov == 0:
            if self.posicion[1] < limits[1]:
                self.moveUp(interval)
        elif mov == 1:
            if self.posicion[1] > limits[0]:
                self.moveDown(interval)
        elif mov == 2:
            if self.posicion[0] > limits[2]:
                self.moveLeft(interval)
        elif mov == 3:
            if self.posicion[0] < limits[3]:
                self.moveRight(interval)

    def pickChip(self, Chips, posChips):
        if self.posicion in posChips and self.color != "green":
            if Chips[posChips[self.posicion]].color != "white":
                self.color = "green"
                Chips[posChips[self.posicion]].color = "white"
                return self.posicion

    def dropChip(self, Chips, posChips):
        distancia = 1

        arriba = (self.posicion[0], self.posicion[1] + distancia)
        abajo = (self.posicion[0], self.posicion[1] - distancia)
        izquierda = (self.posicion[0] - distancia, self.posicion[1])
        derecha = (self.posicion[0] + distancia, self.posicion[1])

        if(self.color != "red"):
            if(arriba in posChips):
                if(Chips[posChips[arriba]].color != "white"):
                    # Colocar Chip en self.posicion
                    nChip = Chip(len(Chips), self.posicion)
                    self.color = "red"
                    return nChip

            if(abajo in posChips):
                if(Chips[posChips[abajo]].color != "white"):
                    # Colocar Chip en self.posicion
                    nChip = Chip(len(Chips), self.posicion)
                    self.color = "red"
                    return nChip

            if(izquierda in posChips):
                if(Chips[posChips[izquierda]].color != "white"):
                    # Colocar Chip en self.posicion
                    nChip = Chip(len(Chips), self.posicion)
                    self.color = "red"
                    return nChip

            if(derecha in posChips):
                if(Chips[posChips[derecha]].color != "white"):
                    # Colocar Chip en self.posicion
                    nChip = Chip(len(Chips), self.posicion)
                    self.color = "red"
                    return nChip


class Chip:

    def __init__(self, index, posicion=(0, 0), color="blue"):
        self.posicion = posicion
        self.color = color
        self.index = index

    def getPos(self):
        return self.posicion

    def getColor(self):
        return self.color
