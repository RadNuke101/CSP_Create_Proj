#############################################################################################################
#                                                --AIM_TRAINER--                                            #
 
#                                             Author: Pranav Putta                                          #
 
#                                 Description: Practice your aim to improve gameplay                        #
 
#                                                                                                           #
 
#                                                                                                           #
 
#                                                                                                           #
 
#                                                                                                           #
#############################################################################################################

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


#Initialize Fonts
Font_TXT = pygame.font.Font("Fonts/Blazed.ttf", 75)
Font_TITLE = pygame.font.Font("Fonts/Blazed.ttf", 100)
Game_TXT = pygame.font.Font("Fonts/raidercrusader.ttf", 50)

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

#Quit game
def quit():
    pygame.quit()
    sys.exit()

#Draw text on screen
def draw(text, surface, x, y, font, color = Red):
    textObject = font.render(text, 1, color)
    textRect = textObject.get_rect()
    textRect.topleft = (x,y)
    surface.blit(textObject, textRect)

#Store position of mouse
mouse = pygame.mouse.get_pos()

#Aim Trainer code
def game():
    while True:
        screen.fill(Black)
        screen.blit(Aim_Target, (50, 600))
        screen.blit(Aim_Target, (400, 366))
        screen.blit(Aim_Target, (100, 200))
        screen.blit(Aim_Target, (600, 300))
        screen.blit(Aim_Target, (789, 921))
        screen.blit(Aim_Target, (425, 800))
        screen.blit(Aim_Target, (900, 400))
        screen.blit(Aim_Target, (300, 500))


#Main Menu - Exit, pause
def main_menu():
    color1 = White
    color2 = Red
    time = 0
    while True:
        Buttons = []
        screen.fill(Black)
        Buttons.append(pygame.Rect(350, 400, 240, 100))
        Buttons.append(pygame.Rect(350, 600, 240, 100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Buttons[0].collidepoint(pygame.mouse.get_pos()):
                    game()
                if Buttons[1].collidepoint(pygame.mouse.get_pos()):
                    quit()
        for btn in Buttons:
            pygame.draw.rect(screen, Black, btn)
        draw("Aim Trainer", screen, 75, 150, Font_TITLE, color1)
        draw("Start", screen, 350, 400, Font_TXT, color2)
        draw("Exit", screen, 350, 600, Font_TXT, color2)
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


#Pause Game
def pause():
    loop = 1
    draw("PAUSED", screen, 500, 150, Game_TXT, Red)
    draw("Press Space to continue", 500, 250, Game_TXT, Blue)
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop = 0
                if event.key == pygame.K_SPACE:
                    screen.fill((0, 0, 0))
                    loop = 0
        pygame.display.update()
        # screen.fill((0, 0, 0))
        Clock.tick(60)

#Change sensitivity
def sensitivity():
    pass

#Game over tab
def game_over(shots, hits, difficulty, score):
    pass

#Targets
def targets():
    enemyImg = []
    enemies_Num = 10
    for enemy in range (enemies_Num):
        enemyImg.append(pygame.image.load("Images/Target.png"))

#Score tracker
def score(x, y):
    score_val = 0
    score = Font_TXT.render("SCORE : " + str(score_val), True, (255, 255, 255))
    screen.blit(score, (x, y))

def scope(x, y):
    screen.blit("Images/Aim.png", (x, y))




    





