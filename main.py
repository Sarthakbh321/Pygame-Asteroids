import pygame
import os

WIDTH, HEIGHT = 900, 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroids vs.")

WHITE = (255, 255, 255)

FPS = 60

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 45

RIGHT_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
RIGHT_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RIGHT_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_WIDTH)), -90)
LEFT_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
LEFT_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(LEFT_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

def draw_graphics():
    WIN.fill(WHITE)
    WIN.blit(LEFT_SPACESHIP, (300, 100))
    WIN.blit(RIGHT_SPACESHIP, (350, 100))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()

    run = True

    while(run):

        clock.tick(FPS)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False

        draw_graphics()

    pygame.quit()


if __name__ == '__main__':
    main()