import pgzrun
import random
from time import time


WIDTH = 700
HEIGHT = 500

stars = []
next = 0
line = []

start = time()

for i in range(10):
    star = Actor("star")
    star.x = random.randint(0,700)
    star.y = random.randint(0,500)
    stars.append(star)

def draw():
    global total
    screen.blit("background", (0,0))
    numb = 1
    for i in stars:
        i.draw()
        screen.draw.text(str(numb), (i.x, i.y - 25) )
        numb = numb + 1
    for i in line:
        screen.draw.line(i[0],i[1], "white")
    if next <10:
        total = time() - start
        screen.draw.text(str(round (total, 1)), (50,50))
    else:
        screen.draw.text(str(round (total, 1)), (50,50))
    
    

def on_mouse_down(pos):
    global next, line
    if stars [next].collidepoint(pos):
        if next >0:
            line.append((stars[next - 1].pos, stars[next].pos))
        next = next + 1








pgzrun.go()