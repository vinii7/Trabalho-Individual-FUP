# Aluno: Vinicius de Oliveira Costa
# Matricula: 515129


# Importar modulos
import turtle
import math
import pygame
from turtle import *
from random import randint
from time import sleep

# Tela
display = turtle.Screen()
display.title('Turtle.io')
display.bgcolor('white')
display.setup(500, 500)
display.tracer(0)

# Score e HP
letra = turtle.Turtle()
letra.speed(0)
letra.color('black')
letra.penup()
letra.hideturtle()
letra.goto(-230, 222)
letra.write('Score: 0      HP: 3', align='left',
            font=('Early GameBoy', 18, 'normal'))

# Background
register_shape('Background.gif')
background = turtle.Turtle()
background.shape('Background.gif')
background.goto(-1, -1)

# Borda
borda = turtle.Turtle()
borda.color('black')
borda.speed(0)
borda.hideturtle()
borda.penup()
borda.setpos(-230, -230)
borda.pendown()
borda.pensize(3)
for lado in range(4):
    borda.fd(455)
    borda.lt(90)


# Tartaruga
tartaruga = turtle.Turtle()
tartaruga.speed(0)
tartaruga.color('dark green')
tartaruga.shape('turtle')
tartaruga.penup()
tartaruga.shapesize(stretch_wid=2.5, stretch_len=2.5)

# Alga
ponto = 0
alga = turtle.Turtle()
register_shape('Alga.gif')
alga.shape('Alga.gif')
alga.penup()
alga.speed(0)
alga.goto(randint(-190, 190), randint(-190, 190))


# Garrafa
vida = 3
garrafa = turtle.Turtle()
register_shape('Garrafa.gif')
garrafa.shape('Garrafa.gif')
garrafa.penup()
garrafa.speed(0)
garrafa.goto(randint(-200, 200), randint(-160, 160))


# Funções de movimento


def f():
    tartaruga.fd(20)


def b():
    tartaruga.bk(20)


def r():
    tartaruga.right(15)


def l():
    tartaruga.left(15)


# Definindo movimento/tecla
listen()
onkeypress(f, 'Up')
onkeypress(b, 'Down')
onkeypress(r, 'Right')
onkeypress(l, 'Left')

# Função colisão


def colisão(t1, t2):
    distancia = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) +
                          math.pow(t1.ycor()-t2.ycor(), 2))
    if distancia < 50:
        return True
    else:
        return False


# Musica
pygame.init()
pygame.mixer.music.load('AQUATIC AMBIENCE.wav')
pygame.mixer.music.play(-1)

# Sons
som_ponto = pygame.mixer.Sound('1+UP.wav')
som_vida = pygame.mixer.Sound('POWERDOWN.wav')

# Loop Principal do jogo
while True:
    if vida == 0:

        # Stop Musica background
        pygame.mixer.music.stop()

        # Game over
        gameover = turtle.Turtle()
        letra.speed(0)
        letra.color('white')
        letra.penup()
        letra.hideturtle()
        letra.goto(5, -40)
        letra.write('GAMEOVER', align='center',
                    font=('Early GameBoy', 40, 'normal'))

        # Musica Game over
        pygame.mixer.music.load('GAMEOVER.wav')
        pygame.mixer.music.play()

        # Tempo e sair
        sleep(4)
        exit()
    # Fronteira
    if tartaruga.ycor() > 205:
        tartaruga.sety(205)

    if tartaruga.ycor() < -210:
        tartaruga.sety(-210)

    if tartaruga.xcor() > 205:
        tartaruga.setx(205)

    if tartaruga.xcor() < -210:
        tartaruga.setx(-210)

    # Colisão Alga
    if colisão(tartaruga, alga):
        alga.setposition(randint(-190, 190), randint(-190, 190))
        ponto += 1
        som_ponto.play()
        letra.clear()
        letra.write(f'Score: {ponto}      HP: {vida}', align='left',
                    font=('Early GameBoy', 18, 'normal'))

    # Colisão Garrafa
    if colisão(tartaruga, garrafa):
        garrafa.setposition(randint(-200, 200), randint(-160, 160))
        vida -= 1
        som_vida.play()
        letra.clear()
        letra.write(f'Score: {ponto}      HP: {vida}', align='left',
                    font=('Early GameBoy', 18, 'normal'))

    display.update()
