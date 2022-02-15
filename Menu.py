mport pygame

def generar_otra_pantalla():
    otra_pantalla = True
    while otra_pantalla:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                #IMPORTANTE ESTA ACCION, DE MODO QUE SI PULSAN DE NUEVO LA TECLA SE OCULTE EL MENU
                    otra_pantalla = False
                # COLOCAMOS EL COLOR DEL MENU
        screen.fill(WHITE)
        # DIBUJAMOS COSAS
        dibujar("cuadrado")
        dibujar("menu de acciones")
        # ACTUALIZAMOS EL DISPLAY CON UPDATE SE USA AQUI PARA 
        # UNICAMENTE ACTUALIZAR LA PORCION DE PANTALLA QUE ESTAMOS USANDO, NO TODO.
        # PORQUE DE LO CONTRARIO BORRARIA LO QUE ESTABA DEBAJO, 
        # DIGAMOS ERA UN MENU DE PAUSA, SI USAMOS FLIP CUANDO QUITEMOS EL MENU NO QUEDARA NADA
        pygame.display.update()

        # Y LUEGO PONEMOS EL RELOJ RAPIDO PARA QUE SEA UN RENDERIZADO PERMANENTE
        reloj_juego.tick(5)
