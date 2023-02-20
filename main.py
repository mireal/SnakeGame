import pygame
from game_logic import EventHandler
from config import WIN_SIZE, GAME_SPEED, BACKGROUND, FPS

pygame.init()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, GAME_SPEED)

game_window = pygame.display.set_mode((WIN_SIZE, WIN_SIZE))
clock = pygame.time.Clock()

events = EventHandler(game_window, SCREEN_UPDATE)


def main():
    while True:
        game_window.fill(BACKGROUND)
        clock.tick(FPS)
        events.update()


if __name__ == '__main__':
    main()
