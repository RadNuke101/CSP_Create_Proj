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
Game_OVER_TXT = pygame.font.Font("Fonts/raidercrusader.ttf", 75)
Score_TXT = pygame.font.Font("Fonts/raidercrusader.ttf", 50)


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


#Game over tab
def game_over(score):
    pygame.mouse.set_visible(True)
    while True:
        Buttons = []
        Buttons.append(pygame.Rect(350, 400, 240, 100))
        Buttons.append(pygame.Rect(350, 600, 240, 100))
        screen.fill(Black)
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
        draw("GAME OVER", screen, 300, 150, Game_OVER_TXT, Red)
        draw("Score:" + str(score), screen, 425, 250, Score_TXT, White)
        draw("Retry", screen, 350, 400, Font_TXT, Red)
        draw("Exit", screen, 350, 600, Font_TXT, White)
        pygame.display.update()

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
Mouse = pygame.mouse.get_pos()

#Aim Trainer code
def game():
    MX = (CanvasW / 2) #0
    MY = (CanvasH / 2) #0
    score = 0
    counter, text = 15, "15".rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    pygame.mouse.set_visible(False)
    Targets = []
    Targets.append((50, 600))
    Targets.append((400, 366))
    Targets.append((100, 200))
    Targets.append((600, 300))
    Targets.append((789, 921))
    Targets.append((425, 800))
    Targets.append((900, 400))
    Targets.append((300, 500))
    Target_rect = []
    Target_rect.append(pygame.Rect(50,600,50,50))
    Target_rect.append(pygame.Rect(400,366,50,50))
    Target_rect.append(pygame.Rect(100,200,50,50))
    Target_rect.append(pygame.Rect(600,300,50,50))
    Target_rect.append(pygame.Rect(789,921,50,50))
    Target_rect.append(pygame.Rect(425,800,50,50))
    Target_rect.append(pygame.Rect(900,400,50,50))
    Target_rect.append(pygame.Rect(300,500,50,50))
    while True:
        screen.fill(Black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEMOTION:
                MX = event.pos[0]
                MY = event.pos[1]
            if event.type == pygame.MOUSEBUTTONDOWN:
                for x in range(0, len(Target_rect)-1):
                    if Target_rect[x].collidepoint(pygame.mouse.get_pos()):   
                        score = score + 1
                        del Targets[x]
                        del Target_rect[x]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause()
            if event.type == pygame.USEREVENT:
                counter = counter - 1
                if counter > 0:
                    text = str(counter).rjust(3)
                else:
                    game_over(score)
        for r in Target_rect:
            pygame.draw.rect(screen, Black, r)
        for t in Targets:
            screen.blit(Aim_Target, t)
        #Cursor = pygame.Rect(MX, MY, 40, 40)
        #pygame.draw.rect(screen, Black, Cursor)
        draw("Score: " + str(score), screen, 50, 50, Game_TXT, Red) 
        draw("Time: " + text, screen, 650, 50, Game_TXT, Red)
        screen.blit(Aim_Scope, (MX - 230, MY - 230))
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

main_menu()


    





