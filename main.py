import pygame
import asyncio
import random
from pacman import pacman
from ghost import ghost

pygame.init()

# screen width and height
WIDTH, HEIGHT = 600, 600
# 20x20 grid
GRID_WIDTH = 20
GRID_HEIGHT = 20
# cell size = 30
CELL_SIZE = WIDTH//GRID_WIDTH
# CELL_WIDTH_SIZE = WIDTH//GRID_WIDTH
# CELL_HEIGHT_SIZE = HEIGHT//GRID_HEIGHT
RADIUS = CELL_SIZE//2
COIN_SIZE = 6
ENERGIZER_SIZE = 10
FPS = 60
# has to be divisible with cell size (30 % 2 = 0)
SPEED = 2

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pacman')


clock = pygame.time.Clock()

# walls
# can produce array with walldrawing.py which can give list of boxes clicked
walls = [(3, 4), (2, 5), (1, 6), (1, 7), (1, 8), (2, 7), (3, 7), (4, 7), (4, 5), (5, 6), (5, 7), (5, 8), (7, 6), (7, 7), (8, 8), (9, 8), (8, 4), (9, 4), (7, 5), (10, 4), (10, 8), (13, 4), (13, 5), (13, 6), (13, 8), (13, 7), (17, 4), (18, 4), (18, 5), (14, 4), (15, 5), (16, 5), (18, 6), (18, 7), (18, 8)]

PX, PY = 0, 0
pacman = pacman(PX, PY, SPEED, RADIUS, screen, walls, CELL_SIZE, GRID_WIDTH, GRID_HEIGHT)
GX1, GY1 = 5, 0
GX2, GY2 = 10, 0
GX3, GY3 = 15, 0
GX4, GY4 = 19, 0
GXY = [[5, 0], [10, 0], [15, 0], [19, 0]]
ghosts = []
ghosts.append(ghost(GXY[0][0], GXY[0][1], SPEED, RADIUS, walls, screen, CELL_SIZE, GRID_WIDTH, GRID_HEIGHT))
ghosts.append(ghost(GXY[1][0], GXY[1][1], SPEED, RADIUS, walls, screen, CELL_SIZE, GRID_WIDTH, GRID_HEIGHT))
ghosts.append(ghost(GXY[2][0], GXY[2][1], SPEED, RADIUS, walls, screen, CELL_SIZE, GRID_WIDTH, GRID_HEIGHT))
ghosts.append(ghost(GXY[3][0], GXY[3][1], SPEED, RADIUS, walls, screen, CELL_SIZE, GRID_WIDTH, GRID_HEIGHT))

coins = []
noofcoins = 0
for i in range(GRID_HEIGHT):
    for j in range(GRID_WIDTH):
        if [j, i] == [PX, PY]:
            continue
        if [j, i] in GXY:
            continue
        if (j, i) in walls:
            continue
        coins.append([j, i])
        noofcoins += 1

score = 0
boosted = False
boost_time = 0

energizers = [[0, 19], [19, 19], [4, 9], [15, 9]]
for [x, y] in energizers:
    coins.remove([x, y])
    noofcoins -= 1


def check_food():
    global score, noofcoins
    if [pacman.x, pacman.y] in coins:
        coins.remove([pacman.x, pacman.y])
        score += 10
        noofcoins -= 1
    elif [pacman.x, pacman.y] in energizers:
        energizers.remove([pacman.x, pacman.y])
        boost()


def check_dead():
    for ghost in ghosts:
        if (pacman.x == ghost.x) and (pacman.y == ghost.y):
            return True
    return False


def boost():
    global boost_time, boosted
    boosted = True
    pacman.speed = 3
    # boost time = 20 secs
    boost_time = 20*FPS


def unboost():
    global boost_time, boosted
    boosted = False
    pacman.speed = 2
    boost_time = 0


async def main():

    not_dead = True
    while not_dead:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                not_dead = False
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP) or (event.key == pygame.K_w):
                    pacman.up()
                elif (event.key == pygame.K_DOWN) or (event.key == pygame.K_s):
                    pacman.down()
                elif (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):
                    pacman.left()
                elif (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
                    pacman.right()

        # grid
        screen.fill(BLACK)
        for i in range(GRID_WIDTH):
            for j in range(GRID_HEIGHT):
                pygame.draw.rect(screen, BLUE, (i*CELL_SIZE, j*CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

        # walls
        for (i, j) in walls:
            pygame.draw.rect(screen, BLUE, (i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        for [x, y] in coins:
            cx = (x * CELL_SIZE) + ((CELL_SIZE // 2) - (COIN_SIZE // 2))
            cy = (y * CELL_SIZE) + ((CELL_SIZE // 2) - (COIN_SIZE // 2))
            pygame.draw.rect(screen, WHITE, (cx, cy, COIN_SIZE, COIN_SIZE))

        for [x, y] in energizers:
            cx = (x * CELL_SIZE) + ((CELL_SIZE // 2) - (ENERGIZER_SIZE // 2))
            cy = (y * CELL_SIZE) + ((CELL_SIZE // 2) - (ENERGIZER_SIZE // 2))
            pygame.draw.rect(screen, WHITE, (cx, cy, ENERGIZER_SIZE, ENERGIZER_SIZE))

        pacman.update()
        for ghost in ghosts:
            ghost.update()
        print('pacman x', pacman.x)
        print('pacman y', pacman.y)

        if boosted:
            global boost_time
            boost_time -= 1
            if boost_time == 0:
                unboost()

        check_food()
        if noofcoins == 0:
            not_dead = False

        if not boosted:
            if check_dead():
                not_dead = False

        pygame.display.update()
        await asyncio.sleep(0)

    print('game over')
    print('score: ', score)
    pygame.quit()

asyncio.run(main())
