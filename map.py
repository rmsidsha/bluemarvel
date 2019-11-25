import pygame as py
import sys
from pygame.locals import *
from time import sleep

py.init()

display_width = 1600
display_height = 900
card_length = 130
card_breadth = 60

screen = py.display.set_mode((display_width, display_height))
FPS = 30
fpsClock = py.time.Clock()

# 이미지 로드
champ_captain = py.image.load('captain.png')
champ_captain = py.transform.scale(champ_captain, (200, 200))
champ_hulk = py.image.load('hulk.png')
champ_hulk = py.transform.scale(champ_hulk, (200, 200))

blockl = 120
blcokh = 50
boxl = 350
boxb = 215
gapv = (display_height - 2*boxl) / 3
gaph = (display_width - display_height -2*boxb) / 3

# initialisig all the colour with the respective RGB values
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# initialising all the colour with the respective RGB values
player_index = 0
rollonce = 0
card_display = 0
endturn = 0
key = 0
place = " "
n = 0
incometax = 0
gotojail = 0
cround = [0,0]
round_complete = 0
spcard_display = 0
railway = 0
rent = 0
rolloncejail = 0
temporary = 0

gameover = 0
timerr = 8
risk = 0

lend_width = 80
lend_height = 150

__font = py.font.Font('freesansbold.ttf', 15)
clock = py.time.Clock()

# The main function
#
# def mainScreen():
#     gameExit = False
#
#     while not gameExit:
#         for event in py.event.get():
#             if event.type == py.QUIT:
#                 gameExit = True

lend_start_x1 = 362
lend_start_x2 = 1088
lend_start_y1 = 12
lend_start_y2 = 738

while True:
    screen.fill(BLACK)
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
        py.draw.rect(screen, RED,(b+a*(lend_width+2), lend_start_y2, lend_width, lend_height))
    # 왼쪽 줄
        py.draw.rect(screen, BLUE, (lend_start_x1, c+a*(lend_width+2), lend_height, lend_width))

    # 유저 창
    py.draw.rect(screen, GREEN, (50, 30, 250, 150)) # 왼쪽 유저
    py.draw.rect(screen, GREEN, (1300, 30, 250, 150)) # 오른쪽 유저

    # 버튼 위치
    py.draw.rect(screen, YELLOW, (730, 550, 160, 90))

    # 캐릭터
    screen.blit(champ_captain, (50, 700))
    screen.blit(champ_hulk, (1300, 700))

    for event in py.event.get():
        if event.type == QUIT:
            py.quit()
            sys.exit()

    py.display.update()
    fpsClock.tick(FPS)
