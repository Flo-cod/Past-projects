mport pygame
import random
import math
from pygame import mixer
pygame.init()
background = pygame.image.load("back.png")
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

mixer.music.load("background.wav")
mixer.music.play(-1)


player_img = pygame.image.load("space-invaders.png")
player_x = 370
player_y = 480
player_x_change = 0
# pygame.draw.rect(screen, (255, 0, 60), Rect=(0, 0)(200,100), width=1)
enemy_img = pygame.image.load("enemy.png")
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies= 6
for i in range(num_of_enemies):
    enemy_x.append(random.randint(-5, 741))
    enemy_y.append(random.randint(10, 150))
    enemy_x_change.append(random.randint(1, 2))
    enemy_y_change.append(40)

bullet_img = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 480
bullet_y_change = 5
bullet_state = "ready"

#score

score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10




overfont = pygame.font.Font("freesansbold.ttf", 120)

def show_score(x,y):
    score = font.render("Score: " + str(score_value), True, (235,235,235))
    screen.blit(score, (x, y))


def game_over():
    over = overfont.render("GAME OVER", True, (255, 255 , 255))
    screen.blit(over, (30, 250))



def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y,):
    screen.blit(enemy_img, (x, y))


def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x+16, y+10))


def isCollision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((math.pow(enemy_x-bullet_x, 2)) + (math.pow(enemy_y - bullet_y, 2)))
    if distance < 27:
        return True
    else:
        return False


running = True
while running:
    screen.blit(background, (0, 0))
    clock = pygame.time.Clock()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_x_change = 3
            if event.key == pygame.K_LEFT:
                player_x_change = -3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    fire_bullet(player_x,bullet_y)
                    bullet_x = player_x
                    bulletsound = mixer.Sound("laser.wav")
                    bulletsound.play()
                elif bullet_state == "fire":
                    pass
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                player_x_change = 0
    player_x += player_x_change
    if player_x < -5:
        player_x = -5
    elif player_x > 741:
        player_x = 741
    for i in range(num_of_enemies):

        if enemy_y[i] > 440:
            for j in range(num_of_enemies):
                enemy_y[j] = 2000
            game_over()
            break
        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] < -5:
            enemy_x_change[i] = 2
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] > 741:
            enemy_x_change[i] = -2
            enemy_y[i] += enemy_y_change[i]
        collision = isCollision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collision:
            collisionsound = mixer.Sound("explosion.wav")
            collisionsound.play()
            bullet_y = 480
            bullet_state = "ready"
            score_value += 1
            enemy_x[i] = random.randint(-5, 741)
            enemy_y[i] = random.randint(10, 150)
        enemy(enemy_x[i], enemy_y[i],)
    if bullet_state == "fire":
        fire_bullet(bullet_x,bullet_y)
        bullet_y -= bullet_y_change
    if bullet_y < 0:
        bullet_y = 480
        bullet_state = "ready"



    player(player_x, player_y)
    show_score(textX, textY)
    pygame.display.update()
