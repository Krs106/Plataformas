#!/usr/bin/python3
import pygame, sys
from pygame import *
from Sudoku import solve, valid


pygame.init()
pygame.font.init()
black =(0,0,0)
font = pygame.font.SysFont("Comic Sans MS", 40)
clock = pygame.time.Clock()
screen =pygame.display.set_mode([500,500])
fondo = pygame.image.load("Azul.jpeg").convert()
text2 = font.render(("Digite su nombre"), True, black)
base_font = pygame.font.Font(None,32)
user_text = ''
user_text1 = 'REGISTRO DEL USUARIO'
user_text2 = 'Digite su NICK:'
user_text3 = 'El tiempo de su intento es: '
user_text4 = 'format_time(time)'



#Rectangulo
input_rect = pygame.Rect(200,135,140,32)
color = pygame.Color('blue')

while True:
    for event in pygame.event.get():
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
    text1_surface = base_font.render(user_text1, True, (50,50,255))
    screen.blit(text1_surface,(120,13))

    text2_surface = base_font.render(user_text2, True, black)
    screen.blit(text2_surface,(30,140))


    text3_surface = base_font.render(user_text3, True, black)
    screen.blit(text3_surface,(30,190))
    #text = fnt.render(user_text3 + format_time(time), 1, (0,0,0))
    #win.blit(text, (480 -  160, 550))

    text_surface = base_font.render(user_text, True, (100,100,255))
    screen.blit(text_surface,(input_rect.x +5 ,input_rect.y +5))
    input_rect.w =max(100,text_surface.get_width()+10)




    pygame.display.flip()
    clock.tick(60)
