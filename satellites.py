import pgzrun
import random

WIDTH = 700
HEIGHT = 600

satelite = Actor("satellite")

satelite.x = random.randint(0,700)
satelite.y = random.randint(0,600)


def draw():
    screen.blit("background", (0,0))
    satelite.draw()







pgzrun.go()