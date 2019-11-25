import pygame as py

py.init()

display_width = 1600
display_height = 900

BLACK = (0,0,0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

clock = py.time.Clock()

screen = py.display.set_mode((display_width, display_height))
py.display.set_caption("브루마블")
py.display.update()

class Player:
    def __init__(self):
