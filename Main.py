import pygame
import random

# Initialise the pygame #

pygame.init()



# Create the screen / surface and its dimensions
# 800 is the Width, and 600 is the Height.
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.png')

# Title and Icon (32x32)
pygame.display.set_caption("Space Invaders!")
icon = pygame.image.load('rocket.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('Player.png')
PlayerX = 370
PlayerY = 480
PlayerX_Change = 0
PlayerY_Change = 0

def player(x, y):
    screen.blit(playerImg, (x, y)) # Blit means to draw

# Enemy Target

enemyImg = pygame.image.load('Alien.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_Change = 3
enemyY_Change = 40

def enemy(x, y):
    screen.blit(enemyImg, (x, y)) # Blit means to draw

# Bullet # Ready state means can't see the bullet on the screen, its ready to be fired. # Fire means the bullet is currently moving.
BulletImg = pygame.image.load('Bullet.png')
Bullet_State = "Ready"
BulletX = 0
BulletY = 480
BulletX_Change = 0
BulletY_Change = 10

def Fire_Bullet(x, y):
    global Bullet_State
    Bullet_State = "Fire"
    screen.blit(BulletImg, (x + 16, y + 10))

# Keeps the window open / Game Loop (Anything that must appear continuously in the game goes inside the game loop)
running = True
while running:
    screen.fill((255, 150, 0))
#Background Image
    screen.blit(background, (0, 0))
# Any keystroke on keyboard is an event and this is happening in the Game Window
# All events, clicks, keyboard strokes are stored in pygame.event.get()
# If keystroke is pressed check whether right or left

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left arrow is pressed")
                PlayerX_Change = -4
            if event.key == pygame.K_RIGHT:
                print("Right arrow is pressed")
                PlayerX_Change = 4
            if event.key == pygame.K_SPACE:
                if Bullet_State == "Ready":
                    BulletX = PlayerX
                    Fire_Bullet(PlayerX, BulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Keystroke has been released")
                PlayerX_Change = 0




# Fills background with RGB, Red, Green and Blue
    PlayerX += PlayerX_Change

# Checking Boundaries Player
    if PlayerX <= 0:
        PlayerX = 0
    elif PlayerX >= 736:
        PlayerX = 736

    enemyX += enemyX_Change
# Checking Boundaries Enemy
    if enemyX <= 0:
        enemyX_Change = 4
        enemyY += enemyY_Change
    elif enemyX >= 736:
        enemyX_Change = -4
        enemyY += enemyY_Change

    # Bullet Movement
    if BulletY <= 0:
        BulletY = 480
        Bullet_State = "Ready"

    if Bullet_State is "Fire":
        Fire_Bullet(BulletX, BulletY)
        BulletY -= BulletY_Change

    player(PlayerX, PlayerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
# An event is anything that happens inside the game window or screen.

print("Hello welcome to the Game")
