import pygame
import random
import sys
import os
from pygame.locals import *
import math 

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
Font = pygame.font.SysFont("Bangers", 50)

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

#Main Menu - Can select difficulty, exit, pause
def main_menu():
    color1 = White
    color2 = Red
    time = 0
    while True:
        screen.fill(Black)
        difficulty = [] #Create a list
        difficulty.append(pygame.Rect(5,450,250,125))
        difficulty.append(pygame.Rect(255,450,250,125))
        difficulty.append(pygame.Rect(505,450,250,125))
        for event in pygame.event.get():
            if event.type == quit:
                quit()
            elif event.type == pygame.KEY_DOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if difficulty[0].collidepoint(pygame.mouse.get_pos()):
                    game("Easy")
                if difficulty[1].collidepoint(pygame.mouse.get_pos()):
                    game("Medium")
                if difficulty[2].collidepoint(pygame.mouse.get_pos()):
                    game("Hard")
        for i in difficulty:
            pygame.draw.rect(screen, Red, pygame.rect)
        Txt("Aim Trainer", screen, 90, 150, pygame.font.SysFont("Bangers", 112), color1)
        Txt("Choose a Difficulty", screen, 90, 300, pygame.font.SysFont("Bangers", 100), color2)
        Txt("Easy", screen, 85, 485, Font, Black)
        Txt("Medium", screen, 315, 485, Font, Black)
        Txt("Hard", screen, 580, 485, Font, Black)
        Clock.tick(50)
        time += 1
        if time % 100 == 0:
            color1 = Red
            color2 = White
        elif time % 50 == 0:
            color1 = White
            color2 = Red
        pygame.display.update()

#Draw text on screen
def draw(txt, surface, x, y, font = Font, color = Green):
    txtRect = Font.render(txt, 1, color).getRect()

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





