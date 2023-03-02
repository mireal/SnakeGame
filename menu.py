import pygame
from pygame.math import Vector2
from config import SIDE, BACKGROUND_COLOR_1, BACKGROUND_COLOR_2, CELL, MOVE_UP, MOVE_LEFT, MOVE_DOWN, MOVE_RIGHT, \
    START_BUTTON, SETTINGS_WINDOW
from snake import Snake
from fruit import Fruit
from random import choice, randint

pygame.init()


# font = pygame.font.SysFont('pixelmix', 50)


class Menu:
    def __init__(self, game_window, screen_event):
        self.screen = game_window
        self.SIDE = SIDE
        self.CELL = CELL
        self.color = BACKGROUND_COLOR_1
        self.color2 = BACKGROUND_COLOR_2
        self.screen_event = screen_event

        self.start_button = START_BUTTON
        self.settings_window = SETTINGS_WINDOW

        self.snake = Snake(self.screen)
        self.fruit = Fruit(self.screen)
        self.fruit.pos = Vector2(9, 9)

        self.turn_counter = 0
        self.step_counter = 3
        self.fruit_counter = 0
        self.game_state = 'menu'

    def menu_loop(self):
        # self.draw_background()
        self.snake.draw_snake()  # snake going in circles on the menu screen
        self.fruit.draw_fruit()
        self.userevent()
        self.draw_menu_items()

    def userevent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == self.screen_event:
                self.snake_moves()
                self.check_fruit_collision()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                start_button_rect = pygame.Rect(CELL * 2, CELL * 2, CELL * 6, CELL)
                if start_button_rect.collidepoint(mouse_pos):
                    self.game_state = 'game'
                    print('starting game')

    def draw_menu_items(self):
        start_button_rect = pygame.Rect(CELL * 2, CELL * 2, CELL * 6, CELL)  # indent left, indent top, height, width
        self.screen.blit(self.start_button, start_button_rect)

        settings_rect = pygame.Rect(CELL * 1, CELL * 4, CELL * 6, CELL)
        self.screen.blit(self.settings_window, settings_rect)

    def snake_moves(self):
        move_list = (MOVE_RIGHT, MOVE_UP, MOVE_LEFT, MOVE_DOWN)

        self.snake.direction = move_list[self.turn_counter]
        self.snake.move_snake()
        self.step_counter += 1

        if self.step_counter == 9:
            self.step_counter = 0
            self.turn_counter += 1
            if self.turn_counter == 4:
                self.turn_counter = 0

    def draw_background(self):
        for y in range(self.SIDE):
            if y % 2 == 0:
                for x in range(self.SIDE):
                    if x % 2 == 0:
                        color = self.color
                    else:
                        color = self.color2
                    pygame.draw.rect(self.screen, color, (x * self.CELL, y * self.CELL, self.CELL, self.CELL))
            else:
                for x in range(SIDE):
                    if x % 2 != 0:
                        color = self.color
                    else:
                        color = self.color2
                    pygame.draw.rect(self.screen, color, (x * self.CELL, y * self.CELL, self.CELL, self.CELL))

    def set_fruit_position(self):
        choice_list = [0, SIDE - 1]
        random_place = randint(0, 1)
        if random_place == 0:
            self.fruit.x = choice(choice_list)
            self.fruit.y = randint(0, 9)
        elif random_place == 1:
            self.fruit.y = choice(choice_list)
            self.fruit.x = randint(0, 9)
        self.fruit.pos = Vector2(self.fruit.x, self.fruit.y)

    def check_fruit_collision(self):
        if self.fruit_counter <= 30:
            if self.fruit.pos == self.snake.body[0]:
                self.snake.grow = True
                self.set_fruit_position()
                while self.fruit.pos in self.snake.body:  # prevent fruit from spawning inside the snake body
                    self.set_fruit_position()
                self.fruit_counter += 1
        else:
            self.fruit.pos = Vector2(7, 7)

# menu = Menu(game_window, SCREEN_UPDATE)
#
# while True:
#     clock.tick(FPS)
#     menu.menu_loop()
#     pygame.display.flip()
