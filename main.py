import pygame
import os

WIDTH, HEIGHT = 900, 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroids vs.")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 60
VELOCITY = 5

BORDER = pygame.Rect(WIDTH/2-10/2, 0, 10, HEIGHT)

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 45

RIGHT_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
RIGHT_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RIGHT_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_WIDTH)), -90)
LEFT_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
LEFT_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(LEFT_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

def draw_graphics(left, right):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(LEFT_SPACESHIP, (left.x, left.y))
    WIN.blit(RIGHT_SPACESHIP, (right.x, right.y))
    pygame.display.update()

def handle_input_left(keys_pressed, left):
    if(keys_pressed[pygame.K_w] and left.y > BORDER.y):
        left.y -= VELOCITY
    if(keys_pressed[pygame.K_d] and left.x < BORDER.x-SPACESHIP_WIDTH):
        left.x += VELOCITY
    if (keys_pressed[pygame.K_s] and left.y < (HEIGHT-SPACESHIP_HEIGHT)):
        left.y += VELOCITY
    if (keys_pressed[pygame.K_a] and left.x > 0):
        left.x -= VELOCITY


def handle_input_right(keys_pressed, right):
    if (keys_pressed[pygame.K_UP] and right.y > BORDER.y):
        right.y -= VELOCITY
    if (keys_pressed[pygame.K_RIGHT] and right.x < WIDTH-SPACESHIP_WIDTH):
        right.x += VELOCITY
    if (keys_pressed[pygame.K_DOWN] and right.y < (HEIGHT-SPACESHIP_HEIGHT)):
        right.y += VELOCITY
    if (keys_pressed[pygame.K_LEFT] and right.x > (BORDER.x)):
        right.x -= VELOCITY

def main():
    clock = pygame.time.Clock()

    right = pygame.Rect(700, 250, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    left = pygame.Rect(100, 250, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    run = True
    while(run):

        clock.tick(FPS)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False



        keys_pressed = pygame.key.get_pressed()
        handle_input_left(keys_pressed, left)
        handle_input_right(keys_pressed, right)
        draw_graphics(left, right)

    pygame.quit()


if __name__ == '__main__':
    main()

