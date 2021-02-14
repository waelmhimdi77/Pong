import pygame
pygame.init()

#display
width=500
height=500
win=pygame.display.set_mode((width,height))
pygame.display.set_caption("PINGPONG")


# colors
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)
black=(0,0,0)
white=(255,250,250)
nokia=(178,189,8)
yellow=(255,217,15)
wood=(133,94,66)

#Fonts
font=pygame.font.SysFont('monospace',20)
font1=pygame.font.SysFont('comicsans',50,True)