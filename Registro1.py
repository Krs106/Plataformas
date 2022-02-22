#!/usr/bin/python3
import pygame as pg
import pygame
from pygame import *

pg.init()
def Menu():


    # Setup pygame/window ---------------------------------------- #
    mainClock = pygame.time.Clock()

    pygame.init()
    black =(0,0,0)
    pygame.display.set_caption('Sudoku')
    screen = pygame.display.set_mode((500, 500), 0, 32)

    font = pygame.font.SysFont("Comic Sans MS", 40)
    fondo = pygame.image.load("fondo.jpg").convert()
    importlib.invalidate_caches()


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

            button_1 = pygame.Rect(125, 80, 250, 50)
            button_2 = pygame.Rect(125, 160, 250, 50)
            button_3 = pygame.Rect(125, 250, 250, 50)
            button_4 = pygame.Rect(125, 340, 250, 50) #ubica botton
            button_5 = pygame.Rect(125, 430, 250, 50)


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
                    #sound = pygame.mixer.Sound("ELVIS.mp3")
                    #sound.play()
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
                    #sound = pygame.mixer.Sound("GNRJ.mp3")
                    #sound.play()
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

            if button_5.collidepoint((mx, my)):
                button5_sound = pygame.mixer.Sound("button-6.wav")
                button5_sound.set_volume(0.2)
                button5_sound.play()
                if click:
                    import Instru


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
def main():
    screen = pg.display.set_mode((640, 480))
    fondo = pg.image.load("NARA.JPG")
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()
    input_box = pg.Rect(230, 180, 140, 32)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    black =(0,0,0)
    red =(255,0,0)
    purple = (128,0,128)
    teal = (0,128,128)
    active = False
    text = ''
    done = False

    while not done:
        menu = pygame.Rect(150, 450, 250, 50)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        print(text)
                        text = ''
                        file = open("Prueba.txt", "w")
                        file.write(text)
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                        file = open("Prueba.txt", "w")
                        file.write(text)
                    else:
                        text += event.unicode
                        file = open("Prueba.txt", "w")
                        file.write(text)

        screen.fill((30, 30, 30))
        screen.blit(fondo, [0, 0])
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(210, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)
        # DEFINO EL TEXTO EN PANTALLA
        #Titulo
        user_text1 = 'REGISTRO'
        text1_surface = font.render(user_text1, True, (50,50,255))
        screen.blit(text1_surface,(80, 30))
        user_text6 = 'DEL'
        text6_surface = font.render(user_text6, True, (50,50,255))
        screen.blit(text6_surface,(120, 52))
        user_text7 = 'USUARIO'
        text7_surface = font.render(user_text7, True, (50,50,255))
        screen.blit(text7_surface,(80, 74))
        #Instruccion
        user_text2 = 'Digite su NICK haciendo click sobre el recuadro celeste'
        text2_surface = font.render(user_text2, True, black)
        screen.blit(text2_surface,(30,140))
        user_text8 = '<< Presione enter para registrarlo >>'
        text8_surface = font.render(user_text8, True, black)
        screen.blit(text8_surface,(130,220))
        #Para dar msj bienvenida
        user_text3 = 'Registrando: '
        text3_surface = font.render(user_text3, True, teal)
        screen.blit(text3_surface,(50,300))
        #name
        text9_surface = font.render(text, True, purple)
        screen.blit(text9_surface,(200,300))
        # Menu
        mx, my = pygame.mouse.get_pos()
        menu = pygame.Rect(150, 450, 250, 50)
        if menu.collidepoint(mx, my):
            draw.rect(screen, (112, 185, 230), menu, 0)
        else:
            draw.rect(screen, (111, 161, 252), menu, 0)
        text = font.render("Menú", True, (255, 255, 255))
        screen.blit(text, (menu.x + (menu.width - text.get_width()) / 2,
                    menu.y + (menu.height - text.get_height()) / 2))
        






        pg.display.flip()
        clock.tick(30)


main()
pg.quit()
