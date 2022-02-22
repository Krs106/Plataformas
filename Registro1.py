#!/usr/bin/python3
import sys
import pygame as pg


def main():
    screen = pg.display.set_mode((640, 480))
    fondo = pg.image.load("NARA.JPG")
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()
    input_box = pg.Rect(230, 180, 140, 32)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    black = (0, 0, 0)
    purple = (128, 0, 128)
    teal = (0, 128, 128)
    active = False
    text = ''
    done = False

    while not done:
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


        pg.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
