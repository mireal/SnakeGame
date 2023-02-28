import pygame
import sys
from config import SIDE, MOVE_UP, MOVE_LEFT, MOVE_DOWN, MOVE_RIGHT
from snake import Snake
from fruit import Fruit


class EventHandler:
    def __init__(self, game_window, screen_event):
        self.game_window = game_window
        self.screen_event = screen_event
        self.snake = Snake(game_window)
        self.fruit = Fruit(game_window)

    def update(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.keyboard_input()
        self.check_fruit_collision()
        pygame.display.update()
        self.check_fail()
        self.show_score()

    def keyboard_input(self):
        for event in pygame.event.get():
            if event.type == self.screen_event:
                self.snake.move_snake()
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and not self.check_turn_collision(MOVE_UP):
                    self.snake.direction = MOVE_UP
                elif event.key == pygame.K_DOWN and not self.check_turn_collision(MOVE_DOWN):
                    self.snake.direction = MOVE_DOWN
                elif event.key == pygame.K_LEFT and not self.check_turn_collision(MOVE_LEFT):
                    self.snake.direction = MOVE_LEFT
                elif event.key == pygame.K_RIGHT and not self.check_turn_collision(MOVE_RIGHT):
                    self.snake.direction = MOVE_RIGHT

    def check_turn_collision(self, direction):  # check for the possible collision with snake body
        nest_position = self.snake.body[0] + direction
        checked_rect = self.snake.body[1]
        return nest_position == checked_rect

    def check_fruit_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.snake.grow = True
            self.fruit.set_position()
            while self.fruit.pos in self.snake.body:  # prevent fruit from spawning inside the snake body
                self.fruit.set_position()

    def show_score(self):
        score = len(self.snake.body)
        pygame.display.set_caption(f'Score: {score - 3}')

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < SIDE or not 0 <= self.snake.body[0].y < SIDE:
            self.game_over()
        if self.snake.body[0] in self.snake.body[1:]:
            self.game_over()

    def game_over(self):
        print('Game over!')
        pygame.quit()
        sys.exit()  # hard quit, because sometimes pygame.quit doesn't work properly
