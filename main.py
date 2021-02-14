import pygame
import sys
import random
from settings import *
import tkinter as tk
from tkinter import messagebox
pygame.init()
# display
# win=pygame.display.set_mode((width,height))
# pygame.display.set_caption("PINGPONG")

# class


class Player:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        # self.num=num
        #self.rect=pygame.draw.rect(win, white, (self.x, self.y, 10,84))
        # self.over
        self.vel = 5

    def draw(self, win):
        pygame.draw.rect(win, white, (self.x, self.y, 10, 84))


class Ball:
    def __init__(self, speed):
        global win
        self.speed = speed
        self.start = False
        self.ball = pygame.draw.circle(win, white, (250, 250), 5)

    def move(self):
        if self.start:
            self.ball = self.ball.move(self.speed)
            if self.ball.top < 0 or self.ball.bottom > height:
                self.speed[1] = -self.speed[1]
            # if player1.rect.collidepoint((self.ball[0], self.ball[1])) or player2.rect.collidepoint((self.ball[0], self.ball[1])):
             #   self.speed[0] = -self.speed[0]
            if ((self.ball.right > player1.x) and (self.ball.top < player1.y+84) and (self.ball.top > player1.y)) or ((self.ball.left < player2.x+15) and (self.ball.top < player2.y+84) and (self.ball.top > player2.y)):
                self.speed[0] = -self.speed[0]
            if self.ball.right > width:
                self.start = False
                self.game_over(2)

            elif self.ball.left < 5:
                self.start = False
                self.game_over(1)

    def draw(self, win):
        self.move()
        pygame.draw.circle(win, white, (self.ball[0], self.ball[1]), 5)

    def game_over(self, n):
        message_box('PLAYER'+str(n) + 'Wins!', 'Play again...')
        reset()


# instances
player1 = Player(480, 250-42, 1)
player2 = Player(20, 250-42, 2)
negx = random.randrange(-1, 2, 2)
negy = random.randrange(-1, 2, 2)
ball = Ball([negx*3, negy*3])


def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


def reset():
    (ball.ball[0], ball.ball[1]) = (250, 250)
    player1.y = 250-42
    player2.y = 250-42


def redraw(win):
    win.fill(black)
    if not ball.start:
        text = font1.render('Press SPACE To Start', 1, red)
        win.blit(text, (50, 250))
    player1.draw(win)
    player2.draw(win)
    ball.draw(win)
    text1 = font.render('Player1', 1, white)
    text2 = font.render('Player2', 1, white)
    win.blit(text2, (20, 20))
    win.blit(text1, (400, 20))
    pygame.display.flip()


# main
clock = pygame.time.Clock()
while 1:
    clock.tick(600)
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
    # commands
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        ball.start = True
    if ball.start:
        if keys[pygame.K_UP] and player1.y > player1.vel:
            player1.y -= player1.vel
        elif keys[pygame.K_DOWN] and player1.y < width - 84 - player1.vel:
            player1.y += player1.vel
        if keys[pygame.K_w] and player2.y > player2.vel:
            player2.y -= player2.vel
        elif keys[pygame.K_s] and player2.y < width - 84 - player2.vel:
            player2.y += player2.vel

    redraw(win)


######################################## needs optimisation and sound effects #######################
