import pygame
import random

pygame.init()  # initializes the pygame engine

# --- initialize variables  ------------
WIDTH = 800
HEIGHT = 600
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)

COLORS = [GREEN, RED, BLUE, CYAN, BLACK]

# the MAIN program begins here
pygame.display.set_caption("Snake Game")
gameWindow.fill(WHITE)

CENTREX = WIDTH / 2
CENTREY = HEIGHT / 2

# snake
firstxpos = WIDTH // 2
firstypos = HEIGHT // 2

changedir = ""
dir = "right"
score = 0
snakeheadx = 100
snakeheady = 50
body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# Randomly place the apple on the screen
applepos = [random.randrange(1, WIDTH // 10) * 10, random.randrange(1, HEIGHT // 10) * 10]
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                changedir = "up"
                print("UP")
            if event.key == pygame.K_DOWN:
                changedir = "down"
                print("down")
            if event.key == pygame.K_LEFT:
                changedir = "left"
                print("left")
            if event.key == pygame.K_RIGHT:
                changedir = "right"
                print("right")

    # Direction changes
    if changedir == "up" and dir != "down":
        dir = 'up'
    if changedir == 'down' and dir != 'up':
        dir = 'down'
    if changedir == "left" and dir != "right":
        dir = 'left'
    if changedir == "right" and dir != "left":
        dir = 'right'

    # Snake movement
    if dir == 'up':
        snakeheady -= 10
    if dir == 'down':
        snakeheady += 10
    if dir == 'left':
        snakeheadx -= 10
    if dir == 'right':
        snakeheadx += 10

    body.insert(0, [snakeheadx, snakeheady])

    if snakeheadx == applepos[0] and snakeheady == applepos[1]:
        score += 1
        # Move apple to a new random position
        applepos = [random.randrange(1, WIDTH // 10) * 10, random.randrange(1, HEIGHT // 10) * 10]
    else:
        body.pop()

    # Fill screen and draw snake
    gameWindow.fill(WHITE)

    # Randomly change snake color
    snake_color = random.choice(COLORS)
    for pos in body:
        pygame.draw.rect(gameWindow, snake_color, pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw apple
    pygame.draw.rect(gameWindow, RED, pygame.Rect(applepos[0], applepos[1], 10, 10))

    pygame.display.update()
    pygame.time.delay(100)

pygame.quit()
