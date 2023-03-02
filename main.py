import pygame
from game_logic import EventHandler
from config import WIN_SIZE, GAME_SPEED, FPS, BACKGROUND_COLOR_1
from menu import Menu

pygame.init()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, GAME_SPEED)

game_window = pygame.display.set_mode((WIN_SIZE, WIN_SIZE))
clock = pygame.time.Clock()

events = EventHandler(game_window, SCREEN_UPDATE)
menu = Menu(game_window, SCREEN_UPDATE)


def main():
    while True:
        game_window.fill(BACKGROUND_COLOR_1)
        menu.draw_background()
        clock.tick(FPS)
        if menu.game_state == 'menu':
            menu.menu_loop()
        elif menu.game_state == 'game':
            events.update()
        pygame.display.flip()


if __name__ == '__main__':
    main()
