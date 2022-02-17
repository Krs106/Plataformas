#!/usr/bin/python3
# Setup Python ----------------------------------------------- #
import pygame, sys
import random
pygame.mixer.init()
# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
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


def main_menu():
    while True:

        screen.blit(fondo, [0,0])
        draw_text('Menu', font, (255, 255, 255), screen, 200, 20)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(125, 150, 250, 50)
        button_2 = pygame.Rect(125, 250, 250, 50)
        button_3 = pygame.Rect(125, 350, 250, 50)

        if button_1.collidepoint((mx, my)):
            sound = pygame.mixer.Sound("urraca.mp3")
            sound.play(0)
            if click:
                sound = pygame.mixer.Sound("5TASINFONIA.mp3")
                sound.play()
                x = random.randint(1, 3)
                if x == 1:
                    import facil1
                elif x == 2:
                    import facil2
                elif x == 3:
                    import facil3
        if button_2.collidepoint((mx, my)):
            #sound = pygame.mixer.Sound("buho.mp3")
            #sound.play(0)
            if click:
                sound = pygame.mixer.Sound("ELVIS.mp3")
                sound.play()
                x = random.randint(1,3)
                if x == 1:
                    import intermedio1
                elif x == 2:
                    import intermedio2
        if button_3.collidepoint((mx, my)):
            #sound = pygame.mixer.Sound("lobo.mp3")
            #sound.play(0)
            if click:
                sound = pygame.mixer.Sound("GNRJ.mp3")
                sound.play()
                x = random.randint(1,3)
                if x == 1:
                    import facil1
                elif x == 2:
                    import facil2
        pygame.draw.rect(screen, (121, 168, 217), button_1)
        facil = font.render("Facil", True, (255,255,255))
        screen.blit(facil, (200,145))
        pygame.draw.rect(screen, (121, 168, 217), button_2)
        intermedio = font.render("Intermedio", True, (255, 255, 255))
        screen.blit(intermedio, (150, 245))
        pygame.draw.rect(screen, (121, 168, 217), button_3)
        dificil = font.render("Dificil", True, (255, 255, 255))
        screen.blit(dificil, (200, 345))

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
