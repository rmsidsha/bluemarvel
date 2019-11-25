import pygame as py, sys
from pygame.locals import *

py.init()

FPS = 30
fpsClock = py.time.Clock()

#set up the window
screen = py.display.set_mode((400, 300), 0, 32)
py.display.set_caption('animation')

#set up the colors
white = (255, 255, 255)
black = (0,0,0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

image = py.image.load('ornn.jpg')
imagex = 360
imagey = 260
direction = 'left'

#text setting
font_obj = py.font.Font('freesansbold.ttf', 32)
text_surface_obj = font_obj.render('Hello World', True, green, blue)
text_rect_obj = text_surface_obj.get_rect()
#text_rectObj.center = (200, 150)

#the main game loop
while True:
    screen.fill(white)

    # draw a green polygon onto the surface
    #py.draw.polygon(screen, green, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

    # draw some blue lines onto the surface
    #py.draw.line(screen, blue, (60,60), (120, 60), 4)
    #py.draw.line(screen, blue, (120, 60), (60, 120))
    #py.draw.line(screen, blue, (60, 120), (120, 120), 4)

    # draw a blue circle onto the surface
    #py.draw.circle(screen, blue, (300, 50), 20, 0)

    # draw a red ellipse onto the surface
    #py.draw.ellipse(screen, red, (100, 150, 40, 80), 1)

    # draw a rectangle onto the surface
    py.draw.rect(screen, red, (0, 0, 100, 50))
    py.draw.rect

    # draw tge text onto the surface
    #screen.blit(text_surface_obj, text_rect_obj)

    #the animation of the image
    if direction == 'right':
        imagex += 5
        if imagex == 360:
            direction = 'down'
    elif direction == 'down':
        imagey += 5
        if imagey == 260:
            direction = 'left'
    elif direction == 'left':
        imagex -= 5
        if imagex == 20:
            direction = 'up'
    elif direction == 'up':
        imagey -= 5
        if imagey == 20:
            direction = 'right'
    screen.blit(image,(imagex, imagey))

    for event in py.event.get():
        if event.type == QUIT:
            py.quit()
            sys.exit()

    py.display.update()
    fpsClock.tick(FPS)

