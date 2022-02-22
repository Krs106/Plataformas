#!/usr/bin/python3
# Se importan las bibliotecas necesarias ----------------------------------------------- #
import pygame, sys
import random

# Se configura la ventada ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
black =(0,0,0)
pygame.display.set_caption('Sudoku')
screen = pygame.display.set_mode((500, 500), 0, 32)

font = pygame.font.SysFont("Comic Sans MS", 40)
fondo = pygame.image.load("fondo.jpg").convert()


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False

#funciones de mission
def main_menu():
    while True:
        
        # Se crean el fondo, el titulo Menu y los botones
        screen.blit(fondo, [0,0])
        draw_text('Menu', font, (255, 255, 255), screen, 200, 20)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(125, 80, 250, 50)
        button_2 = pygame.Rect(125, 160, 250, 50)
        button_3 = pygame.Rect(125, 250, 250, 50)
        button_4 = pygame.Rect(125, 340, 250, 50) 
        button_5 = pygame.Rect(125, 430, 250, 50)

        # Se da las instrucciones para que se importen los programas respectivos al presionar cada boton
        if button_1.collidepoint((mx, my)):
            button1_sound = pygame.mixer.Sound("button-6.wav")
            button1_sound.set_volume(0.2)
            button1_sound.play()
            if click:
                import facil
        if button_2.collidepoint((mx, my)):
            button2_sound = pygame.mixer.Sound("button-8.wav")
            button2_sound.set_volume(0.2)
            button2_sound.play()
            if click:
                import intermedio
        if button_3.collidepoint((mx, my)):
            button3_sound = pygame.mixer.Sound("button-09a.wav")
            button3_sound.set_volume(0.2)
            button3_sound.play()
            if click:
                import dificil

        if button_4.collidepoint((mx, my)):
            button4_sound = pygame.mixer.Sound("button-09a.wav")
            button4_sound.set_volume(0.2)
            button4_sound.play()
            if click:
                    import Registro1

        if button_5.collidepoint((mx, my)):
            button5_sound = pygame.mixer.Sound("button-6.wav")
            button5_sound.set_volume(0.2)
            button5_sound.play()
            if click:
                import Instru

        # Se dibujan los botones
        pygame.draw.rect(screen, (121, 168, 217), button_1)
        facil = font.render("Facil", True, (255,255,255))
        screen.blit(facil, (210,90))
        pygame.draw.rect(screen, (121, 168, 217), button_2)
        intermedio = font.render("Intermedio", True, (255, 255, 255))
        screen.blit(intermedio, (175, 170))
        pygame.draw.rect(screen, (121, 168, 217), button_3)
        dificil = font.render("Dificil", True, (255, 255, 255))
        screen.blit(dificil, (210, 260))
        pygame.draw.rect(screen, (121, 168, 217), button_4)
        Registro = font.render("Registro", True, (255, 255, 255)) #donde aparece la palabra
        screen.blit(Registro, (200, 350)) #Aqui
        pygame.draw.rect(screen, (121, 168, 217), button_5)
        Instru1 = font.render("Instrucciones", True, (255,255,255))
        screen.blit(Instru1, (150,435))


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
