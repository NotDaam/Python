import pygame
from random import randint
pygame.init()

puntos = 0
ventana = pygame.display.set_mode((650,490))
pygame.display.set_caption("La Pelotita")
ball = pygame.image.load("Capturas/pelota.png")
ballrect = ball.get_rect()
speed = [5,5]
ballrect.move_ip(0,0)
# Crea el objeto bate, y obtengo su rectángulo
bate = pygame.image.load("Capturas/bate.png")
baterect = bate.get_rect()
# Pongo el bate en la parte inferior de la pantalla
baterect.move_ip(240,450)
fuente = pygame.font.Font(None, 50)
jugando = True

while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
    # Compruebo si se ha pulsado alguna tecla
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        baterect = baterect.move(-5,0)
    if keys[pygame.K_RIGHT]:
        baterect = baterect.move(5,0)
    if keys[pygame.K_UP]:
        baterect = baterect.move(0,-4)
    if keys[pygame.K_DOWN]:
        baterect = baterect.move(0,4)
    # Compruebo si hay colisión
    if baterect.colliderect(ballrect):
        speed[1] = -speed[1]

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speed[1] = -speed[1]
    
    #Mensaje de que ganaste cuando llegas al limite de puntos
    if ballrect.top < 0:
        puntos = puntos + 1
    if puntos == 1:
        speed = [0,0]
        texto1 = fuente.render("Limite de puntos", True, (10,10,10))
        texto1_rect = texto1.get_rect()
        texto1_x = ventana.get_width() / 2 - texto1_rect.width / 2
        texto1_y = ventana.get_height() / 2 - texto1_rect.height / 2
        ventana.blit(texto1, [texto1_x, texto1_y])
    else:
        ventana.fill((252, 243, 207))
        ventana.blit(ball, ballrect)
        ventana.blit(bate, baterect)

    #El juego termina cuando la pelota toca la parte inferior 
    if ballrect.bottom > ventana.get_height() or puntos == 1:
        speed = [0,0]
        texto2 = fuente.render("Perdiste:(", True, (10,0,0))
        texto2_rect = texto2.get_rect()
        texto2_x = ventana.get_width() / 2 - texto2_rect.width / 2
        texto2_y = ventana.get_height() / 2 - texto2_rect.height / 2
        ventana.blit(texto2, [texto2_x, texto2_y])
        #pygame.quit()
    else:
        ventana.fill((252, 243, 207))
        ventana.blit(ball, ballrect)
        ventana.blit(bate, baterect)

    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()