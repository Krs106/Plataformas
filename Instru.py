#!/usr/bin/python3

# importamos modulos
import pygame
import sys
from pygame import *
import importlib

# iniciamos los modulos
pygame.init()
pygame.font.init()
# definimos un color, un fondo, tamaño de la letra y la pantalla
black = (0, 0, 0)
font = pygame.font.SysFont("Comic Sans MS", 40)
clock = pygame.time.Clock()
screen = pygame.display.set_mode([500, 500])
fondo = pygame.image.load("sudo.JPG").convert()
base_font = pygame.font.Font(None, 27)
#Definimos en variable algunos string
user_text1 = 'Instruciones'
user_text2 = '1. Seleccione la celda con el mouse para modificar'
user_text3 = '2. Digite el número correcto a escribir en la casilla'
user_text4 = '3. Verifique con ENTER su selección'
user_text5 = '4. Presione el botón Menú para retornar al Menú'
user_text6 = '5. Clic en la X de la Ventana para abandonar'

# se difinen los Rectangulos de los bottones
input_rect = pygame.Rect(200,135,140,32)
color = pygame.Color('blue')

def Menu():

    # condiguración del pygame/window
    # define un cronómetro, título, letra, fondo
    mainClock = pygame.time.Clock()
    pygame.init()
    black =(0,0,0)
    pygame.display.set_caption('Sudoku')
    screen = pygame.display.set_mode((500, 500), 0, 32)
    font = pygame.font.SysFont("Comic Sans MS", 40)
    fondo = pygame.image.load("fondo.jpg").convert()
    # borra algun dato guardado
    importlib.invalidate_caches()

    # Configuración de dibujo y cajas
    def draw_text(text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    click = False

    # funciones de mission
    def main_menu():
        click = False
        while True:
            screen.blit(fondo, [0,0])
            # Dibuja el Menu
            draw_text('Menu', font, (255, 255, 255), screen, 200, 20)
            mx, my = pygame.mouse.get_pos()
            # establece el recuadro de los botones
            button_1 = pygame.Rect(125, 80, 250, 50)
            button_2 = pygame.Rect(125, 160, 250, 50)
            button_3 = pygame.Rect(125, 250, 250, 50)
            button_4 = pygame.Rect(125, 340, 250, 50)
            button_5 = pygame.Rect(125, 430, 250, 50)

            # Se estabecen funciones de los bottones (música)
            if button_1.collidepoint((mx, my)):
                button1_sound = pygame.mixer.Sound("button-6.wav")
                button1_sound.set_volume(0.2)
                button1_sound.play()
                # Importar al hacer click sobre botton 1
                if click:
                    import facil
                    importlib.reload(facil)
            if button_2.collidepoint((mx, my)):
                button2_sound = pygame.mixer.Sound("button-8.wav")
                button2_sound.set_volume(0.2)
                button2_sound.play()
                # Importar al hacer click sobre botton 2
                if click:
                    import intermedio
                    importlib.reload(intermedio)
            if button_3.collidepoint((mx, my)):
                button3_sound = pygame.mixer.Sound("button-09a.wav")
                button3_sound.set_volume(0.2)
                button3_sound.play()
                # Importar al hacer click sobre botton 3
                if click:
                    import dificil
                    importlib.reload(dificil)

            if button_4.collidepoint((mx, my)):
                button4_sound = pygame.mixer.Sound("button-09a.wav")
                button4_sound.set_volume(0.2)
                button4_sound.play()
                # Importar al hacer click sobre botton 4
                if click:
                    import Registro1
                    importlib.reload(Registro1)

            if button_5.collidepoint((mx, my)):
                button5_sound = pygame.mixer.Sound("button-6.wav")
                button5_sound.set_volume(0.2)
                button5_sound.play()
                # Importar al hacer click sobre botton 5
                if click:
                    import Instru
                    importlib.reload(Instru)

            # Se establece etiqueta sobre bottones y posición de la misma
            pygame.draw.rect(screen, (121, 168, 217), button_1)
            facil = font.render("Facil", True, (255, 255, 255))
            screen.blit(facil, (210, 90))
            pygame.draw.rect(screen, (121, 168, 217), button_2)
            intermedio = font.render("Intermedio", True, (255, 255, 255))
            screen.blit(intermedio, (175, 170))
            pygame.draw.rect(screen, (121, 168, 217), button_3)
            dificil = font.render("Dificil", True, (255, 255, 255))
            screen.blit(dificil, (210, 260))
            pygame.draw.rect(screen, (121, 168, 217), button_4)
            Registro = font.render("Registro", True, (255, 255, 255))
            screen.blit(Registro, (200, 350))
            pygame.draw.rect(screen, (121, 168, 217), button_5)
            Instru1 = font.render("Instrucciones", True, (255, 255, 255))
            screen.blit(Instru1, (150, 435))

            # Se establecen eventos para salir del menu
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
            # Se ordena la actualización de la pantalla Menu
            pygame.display.update()
            # Se establece tiempo de cronómetro
            mainClock.tick(60)


    # Se llama la función
    main_menu()

# Se crea un ciclo de acción para la pantalla instrucción
while True:
    menu = pygame.Rect(150, 450, 250, 50)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu.collidepoint(mouse.get_pos()):
                pygame.mixer.stop()
                Menu()
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
    # se establece la configuración de pantalla
    screen.fill((0, 0, 0))
    screen.blit(fondo, [0, 0])
    pygame.draw.rect(screen, color, input_rect, 2)
    screen.blit(fondo, [0,0])
    mx, my = pygame.mouse.get_pos()
    menu = pygame.Rect(150, 450, 250, 50)
    if menu.collidepoint(mx, my):
        draw.rect(screen, (112, 185, 230), menu, 0)
    else:
        draw.rect(screen, (111, 161, 252), menu, 0)

    # Se dibuja el botton Menu
    text = font.render("Menú", True, (255, 255, 255))
    screen.blit(text, (menu.x + (menu.width - text.get_width()) / 2,
                    menu.y + (menu.height - text.get_height()) / 2))
    # Se crea el texto de las instrucciones y su posición
    text1_surface = base_font.render(user_text1, True, (50, 50, 255))
    screen.blit(text1_surface,(80, 13))
    text2_surface = base_font.render(user_text2, True, black)
    screen.blit(text2_surface, (30, 200))
    text3_surface = base_font.render(user_text3, True, black)
    screen.blit(text3_surface, (30, 235))
    text4_surface = base_font.render(user_text4, True, black)
    screen.blit(text4_surface,(30,270))
    text5_surface = base_font.render(user_text5, True, black)
    screen.blit(text5_surface,(30,  305))
    text6_surface = base_font.render(user_text6, True, black)
    screen.blit(text6_surface, (30, 350))
    # Se ordena la actualización de la pantalla para la Instrución
    pygame.display.flip()
    # Se establece ttiempo de cronómetro
    clock.tick(60)
