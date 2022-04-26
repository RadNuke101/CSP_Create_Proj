#############################################################################################################
#                                                --AIM TRAINER--                                            #
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
# Inputs: Button click, Space Bar, Q key, R key                                                             #
#                                                                                                           #
# Outputs: Difficulty, Exit, Shoot Target, Retry, Pause                                                     #
#                                                                                                           #
# Sources:                                                                                                  #
#         - https://github.com/pzet123/aim-Trainer                                                          #
#         - https://stackoverflow.com/questions/30720665/countdown-timer-in-pygame                          #
#         - https://www.youtube.com/watch?v=sDL7P2Jhlh8                                                     #
#                                                                                                           #
#############################################################################################################

#Import modules into code
import pygame, sys, random
from pygame.locals import *

#Initialize pygame modules
pygame.init()

#Initialize Canvas/Window
CanvasW = 1000
CanvasH = 750
screen = pygame.display.set_mode((CanvasW,CanvasH))

#Initialize Colors
Black = (0,0,0)
Red = (255,0,0)
White = (255,255,255)

#Initialize Fonts
Font_TXT = pygame.font.Font("Fonts/Blazed.ttf", 75)
Font_TITLE = pygame.font.Font("Fonts/Blazed.ttf", 100)
Game_TXT = pygame.font.Font("Fonts/raidercrusader.ttf", 75)
Pause_TXT = pygame.font.Font("Fonts/raidercrusader.ttf", 150)
Game_Over_TXT = pygame.font.Font("Fonts/raidercrusader.ttf", 75)
Score_TXT = pygame.font.Font("Fonts/raidercrusader.ttf", 50)

#Initialize Caption
pygame.display.set_caption("Aim Trainer")

#Initialize Icon
I = pygame.image.load("Images/Icon.jpg")
pygame.display.set_icon(I)

#Initialize Images
T = pygame.image.load("Images/Target.png")
Aim_Target = pygame.transform.scale(T, (50, 50))
Aim = pygame.image.load("Images/Aim.png")
Aim_Scope = pygame.transform.scale(Aim, (500,500))

#Quit game
def quit():
    pygame.quit()
    sys.exit()

#Display text on screen
def draw(txt, surface, x, y, font, color):
    txtObject = font.render(txt, 1, color)
    txtRect = txtObject.get_rect()
    txtRect.topleft = (x,y)
    surface.blit(txtObject, txtRect)

#Game over screen
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Buttons[0].collidepoint(pygame.mouse.get_pos()):
                    main_menu()
                if Buttons[1].collidepoint(pygame.mouse.get_pos()):
                    quit()
        for btn in Buttons:
            pygame.draw.rect(screen, Black, btn)
        draw("GAME OVER", screen, 300, 150, Game_Over_TXT, Red)
        draw("Score:" + str(score), screen, 425, 250, Score_TXT, White)
        draw("Retry", screen, 350, 400, Font_TXT, Red)
        draw("Exit", screen, 350, 600, Font_TXT, White)
        pygame.display.update()

#Winner screen
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Buttons[0].collidepoint(pygame.mouse.get_pos()):
                    main_menu()
                if Buttons[1].collidepoint(pygame.mouse.get_pos()):
                    quit()
        for btn in Buttons:
            pygame.draw.rect(screen, Black, btn)
        draw("WINNER WINNER", screen, 250, 150, Game_Over_TXT, Red)
        draw("CHICKEN DINNER", screen, 335, 250, Score_TXT, White)
        draw("Retry", screen, 350, 400, Font_TXT, Red)
        draw("Exit", screen, 365, 600, Font_TXT, White)
        pygame.display.update()

#Pause screen
def pause():
    halt = True
    while halt:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quit()
                if event.key == pygame.K_r:
                    main_menu()
                if event.key == pygame.K_SPACE:
                    halt = False
        screen.fill(White)
        draw("Paused", screen, 250, 100, Pause_TXT, Red)
        draw("Press Space to Resume", screen, 120, 350, Game_TXT, Black)
        draw("Press R to Restart", screen, 175, 450, Game_TXT, Black)
        draw("Press Q to Quit", screen, 200, 550, Game_TXT, Black)
        pygame.display.update()

#Aim Trainer game code
def game(difficulty):
    MX = (CanvasW / 2)
    MY = (CanvasH / 2)
    score = 0
    counter, text = 15, "15".rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    pygame.mouse.set_visible(False)
    Targets = []
    Target_rect = []
    if difficulty == "e":
        number_targets = 7
    if difficulty == "n":
        number_targets = 14
    if difficulty == "h":   
        number_targets = 21
    for x in range(number_targets):
        x = random.randrange(50, 950, 66)
        y = random.randrange(150, 700, 66)
        Targets.append((x, y))
        Target_rect.append(pygame.Rect(x, y, 50, 50))
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

#Main Menu screen
def main_menu():
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Buttons[0].collidepoint(pygame.mouse.get_pos()):
                    game("e")
                    pause()
                if Buttons[1].collidepoint(pygame.mouse.get_pos()):
                    game("n")
                    pause()
                if Buttons[2].collidepoint(pygame.mouse.get_pos()):
                    game("h")
                    pause()
                if Buttons[3].collidepoint(pygame.mouse.get_pos()):
                    quit()
        for btn in Buttons:
            pygame.draw.rect(screen, Black, btn)
        draw("Aim Trainer", screen, 75, 100, Font_TITLE, Red)
        draw("Easy", screen, 350, 250, Font_TXT, White)
        draw("Normal", screen, 275, 350, Font_TXT, White)
        draw("Hard", screen, 350, 450, Font_TXT, White)
        draw("Exit", screen, 350, 600, Font_TXT, Red)
        pygame.display.update()

main_menu()