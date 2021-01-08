import pygame
import os

WIDTH, HEIGHT = 900, 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroids vs.")

WHITE = (255, 255, 255)

FPS = 60
VELOCITY = 5

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 45

RIGHT_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
RIGHT_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RIGHT_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_WIDTH)), -90)
LEFT_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
LEFT_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(LEFT_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

def draw_graphics(left, right):
    WIN.fill(WHITE)
    WIN.blit(LEFT_SPACESHIP, (left.x, left.y))
    WIN.blit(RIGHT_SPACESHIP, (right.x, right.y))
    pygame.display.update()

def handle_input(left, right):
    keys_pressed = pygame.key.get_pressed()

    if(keys_pressed[pygame.K_w]):
        left.y -= VELOCITY
    if(keys_pressed[pygame.K_d]):
        left.x += VELOCITY
    if (keys_pressed[pygame.K_s]):
        left.y += VELOCITY
    if (keys_pressed[pygame.K_a]):
        left.x -= VELOCITY



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


        handle_input(left, right)
        draw_graphics(left, right)

    pygame.quit()


if __name__ == '__main__':
    main()