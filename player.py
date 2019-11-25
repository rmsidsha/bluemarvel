import pygame as py
import functions

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

lend_width = 80
lend_height = 150
lend_start_x1 = 362
lend_start_x2 = 1088
lend_start_y1 = 12
lend_start_y2 = 738


x = lend_start_x2
y = lend_start_y2


screen = py.display.set_mode((display_width, display_height))
py.display.set_caption("브루마블")
py.display.update()

# 플레이어 객체
class Player:
    def __init__(self):
        self.cash = 1000000  # 돈 백만원
        self.posX =         # 캐릭터 x 위치
        self.posY =         # 캐릭터 y 위치
        self.total_wealth = 1000000  # 총 자산 백만원
        self.properties = []    # 건물 수
        self.no = no
        self.no_of_railways = 0
        self.released = 1   # 무인도 갔을 때
        self.color = color

    def draw(self):
        _font = py.font.Font('freesansbold.ttf', 20)
        py.draw.circle(functions.screen, self.color, [(int)(self.posX), (int)(self.posY)], 20)
        textSurface = _font.render(self.no, True, BLACK)
        textRect = textSurface.get_rect()
        textRect.center(self.posX, self.posY)
        py.display.update()

    def move(self, n):   # 캐릭터 움직임 설정
        while n > 0:
            if lend_width+lend_height / 2 < self.posX <

