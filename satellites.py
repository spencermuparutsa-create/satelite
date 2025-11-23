import pgzrun
import random
from time import time

WIDTH = 700
HEIGHT = 600

sate = []
next = 0
line = []

start = time()

for i in range(10):
    satelite = Actor("satellite")
    satelite.x = random.randint(0,700)
    satelite.y = random.randint(0,600)
    sate.append(satelite)


def draw():
    global total
    screen.blit("background", (0,0))
    numb = 1
    for i in sate:
        i.draw()
        screen.draw.text(str(numb),(i.x, i.y - 25))
        numb = numb + 1
    for e in line:
        screen.draw.line(e[0],e[1],"white")
    if next <10:
        total = time() - start
        screen.draw.text(str(round (total, 2)), (50,50))
    else:
        screen.draw.text(str(round (total, 2)), (50,50))

def on_mouse_down(pos):
    global next, line
    if sate [next].collidepoint(pos):
        if next >0:
            line.append((sate[next - 1].pos,sate[next].pos))
        next = next + 1

    else:
        line = []
        next = 0

def update():
    pass






pgzrun.go()