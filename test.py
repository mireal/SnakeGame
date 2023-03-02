import pygame
from pygame.math import Vector2
from config import WIN_SIZE, GAME_SPEED, FPS, SIDE, BACKGROUND_COLOR_1, BACKGROUND_COLOR_2, CELL, MOVE_UP, MOVE_LEFT, \
    MOVE_DOWN, MOVE_RIGHT, FONT_COLOR
from snake import Snake
from fruit import Fruit
from random import choice, randint

pygame.init()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, GAME_SPEED)

game_window = pygame.display.set_mode((WIN_SIZE, WIN_SIZE))
clock = pygame.time.Clock()

font = pygame.font.SysFont('pixelmix', 50)


class Menu:
    def __init__(self, screen_event, font):
        self.screen = game_window
        self.clock = clock
        self.SIDE = SIDE
        self.CELL = CELL
        self.color = BACKGROUND_COLOR_1
        self.color2 = BACKGROUND_COLOR_2
        self.screen_event = screen_event
        self.font = font
        self.font_color = FONT_COLOR

        self.snake = Snake(self.screen)
        self.fruit = Fruit(self.screen)
        self.fruit.pos = Vector2(9, 9)

        self.turn_counter = 0
        self.step_counter = 3
        self.fruit_counter = 0

    def userevent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == self.screen_event:
                self.snake_moves()
                self.check_fruit_collision()

    def draw_menu_items(self):
        item = 'start'
        start_pos = 3
        for ind, letter in enumerate(item):
            start_pos += ind
            item_text = self.font.render(letter, True, self.font_color)
            # item_rect = pygame.Rect(CELL * 3, CELL * 3, CELL * 3, CELL) # indent left, indent top, height, width
            self.screen.blit(item_text, (CELL * start_pos, CELL * 3)) # text, indent left, indent top

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
                    pygame.draw.rect(game_window, color, (x * self.CELL, y * self.CELL, self.CELL, self.CELL))
            else:
                for x in range(SIDE):
                    if x % 2 != 0:
                        color = self.color
                    else:
                        color = self.color2
                    pygame.draw.rect(game_window, color, (x * self.CELL, y * self.CELL, self.CELL, self.CELL))

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


menu = Menu(SCREEN_UPDATE, font)

while True:
    clock.tick(FPS)
    menu.draw_background()
    menu.snake.draw_snake()
    menu.fruit.draw_fruit()
    menu.userevent()
    menu.draw_menu_items()
    pygame.display.flip()
