import pygame
import random
import sys
import os
from pygame.locals import *
import math 

pygame.font.init()
pygame.init()

#Initialize Canvas/Window
CanvasW = 1000
CanvasH = 1000
screen = pygame.display.set_mode((CanvasW,CanvasH))

#Initialize Colors
Black = (0,0,0)
Red = (255,0,0)
Blue = (0,0,255)
White = (255,255,255)
Green = (0,255,0)

#Initialize Font
font = pygame.font.Font('Lobster.ttf', 32)
txt = font.render('Aim Trainer', True, Red)
textRect = txt.get_rect()
textRect.center = (CanvasW // 2, CanvasH // 2)


#Initialize Caption
pygame.display.set_caption("Aim Trainer")

#Initialize Icon
I = pygame.image.load("Images/Icon.jpg")
pygame.display.set_icon(I)

#Initialize Images
T = pygame.image.load("Images/Target.png")
Aim_Target = pygame.transform.scale(T, (50, 50))
A = pygame.image.load("Images/Play.png")
Play_Button = pygame.transform.scale(A, (100,100))
B = pygame.image.load("Images/Play_Again.jpg")
Play_Again_Button = pygame.transform.scale(B, (100,100))

#Initialize Time
Clock = pygame.time.Clock()

#Loading Screen
def intro():
    pass

#Quit game
def quit():
    pygame.quit()
    sys.exit()

#Draw text on screen
def draw(text, surface, x, y, Font, color):
    textObject = Font.render(text, 1, color)
    textRect = textObject.get_rect()
    textRect.topleft = (x,y)
    surface.blit(textObject, textRect)


#Main Menu - Exit, pause
def main_menu():
    color1 = White
    color2 = Red
    time = 0
    while True:
        screen.fill(Black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
        
        screen.blit(txt, textRect)
        #draw("Aim Trainer", screen, 90, 150, 100, color1)
        #draw("Start", screen, 90, 300, 100, color2)
        Clock.tick(50)
        time += 1
        if time % 100 == 0:
            color1 = Red
            color2 = White
        elif time % 50 == 0:
            color1 = White
            color2 = Red
        pygame.display.update()

main_menu()

#Code for different difficulties 
def difficulty_lvl(difficulty):
    pass

#Change sensitivity
def sensitivity():
    pass

#Game over tab
def game_over(shots, hits, difficulty, score):
    pass

#Aim Trainer code
def game(difficulty):
    pass





