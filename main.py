import pygame
from game_logic import EventHandler
from config import WIN_SIZE, GAME_SPEED, BACKGROUND_COLOR, FPS
from menu import GameMenu

pygame.init()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, GAME_SPEED)

game_window = pygame.display.set_mode((WIN_SIZE, WIN_SIZE))
clock = pygame.time.Clock()

font = pygame.font.SysFont('comicsansms', 40)

events = EventHandler(game_window, SCREEN_UPDATE)
menu = GameMenu(game_window, font, SCREEN_UPDATE)


def main():
    while True:
        game_window.fill(BACKGROUND_COLOR)
        clock.tick(FPS)
        if menu.game_state == 'menu':
            menu.main_menu()
        else:
            events.update()


if __name__ == '__main__':
    main()
