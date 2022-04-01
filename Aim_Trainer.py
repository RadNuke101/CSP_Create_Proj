#############################################################################################################
#                                                --AIM_TRAINER--                                            #
 
#                                             Author: Pranav Putta                                          #
 
#                                 Description: Practice your aim to improve gameplay                        #
 
#                                                                                                           #
 
#                                                                                                           #
 
#                                                                                                           #
 
#                                                                                                           #
#############################################################################################################

import pygame, random, sys, os, math, random
from pygame.locals import *

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
Game_TXT = pygame.font.Font("Fonts/raidercrusader.ttf", 75)

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
Aim = pygame.image.load("Images/Aim.png")
Aim_Scope = pygame.transform.scale(Aim, (500,500))


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

#Pause Game
def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False
        screen.fill(White)
        draw("Press Space to Resume", screen, 120, 350, Game_TXT, Red)
        pygame.display.update()

#Store position of mouse
Mice = pygame.mouse.get_pos()

#Aim Trainer code
def game():
    MX = (CanvasW / 2) #0
    MY = (CanvasH / 2) #0
    pygame.mouse.set_visible(False)
    while True:
        #screen.fill(Black)
        #screen.blit(Aim_Target, (50, 600))
        #screen.blit(Aim_Target, (400, 366))
        #screen.blit(Aim_Target, (100, 200))
        #screen.blit(Aim_Target, (600, 300))
        #screen.blit(Aim_Target, (789, 921))
        #screen.blit(Aim_Target, (425, 800))
        #screen.blit(Aim_Target, (900, 400))
        #screen.blit(Aim_Target, (300, 500))
        Targets = []
        Targets.append((50, 600))
        Targets.append((400, 366))
        Targets.append((100, 200))
        Targets.append((600, 300))
        Targets.append((789, 921))
        Targets.append((425, 800))
        Targets.append((900, 400))
        Targets.append((300, 500))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEMOTION:
                MX = event.pos[0]
                MY = event.pos[1]
            if event.type == pygame.MOUSEBUTTONDOWN:
                for x in range(0,8):
                    if Targets[x].collidepoint(pygame.mouse.get_pos()):
                        Targets.pop(x)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause()
        for t in Targets:
            screen.blit(Aim_Target, t)
        screen.blit(Aim_Scope, (MX, MY))    
        pygame.display.update()


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
                    pause()
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

main_menu()


    





