import pygame
import random
import sys
import os
import math
from pygame.locals import *

pygame.init()

#Initialize Canvas/Window
CanvasW = 1000
CanvasH = 1000

#Initialize Colors
Black = (0,0,0)
Red = (255,0,0)
Blue = (0,0,255)
White = (255,255,255)
Green = (0,255,0)

#Initialize Font
Font = pygame.font.SysFont("Bangers", 50)

#Initialize Images
Aim_Target = pygame.transform.scale(Images/"Target.png", (50,50))
Play_Button = pygame.transform.scale(Images/"Play.png", (100,100))
Play_Again_Button = pygame.transform.scale(Images/"Play_Again.jpg", (100,100))

def main_menu():
    while True:
        screen.fill(Black)
        difficulty = []
        difficulty.append(pygame.Rect(5,450,240,100))
        difficulty.append(pygame.Rect(255,450,240,100))
        difficulty.append(pygame.Rect(505,450,240,100))
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    Menu()
            if event.type == MOUSEBUTTONDOWN:
                if difficulty[0].collidepoint(pygame.mouse.get_pos()):
                    

