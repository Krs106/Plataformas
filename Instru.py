#!/usr/bin/python3
import pygame, sys
from pygame import *
import importlib

pygame.init()
pygame.font.init()
black =(0,0,0)
font = pygame.font.SysFont("Comic Sans MS", 40)
clock = pygame.time.Clock()
screen =pygame.display.set_mode([500,500])
fondo = pygame.image.load("sudo.JPG").convert()
text2 = font.render(("Digite su nombre"), True, black)
base_font = pygame.font.Font(None,27)

user_text1 = 'Instruciones'
user_text2 = '1. Seleccione la celda con el mouse para modificar'
user_text3 = '2. Digite el número correcto a escribir en la casilla'
user_text4 = '3. Verifique con ENTER su selección'
user_text5 = '4. Presione el botón Menú para retornar al Menú'
user_text6 = '5. Clic en la X de la Ventana para abandonar'




#Rectangulo
input_rect = pygame.Rect(200,135,140,32)
color = pygame.Color('blue')

while True:
    menu = pygame.Rect(150, 450, 250, 50)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu.collidepoint(mouse.get_pos()):
                pygame.mixer.stop()
                import Menu
                importlib.reload(Menu)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            elif event.key == pygame.K_KP_ENTER:
                Codigo = []
                Codigo.append(user_text)
                print(Codigo)


            else:
                user_text += event.unicode

    screen.fill((0,0,0))
    screen.blit(fondo, [0,0])
    pygame.draw.rect(screen,color,input_rect,2)
    screen.blit(fondo, [0,0])
    mx, my = pygame.mouse.get_pos()
    menu = pygame.Rect(150, 450, 250, 50)
    if menu.collidepoint(mx, my):
        draw.rect(screen, (112, 185, 230), menu, 0)
    else:
        draw.rect(screen, (111, 161, 252), menu, 0)
    text = font.render("Menú", True, (255, 255, 255))
    screen.blit(text, (menu.x + (menu.width - text.get_width()) / 2,
                    menu.y + (menu.height - text.get_height()) / 2))

    text1_surface = base_font.render(user_text1, True, (50,50,255))
    screen.blit(text1_surface,(80,13))

    text2_surface = base_font.render(user_text2, True, black)
    screen.blit(text2_surface,(30,200))

    text3_surface = base_font.render(user_text3, True, black)
    screen.blit(text3_surface,(30,235))

    text4_surface = base_font.render(user_text4, True, black)
    screen.blit(text4_surface,(30,270))

    text5_surface = base_font.render(user_text5, True, black)
    screen.blit(text5_surface,(30,305))

    text6_surface = base_font.render(user_text6, True, black)
    screen.blit(text6_surface,(30,350))







    #text5_surface = base_font.render(user_text4, True, black)
    #screen.blit(text3_surface,(30,190))






    pygame.display.flip()
    clock.tick(60)
