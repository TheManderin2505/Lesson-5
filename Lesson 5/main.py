from random import randint
import time
import pgzrun

WIDTH = 400
HEIGHT  = 400
TITLE = 'bee game'

bee = Actor('bee')
flower = Actor('flower')

score = 0
game_over = False

bee.pos = 100,100
flower.pos = 200,200

def move_flower():
    flower.x= randint(0,400)
    flower.y=randint(0,400)

def time_1():
    global game_over
    game_over = True
clock.schedule(time_1,60.1)

def update():
    global score
    if keyboard.d:
        bee.x=bee.x+2
    if keyboard.a:
        bee.x=bee.x-2
    if keyboard.w:
        bee.y=bee.y-2
    if keyboard.s:
        bee.y=bee.y+2
    if bee.colliderect(flower):
        score = score + 20
        move_flower()


def draw():
    screen.blit("background",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("score: "+str(score),color = "black",topleft=(10,10))
    if game_over:
        screen.fill("blue")
        screen.draw.text("game over you scored: "+str(score),color = "black",topleft=(10,10))





pgzrun.go()