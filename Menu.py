#!/usr/bin/python3
# Setup Python ----------------------------------------------- #
import pygame, sys
import random

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
black =(0,0,0)
pygame.display.set_caption('Sudoku')
screen = pygame.display.set_mode((500, 500), 0, 32)

font = pygame.font.SysFont("Comic Sans MS", 40)
fondo = pygame.image.load("fondo.jpg").convert()

#text2 = font.render(("Digite su nombre"), True, black)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False

#funciones de mission
def main_menu():
    while True:

        screen.blit(fondo, [0,0])
        #screen.blit(text2, (80, 90))
        draw_text('Menu', font, (255, 255, 255), screen, 200, 20)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(125, 140, 250, 50)
        button_2 = pygame.Rect(125, 240, 250, 50)
        button_3 = pygame.Rect(125, 340, 250, 50)
        button_4 = pygame.Rect(125, 420, 250, 50) #ubica botton

        if button_1.collidepoint((mx, my)):
            button1_sound = pygame.mixer.Sound("button-6.wav")
            button1_sound.set_volume(0.2)
            button1_sound.play()
            if click:
                #sound = pygame.mixer.Sound("5TASINFONIA.mp3")
                #sound.play()
                x = random.randint(1, 3)
                if x == 1:
                    import facil1
                elif x == 2:
                    import facil2
                elif x == 3:
                    import facil3
        if button_2.collidepoint((mx, my)):
            button2_sound = pygame.mixer.Sound("button-8.wav")
            button2_sound.set_volume(0.2)
            button2_sound.play()
            if click:
                sound = pygame.mixer.Sound("ELVIS.mp3")
                sound.play()
                x = random.randint(1, 4)
                if x == 1:
                    import intermedio1
                elif x == 2:
                    import intermedio2
                elif x == 3:
                    import intermedio3
        if button_3.collidepoint((mx, my)):
            button3_sound = pygame.mixer.Sound("button-09a.wav")
            button3_sound.set_volume(0.2)
            button3_sound.play()
            if click:
                sound = pygame.mixer.Sound("GNRJ.mp3")
                sound.play()
                x = random.randint(1,3)
                if x == 1:
                    import dificil1
                elif x == 2:
                    import dificil2

        if button_4.collidepoint((mx, my)):
            button4_sound = pygame.mixer.Sound("button-09a.wav")
            button4_sound.set_volume(0.2)
            button4_sound.play()
            if click:
                    import Registro1


        pygame.draw.rect(screen, (121, 168, 217), button_1)
        facil = font.render("Facil", True, (255,255,255))
        screen.blit(facil, (200,150))
        pygame.draw.rect(screen, (121, 168, 217), button_2)
        intermedio = font.render("Intermedio", True, (255, 255, 255))
        screen.blit(intermedio, (150, 250))
        pygame.draw.rect(screen, (121, 168, 217), button_3)
        dificil = font.render("Dificil", True, (255, 255, 255))
        screen.blit(dificil, (200, 350))
        pygame.draw.rect(screen, (121, 168, 217), button_4)
        Registro = font.render("Registro", True, (255, 255, 255)) #donde aparece la palabra
        screen.blit(Registro, (200, 430)) #Aqui


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)



main_menu()
