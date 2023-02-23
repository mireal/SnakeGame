import pygame
from game_logic import EventHandler
from config import WIN_SIZE, GAME_SPEED, FPS,SIDE, BACKGROUND_COLOR_1, BACKGROUND_COLOR_2, CELL
from menu import GameMenu

pygame.init()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, GAME_SPEED)

game_window = pygame.display.set_mode((WIN_SIZE, WIN_SIZE))
clock = pygame.time.Clock()

font = pygame.font.SysFont('comicsansms', 40)

events = EventHandler(game_window, SCREEN_UPDATE)
menu = GameMenu(game_window, font, SCREEN_UPDATE)


def draw_background():
    for y in range(SIDE):
        if y % 2 == 0:
            for x in range(SIDE):
                if x % 2 == 0:
                    color = BACKGROUND_COLOR_1
                else:
                    color = BACKGROUND_COLOR_2
                pygame.draw.rect(game_window, color, (x * CELL, y * CELL, CELL, CELL))
        else:
            for x in range(SIDE):
                if x % 2 != 0:
                    color = BACKGROUND_COLOR_1
                else:
                    color = BACKGROUND_COLOR_2
                pygame.draw.rect(game_window, color, (x * CELL, y * CELL, CELL, CELL))

def main():
    while True:
        game_window.fill(BACKGROUND_COLOR_1)
        draw_background()
        clock.tick(FPS)
        if menu.game_state == 'menu':
            menu.main_menu()
        else:
            events.update()


if __name__ == '__main__':
    main()
