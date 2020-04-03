import pygame
import math
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
EnemyImg = []
EnemyX = []
EnemyY = []
EnemyX_Change = []
EnemyY_Change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    EnemyImg.append(pygame.image.load('Alien.png'))
    EnemyX.append(random.randint(0, 735))
    EnemyY.append(random.randint(50, 150))
    EnemyX_Change.append(2)
    EnemyY_Change.append(40)


def enemy(x, y, i):
    screen.blit(EnemyImg[i], (x, y))

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

# Concept of Collision Detection
# We take away the distance between bullet and target, and If the distance is short enough, we say it has hit.

def isCollision(EnemyX, EnemyY, BulletX, BulletY):
    Distance = math.sqrt((math.pow(EnemyX[i] - BulletX, 2)) + (math.pow(EnemyY[i] - BulletY, 2)))
    if Distance < 27:
        return True
    else:
        return False


score = 0


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
    for i in range(num_of_enemies):
        EnemyX[i] += EnemyX_Change[i]
# Checking Boundaries Enemy
        if EnemyX[i] <= 0:
            EnemyX_Change[i] = 4
            EnemyY[i] += EnemyY_Change[i]
        elif EnemyX[i] >= 736:
            EnemyX_Change[i] = -4
            EnemyY[i] += EnemyY_Change[i]

        # Collision True or False
        collision = isCollision(EnemyX, EnemyY, BulletX, BulletY)
        if collision:
            BulletY = 480
            Bullet_State = "Ready"
            score += 1
            print(score)
            EnemyX.append(random.randint(0, 735)) #add a new one
            EnemyY.append(random.randint(50, 150))
            # remove the old enemy
             EnemyX.remove(EnemyX[i])
            EnemyY.remove(EnemyY[i])

        enemy(EnemyX[i], EnemyY[i], i)
    # Bullet Movement
    if BulletY <= 0:
        BulletY = 480
        Bullet_State = "Ready"

    if Bullet_State is "Fire":
        Fire_Bullet(BulletX, BulletY)
        BulletY -= BulletY_Change


    player(PlayerX, PlayerY)
    pygame.display.update() #An event is anything that happens inside the game window or screen.
print("Hello welcome to the Game")
