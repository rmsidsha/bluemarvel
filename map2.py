import pygame as py
import sys
import random
import math
from time import sleep

BLACK = (0,0,0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

display_width = 1600
display_height = 900

lend_width = 80
lend_height = 150
lend_start_x1 = 362
lend_start_x2 = 1088
lend_start_y1 = 12
lend_start_y2 = 738


x = lend_start_x2
y = lend_start_y2


def drawMap():
    global screen
    # 모서리
    py.draw.rect(screen, WHITE,(lend_start_x1, lend_start_y1, lend_height, lend_height))
    py.draw.rect(screen, WHITE,(lend_start_x2, lend_start_y1, lend_height, lend_height))
    py.draw.rect(screen, WHITE,(lend_start_x2, lend_start_y2, lend_height, lend_height))
    py.draw.rect(screen, WHITE,(lend_start_x1, lend_start_y2, lend_height, lend_height))

    for a in range(7):
        b = 514
        c = 164
    # 윗줄
        py.draw.rect(screen, RED,(b+a*(lend_width+2), lend_start_y1, lend_width , lend_height))
    # 오른쪽 줄
        py.draw.rect(screen, BLUE, (lend_start_x2, c+a*(lend_width+2), lend_height, lend_width))
     # 밑 줄
        py.draw.rect(screen, RED, (b+a*(lend_width+2), lend_start_y2, lend_width, lend_height))
    # 왼쪽 줄
        py.draw.rect(screen, BLUE, (lend_start_x1, c+a*(lend_width+2), lend_height, lend_width))

def drawObject(obj, x, y):
    global screen
    screen.blit(obj, (x,y))

def rollDices(int):
    global diceImage, dice
    for a in range(2):
        b = 110
        dice = py.image.load(diceImage[int-1])
        dice = py.transform.scale(dice, (100, 100))
        drawObject(dice, a*b+x*0.65, y*0.5)


def initGame():
    global screen, clock, captain, hulk, buttonRoll1, buttonRoll2, diceImage, x, y
    py.init()
    screen = py.display.set_mode((display_width, display_height))
    py.display.set_caption('BlueMarvel')
    captain = py.image.load('captain.png')
    hulk = py.image.load('hulk.png')
    buttonRoll1 = py.image.load('button1.png')
    buttonRoll2 = py.image.load('button2.png')
    # dice1 = py.image.load()
    diceImage = ['dice (1).png', 'dice (2).png','dice (3).png','dice (4).png','dice (5).png','dice (6).png' ]
    clock = py.time.Clock()

def runGame():
    global screen, clock, captain, hulk, buttonRoll1, buttonRoll2, x, y

    # character size
    characterSize = captain.get_rect().size
    characterWidth = characterSize[0]
    characterHeigth = characterSize[1]

    # Roll button size
    buttonRollSize = buttonRoll1.get_rect().size
    buttonRollWidth = buttonRollSize[0]
    buttonRollHeight = buttonRollSize[1]

    # character location
    captainX = lend_start_x2
    captainY = lend_start_y2
    hulkX = lend_start_x2
    hulkY = lend_start_y2

    # charcter location list
    captainXY = [[captainX, captainY]]
    hulkXY = []

    clickRoll = True
    roll = py.Rect(x*0.65, y*0.8, 190, 88)

    onGame = False
    while not onGame:
        for event in py.event.get():
            if event.type in [py.QUIT]:  # pygame 종료와 관련된 처리를 할 경우
                py.quit()
                sys.exit()
            if event.type == py.MOUSEBUTTONDOWN:
                print(event.pos)
                mouse_location = event.pos
                if roll.collidepoint(mouse_location):
                    clickRoll = False
                    print("click")
            if event.type == py.MOUSEBUTTONUP:
                clickRoll = True
                moveA = random.randint(1, 6)
                rollDices(moveA)
                moveB = random.randint(1, 6)
                rollDices(moveB)
                captainX = 80*(moveA+moveB)
                captainXY.append([captainX, captainY])
                del captainXY[0]
                print("up")
        if clickRoll==True:
            drawObject(buttonRoll2, x*0.65, y*0.8)
        else:
            drawObject(buttonRoll1, x*0.65, y*0.8)

        screen.fill(BLACK)
        drawMap()
        if len(captainXY) !=0:
            for captainX, captainY in captainXY:
                drawObject(captain, captainX, captainY)
        drawObject(hulk, hulkX, hulkY)
        py.display.update()
        clock.tick(60)
    py.quit()

initGame()
runGame()
