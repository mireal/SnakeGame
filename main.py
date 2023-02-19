import pygame
from pygame.math import Vector2

from random import randint

pygame.init()

CELL = 20
WIDTH = CELL * 20
HEIGHT = CELL * 20
FPS = 60
GAME_SPEED = 150

BACKGROUND = (200, 200, 200)
SNAKE_COLOR = (100, 100, 200)
FRUIT_COLOR = (200, 100, 100)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, GAME_SPEED)

game_window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()


class Snake:
    def __init__(self):
        self.body = [Vector2(6, 5), Vector2(5, 5), Vector2(4, 5)]
        self.direction = Vector2(1, 0)
        self.grow = False

    def draw_snake(self):
        for block in self.body:
            block_rect = pygame.Rect(block.x * CELL, block.y * CELL, CELL, CELL)
            pygame.draw.rect(game_window, SNAKE_COLOR, block_rect)

    def move_snake(self):
        if self.grow == True:
            body_split = self.body[:]
            body_split.insert(0, body_split[0] + self.direction)
            self.body = body_split[:]
            self.grow = False
        else:
            body_split = self.body[:-1]
            body_split.insert(0, body_split[0] + self.direction)
            self.body = body_split[:]

    def add_block(self):
        self.grow = True


class Fruit:
    def __init__(self):
        self.set_position()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * CELL, self.pos.y * CELL, CELL, CELL)
        pygame.draw.rect(game_window, FRUIT_COLOR, fruit_rect)

    def set_position(self):
        self.x = randint(0, CELL - 1)
        self.y = randint(0, CELL - 1)
        self.pos = Vector2(self.x, self.y)


class Event_handler:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        game_window.fill(BACKGROUND)
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.keyboard_input()
        self.check_collision()
        pygame.display.update()
        self.check_fail()

    def keyboard_input(self):
        for event in pygame.event.get():
            if event.type == SCREEN_UPDATE:
                self.snake.move_snake()
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snake.direction.y != 1:
                    self.snake.direction = Vector2(0, -1)
                elif event.key == pygame.K_DOWN and self.snake.direction.y != -1:
                    self.snake.direction = Vector2(0, 1)
                elif event.key == pygame.K_LEFT and self.snake.direction.x != 1:
                    self.snake.direction = Vector2(-1, 0)
                elif event.key == pygame.K_RIGHT and self.snake.direction.x != -1:
                    self.snake.direction = Vector2(1, 0)

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.snake.grow = True
            self.fruit.set_position()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < CELL or not 0 <= self.snake.body[0].y < CELL:
            self.game_over()

    def game_over(self):
        print('Game over!')
        pygame.quit()


events = Event_handler()


def main():
    while True:
        clock.tick(FPS)
        events.update()


if __name__ == '__main__':
    main()
