import random

import pygame



pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((640, 360))
running = True
background = pygame.image.load('media\w.png')
sprite = pygame.image.load('media\sprite.png')
cx = 75
cy = 25
y_change = 0
OBSTACLE_WIDTH = 70
OBSTACLE_HEIGHT = random.randint(150, 300)
OBSTACLE_COLOR = (1, 253, 1)
OBSTACE_X_CHANGE = -1
obstacle_x = 700
ob_y = 360
score = 0
score_font = pygame.font.Font('freesansbold.ttf', 16)
version =' 0.1.0'
def version_name(version):
    display = score_font.render(f"Version: {version}", True, (0,0,0))
    screen.blit(display, (10, 340))

def score_display(score):
    display = score_font.render(f"Score: {score}", True, (0,0,0))
    screen.blit(display, (10, 10))


def display_obstacle(height):
    pygame.draw.rect(screen, OBSTACLE_COLOR, (obstacle_x, 0, OBSTACLE_WIDTH, height))
    h = 360 - height - 150
    bottom_obstacle_height = h - (2*h)
    pygame.draw.rect(screen, OBSTACLE_COLOR, (obstacle_x, 360, OBSTACLE_WIDTH, bottom_obstacle_height))



def display_sprite(x,y):
    screen.blit(sprite, (cx, cy))

def collision_detection(obstacle_x, obstacle_height, sprite_y, bottom_obstacle_height):
    if obstacle_x >= 50 and obstacle_x <= (50+100):
        if sprite_y <= obstacle_height or sprite_y >=  (bottom_obstacle_height - 64):
            return True
    return False




while running:

    screen.fill((1,1,1))
    screen.blit(background, (0,0))

    collision = collision_detection(obstacle_x, OBSTACLE_HEIGHT, cy, OBSTACLE_HEIGHT + 150)

    if collision:
        score = -1

    score_display(score)
    version_name(version)


    display_sprite(cx, cy)

    cy += y_change
    if cy <= 0:
        cy = 0
    if cy >= 320 :
        cy = 320



    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            y_change = -1.5

        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            y_change = 1.5

        if event.type == pygame.QUIT:
            running = False

    obstacle_x += OBSTACE_X_CHANGE
    if obstacle_x <= -50:
        obstacle_x = 500
        OBSTACLE_HEIGHT = random.randint(50, 150)
        score += 1
    display_obstacle(OBSTACLE_HEIGHT)






    pygame.display.update()
