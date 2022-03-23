import pygame
import random
import sys
import os
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

#Initialize Images
Aim_Target = pygame.transform.scale("Images/Target.png", (50,50))
Play_Button = pygame.transform.scale("Images/Play.png", (100,100))
Play_Again_Button = pygame.transform.scale("Images/Play_Again.jpg", (100,100))

#Initialize Time
Clock = pygame.time.clock()


def main_menu():
    color = Blue
    time = 0
    while True:
        screen.fill(Black)
        difficulty = []
        difficulty.append(pygame.Rect(5,450,240,100))
        difficulty.append(pygame.Rect(255,450,240,100))
        difficulty.append(pygame.Rect(505,450,240,100))
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
        for r in difficulty:
            pygame.draw.rect(screen, Red, pygame.rect)
        Txt("Difficulty", screen, 90, 150, pygame.font.SysFont("Bangers", 112), color)
        Txt("Easy", screen, 85, 485, Font, Black)
        Txt("Medium", screen, 315, 485, Font, Black)
        Txt("Hard", 580, 485, Font, Black)
        Clock.tick(50)
        time += 1
        if time % 100 == 0:
            color = Blue
        elif time % 50 == 0:
            color = Red
        pygame.display.update()

def Txt():
    pass

def game():
    pass




