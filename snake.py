import pygame
import random


pygame.init()  # initializes the pygame engine
# --- initialize variables  ------------
WIDTH = 800
HEIGHT = 600
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))

RED = (255, 0, 0)
GREEN =(0, 255, 0)
BLUE =( 0, 0,255 )
CYAN =(0, 255, 255)
WHITE =(255, 255, 255)
BLACK =(0, 0, 0)
GREY = (128, 128, 128)

# the MAIN program begins here
#pygame.event.pump()
pygame.display.set_caption("Snake Game")
gameWindow.fill(WHITE)

CENTREX = WIDTH/2
CENTREY = HEIGHT /2

#apple

#apple = pygame.image.load("apple.png").convert(gameWindow)
#apple = pygame.transform.scale(apple, (10,10))


#snake 
firstxpos = WIDTH//2
firstypos = HEIGHT//2


changedir=""
dir = "right"
score=0
snakeheadx=100
snakeheady=50
body= [[100,50],[90, 50],[80, 50],[70, 50]]

applepos = (0,0)
running = True
while running: 
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
    if event.type== pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        changedir = "up"
        print("UP")
      if event.key == pygame.K_DOWN:
        changedir = "down"
        print("down")
        snakeheady+=10
      if event.key==pygame.K_LEFT:
        changedir = "left"
        print("left")
      if event.key ==pygame.K_RIGHT:
        changedir = "right"
        print("right")
      #snake cannot go opposite directions
  
  if changedir == "up" and dir!="down":
    dir = 'up'
  if changedir == 'down' and dir!= 'up':
   dir = 'down'
  if changedir=="left" and dir!="right":
    dir= 'left'
  if changedir =="right" and dir!="left":
    dir = 'right'
  #changing directions
  if dir == 'up':
    snakeheady -=10
  if dir =='down':
    snakeheady +=10        
  if dir =='left':
    snakeheadx-=10
  if dir =='right':
    snakeheadx+=10
  #snake moving
  body.insert(0,[snakeheadx,snakeheady])
  if snakeheadx==applepos[0] and snakeheady==applepos[1]:
    #ADD SCORE
    hi=0
    #delete fruit
  else:
    body.pop()
  gameWindow.fill(WHITE)                
  for pos in body:
    pygame.draw.rect(gameWindow, GREEN, pygame.Rect(
      pos[0], pos[1], 10, 10))
    
    
  pygame.display.update() 
  pygame.time.delay(50) 

pygame.quit()

#pygame.quit()  # must put in quit, so you don't get an NO-responding window


