import pygame as py

# pygame 모듈 초기화
successes, failures = py.init()
print("Initializeing Pygame: {0} successes and {1} failures".format(successes, failures))

# 필수 폼 만들기

# 디스플레이 설정, 2개의 인자가 아니라 튜플임.
screen = py.display.set_mode((720, 480))
# 프로그램을 고정된 속도로 업뎃 할 수 있도록 시계를 만들어 주는 것이 좋음
# 그렇지 않으면 컴퓨터 속도에 따라 다른 속도로 실행
clock = py.time.Clock()
FPS = 60

BLACK = (0,0,0)
WHITE = (255, 255, 255)

"""
# 객체의 모양을 나타내기 위해 Surface, 위치를 나타내기 위해 Rect사용
# 첫번째 튜플: 위치  /  두번째: 크기
rect = py.Rect((0,0), (32, 32))
# 튜플: 대표사이즈
image = py.Surface((32, 32))
# Surface를 흰색으로 채우겠다. default: black
image.fill(WHITE)

while True:
    clock.tick(FPS)

# EVENT
    for event in py.event.get():
        if event.type == py.QUIT: # close 버튼 눌렀을 때 끄겠다
            # 프로그램은 닫아도 모듈은 초기화x
            quit()
        # 키를 눌렀을 때, 각각 w s a d
        elif event.type == py.KEYDOWN:
            if event.key == py.K_w:
                rect.move_ip(0, -2)
            elif event.key == py.K_s:
                rect.move_ip(0, 2)
            elif event.key == py.K_a:
                rect.move_ip(-2, 0)
            elif event.key == py.K_d:
                rect.move_ip(2, 0)

    # 화면을 검은색으로 채워서 다른 코드를 지움
    screen.fill(BLACK)
    # 다른 표면에 복사
    screen.blit(image, rect)
    py.display.update()
"""

class Player(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = py.Surface((32, 32))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.velocity = [0, 0]
    def update(self):
        self.rect.move_ip(*self.velocity)

player = Player()
running = True
while running:
    dt = clock.tick(FPS) / 1000
    screen.fill(BLACK)

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        elif event.type == py.KEYDOWN:
            if event.key == py.K_w:
                player.velocity[1] = -200 * dt  # 200 pixels per second
            elif event.key == py.K_s:
                player.velocity[1] = 200 * dt
            elif event.key == py.K_a:
                player.velocity[0] = -200 * dt
            elif event.key == py.K_d:
                player.velocity[0] = 200 * dt
            # elif event.key == py.K_SPACE:
            #     player.velocity[1] = -500 * dt
            #     player.velocity[1] = 500 d* dt

        elif event.type == py.KEYUP:
            if event.key == py.K_w or event.key == py.K_s:
                player.velocity[1] = 0
            elif event.key == py.K_a or event.key == py.K_d:
                player.velocity[0] = 0

    player.update()

    screen.blit(player.image, player.rect)
    py.display.update()

print("Exited the game loop. Game wile quit...")
quit()
