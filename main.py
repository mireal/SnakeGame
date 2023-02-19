import pygame
from pygame.math import Vector2
import sys
from random import randint

pygame.init()

CELL = 30
WIDTH = CELL * 10
HEIGHT = CELL * 10
BORDER = int(WIDTH / CELL)
FPS = 60
GAME_SPEED = 200

BACKGROUND = (200, 200, 200)
SNAKE_COLOR = (100, 100, 200)
FRUIT_COLOR = (200, 100, 100)

MOVE_UP = Vector2(0, -1)
MOVE_DOWN = Vector2(0, 1)
MOVE_LEFT = Vector2(-1, 0)
MOVE_RIGHT = Vector2(1, 0)

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
        if self.grow is True:
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
        self.x = randint(0, BORDER - 1)
        self.y = randint(0, BORDER - 1)
        self.pos = Vector2(self.x, self.y)


class EventHandler:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        game_window.fill(BACKGROUND)
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.keyboard_input()
        self.check_fruit()
        pygame.display.update()
        self.check_fail()
        self.show_score()

    def keyboard_input(self):
        for event in pygame.event.get():
            if event.type == SCREEN_UPDATE:
                self.snake.move_snake()
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and not self.check_collision(MOVE_UP):
                    self.snake.direction = MOVE_UP
                elif event.key == pygame.K_DOWN and not self.check_collision(MOVE_DOWN):
                    self.snake.direction = MOVE_DOWN
                elif event.key == pygame.K_LEFT and not self.check_collision(MOVE_LEFT):
                    self.snake.direction = MOVE_LEFT
                elif event.key == pygame.K_RIGHT and not self.check_collision(MOVE_RIGHT):
                    self.snake.direction = MOVE_RIGHT

    def check_collision(self, direction):  # check for the possible collision with snake body
        nest_position = self.snake.body[0] + direction
        checked_rect = self.snake.body[1]
        return nest_position == checked_rect

    def show_score(self):
        score = len(self.snake.body)
        pygame.display.set_caption(f'Score: {score - 3}')

    def check_fruit(self):
        if self.fruit.pos == self.snake.body[0]:
            self.snake.grow = True
            self.fruit.set_position()
            while self.fruit.pos in self.snake.body:  # prevent fruit from spawning inside the snake body
                self.fruit.set_position()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < BORDER or not 0 <= self.snake.body[0].y < BORDER:
            self.game_over()
        if self.snake.body[0] in self.snake.body[1:]:
            self.game_over()

    def game_over(self):
        print('Game over!')
        pygame.quit()
        sys.exit()  # hard quit, because sometimes pygame.quit doesn't work properly


events = EventHandler()


def main():
    while True:
        clock.tick(FPS)
        events.update()


if __name__ == '__main__':
    main()
