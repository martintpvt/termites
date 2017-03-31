def walk(steps, interval, termites, chips):
    import turtle as t
    import random as r
    import termite as te
    from time import sleep

    t.setworldcoordinates(-600, -600, 600, 600)
    maxLimit = 40
    limits = [-maxLimit, maxLimit, -maxLimit, maxLimit]
    termList = []  # Lista de objetos termitas
    chipList = []  # Lista de objetos chips
    clist = list()  # Lista de objetos turtle para los chips
    tlist = list()  # Lista de objetos turtle para las termitas

    """
    Crea una lista de objetos turtle y objetos termite
    """
    for pi in range(termites):
        termList.append(te.Termite((r.randint(limits[0], limits[1]), r.randint(limits[2], limits[3]))))
        tlist.append(t.Turtle(shape="turtle"))  # Asigna forma circulo a cada turtle
        tlist[pi].color(termList[pi].getColor())  # Asigna color rojo a turtle
        tlist[pi].speed(0)  # Asigna la velocidad mas alta posible
        tlist[pi].shapesize(0.1, 0.15)  # Asigna el tamano de forma
        tlist[pi].penup()  # Pen up para no dejar rastro del camino
        tlist[pi].goto(termList[pi].getPos())  # Va a la posicion inicial de cada termite


    """
    Crea una lista de objetos chips y sus turtle correspondientes
    """
    for pi in range(chips):
        chipList.append(te.Chip(pi, (r.randint(limits[0], limits[1]), r.randint(limits[2], limits[3]))))
        clist.append(t.Turtle(shape="triangle"))
        clist[pi].color(chipList[pi].getColor())  # Asigna color del chip a turtle
        clist[pi].speed(0)  # Asigna la velocidad mas alta posible
        clist[pi].shapesize(0.1, 0.1)  # Asigna el tamano de forma
        clist[pi].penup()  # Pen up para no dejar rastro del camino
        clist[pi].goto(chipList[pi].getPos())  # Va a la posicion inicial de cada chip

    screen = t.getscreen()  # Obtiene la pantalla de turtle para hacer tracer

    # for i, tc in enumerate(tlist):
    #    tc.goto(termList[i].getPos())

    for ts in range(steps):
        posChips = {c.getPos(): c.index for c in chipList}
        for i, tc in enumerate(tlist):
            posT = termList[i].pickChip(chipList, posChips)
            nChip = termList[i].dropChip(chipList, posChips)
            termList[i].move(r, limits, interval)
            if posT is not None:
                ind = posChips[posT]
                clist[ind].color(chipList[ind].getColor())
                clist[ind].goto(chipList[ind].getPos())
                
            if nChip is not None:
                chipList.append(nChip)
                clist.append(t.Turtle(shape="triangle"))
                clist[nChip.index].color(chipList[nChip.index].getColor())  # Asigna color del chip a turtle
                clist[nChip.index].speed(0)  # Asigna la velocidad mas alta posible
                clist[nChip.index].shapesize(0.1, 0.1)  # Asigna el tamano de forma
                clist[nChip.index].penup()  # Pen up para no dejar rastro del camino
                clist[nChip.index].goto(chipList[nChip.index].getPos())  # Va a la posicion inicial de cada chip

            tc.color(termList[i].getColor())
            tc.goto(termList[i].getPos())

        # sleep(0.00001)
        # screen.update()
        screen.tracer(100)  # Se refrescara la pantalla cada 10 ejecuciones

    t.exitonclick()  # Al hacer clic sobre la ventana grafica se cerrara


def main(args):
    """
    Uso:
    python walkTermites.py steps interval termites chips
    Parametros:
    steps: numero de pasos
    inteval: longitud del paso
    termites: number of termites
    chips: number of chips
    Ejemplo:
    python walkTermites.py 1000 5 10 10
    """

    if len(args) == 4:
        steps = int(args[0])
        interval = int(args[1])
        termites = int(args[2])
        chips = int(args[3])
        walk(steps, interval, termites, chips)
    else:
        print (main.__doc__)


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
