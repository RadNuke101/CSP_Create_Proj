#############################################################################################################
#                                                --2D AIM TRAINER--                                         #
#                                                                                                           #
# Author: Pranav Putta                                                                                      #
# Teacher: Mr. Millard                                                                                      #
# School: American High School                                                                              #
# Class: AP Computer Science Principlse                                                                     #
#                                                                                                           #
# Description: Practice your aim to improve gameplay in shooter games.                                      #
#              This game also serves as a way to excercise your eyes to improve health.                     #
#                                                                                                           #
#                                                                                                           #
# Functions:                                                                                                #
#           - quit() : Close the game/program                                                               #
#           - draw() : Display text in according font on the screen                                         #
#           - game_over(): Screen pops up when time runs out                                                #
#           - winner() : Screen pops up if user shoots down all the targets                                 #
#           - pause() : Screen pops up to pause the game                                                    #
#           - game() : Runs the Aim Trainer game                                                            #
#           - main_menu() : Starting menu where user can select difficulty                                  # 
#                                                                                                           #
# Inputs: Button click, Space Bar                                                                           #
#                                                                                                           #
# Outputs: Difficulty, Exit, Shoot Target, Retry, Pause                                                     #
#                                                                                                           #
#                                                                                                           #
#############################################################################################################

import pygame, sys, random
from pygame.locals import *

pygame.font.init()
pygame.init()

#Initialize Canvas/Window
CanvasW = 1000
CanvasH = 750
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
Small_Aim = pygame.transform.scale(T, (25, 25))
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
                    main_menu()
                if Buttons[1].collidepoint(pygame.mouse.get_pos()):
                    quit()
        for btn in Buttons:
            pygame.draw.rect(screen, Black, btn)
        draw("GAME OVER", screen, 300, 150, Game_OVER_TXT, Red)
        draw("Score:" + str(score), screen, 425, 250, Score_TXT, White)
        draw("Retry", screen, 350, 400, Font_TXT, Red)
        draw("Exit", screen, 350, 600, Font_TXT, White)
        pygame.display.update()

# Winner screen
def winner():
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
                    main_menu()
                if Buttons[1].collidepoint(pygame.mouse.get_pos()):
                    quit()
        for btn in Buttons:
            pygame.draw.rect(screen, Black, btn)
        draw("WINNER WINNER", screen, 250, 150, Game_OVER_TXT, Red)
        draw("CHICKEN DINNER", screen, 350, 250, Score_TXT, White)
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

#Aim Trainer code
def game(difficulty):
    MX = (CanvasW / 2)
    MY = (CanvasH / 2)
    score = 0
    counter, text = 15, "15".rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    pygame.mouse.set_visible(False)
    Targets = []
    Target_rect = []
    if difficulty == "easy":
        number_targets = 7
    if difficulty == "normal":
        number_targets = 14
    if difficulty == "hard":   
        number_targets = 21
    for x in range(number_targets):
        x = random.randrange(50, 950, 66)
        y = random.randrange(150, 700, 66)
        Targets.append((x, y))
        Target_rect.append(pygame.Rect(x,y,50,50))
    while True:
        screen.fill(Black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEMOTION:
                MX = event.pos[0]
                MY = event.pos[1]
            for i in Target_rect:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if i.collidepoint(pygame.mouse.get_pos()):   
                        score = score + 1
                        indx = Target_rect.index(i)
                        Targets.pop(indx)
                        Target_rect.pop(indx)
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
        if len(Targets) == 0:
            winner()
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
        Buttons.append(pygame.Rect(350, 250, 240, 100))
        Buttons.append(pygame.Rect(275, 350, 240, 100))
        Buttons.append(pygame.Rect(350, 450, 240, 100))        
        Buttons.append(pygame.Rect(350, 600, 240, 100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Buttons[0].collidepoint(pygame.mouse.get_pos()):
                    game("easy")
                    pause()
                if Buttons[1].collidepoint(pygame.mouse.get_pos()):
                    game("normal")
                    pause()
                if Buttons[2].collidepoint(pygame.mouse.get_pos()):
                    game("hard")
                    pause()
                if Buttons[3].collidepoint(pygame.mouse.get_pos()):
                    quit()
        for btn in Buttons:
            pygame.draw.rect(screen, Black, btn)
        draw("Aim Trainer", screen, 75, 100, Font_TITLE, color1)
        draw("Easy", screen, 350, 250, Font_TXT, color2)
        draw("Normal", screen, 275, 350, Font_TXT, color2)
        draw("Hard", screen, 350, 450, Font_TXT, color2)
        draw("Exit", screen, 350, 600, Font_TXT, color1)
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


    





