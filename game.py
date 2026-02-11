import pygame
from random import randint
 
pygame.init()
screen = pygame.display.set_mode((640, 480))
 
robot = pygame.image.load("robot.png")
coin = pygame.image.load("coin.png")
door = pygame.image.load("door.png")
monster = pygame.image.load("monster.png")
 
 
x = 300
y = 400
speed = 4
 
cx = randint(0, 640 - coin.get_width())
cy = randint(0, 480 - coin.get_height())
 
dx = 320 - door.get_width() // 2
dy = 20
 
mx = randint(0, 640 - monster.get_width())
my = randint(100, 400)
mxv = randint(-2, 2)
myv = randint(-2, 2)
 
points = 0
need = 5
font = pygame.font.SysFont("Arial", 24)
clock = pygame.time.Clock()
 
game_over = False
win = False
left = False
right = False
up = False
down = False
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_RIGHT:
                right = True
            if event.key == pygame.K_UP:
                up = True
            if event.key == pygame.K_DOWN:
                down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_RIGHT:
                right = False
            if event.key == pygame.K_UP:
                up = False
            if event.key == pygame.K_DOWN:
                down = False
            
    if not game_over and not win:
        if left:
            x -= speed
        if right:
            x += speed
        if up:
            y -= speed
        if down:
            y += speed
            
 
        if x < 0:
            x = 0
        if x > 640 - robot.get_width():
            x = 640 - robot.get_width()
        if y < 0:
            y = 0
        if y > 480 - robot.get_height():
            y = 480 - robot.get_height()
 
        if x < cx + coin.get_width() and x + robot.get_width() > cx and y < cy + coin.get_height() and y + robot.get_height() > cy:
            points += 1
            cx = randint(0, 640 - coin.get_width())
            cy = randint(0, 480 - coin.get_height())
 
        mx += mxv
        my += myv
 
        if mx <= 0 or mx >= 640 - monster.get_width():
            mxv *= -1
        if my <= 0 or my >= 480 - monster.get_height():
            myv *= -1
 
        if x < mx + monster.get_width() and x + robot.get_width() > mx and y < my + monster.get_height() and y + robot.get_height() > my:
            game_over = True
 
        if points >= need:
            if x < dx + door.get_width() and x + robot.get_width() > dx and y < dy + door.get_height() and y + robot.get_height() > dy:
                win = True
 
    screen.fill((255, 255, 255))
    screen.blit(robot, (x, y))
    screen.blit(coin, (cx, cy))
    screen.blit(door, (dx, dy))
    screen.blit(monster, (mx, my))
 
    text = font.render("Coins: " + str(points) + "/5", True, (0, 0, 0))
    screen.blit(text, (10, 10))
 
    if game_over:
        screen.blit(font.render("GAME OVER", True, (255, 0, 0)), (250, 230))
 
    if win:
        screen.blit(font.render("YOU WIN", True, (0, 255, 0)), (260, 230))
 
    pygame.display.flip()
    clock.tick(60)
 