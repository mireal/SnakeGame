import pygame
from pygame.math import Vector2
from config import CELL, SNAKE_COLOR


class Snake:
    def __init__(self, game_window):
        self.game_window = game_window
        self.body = [Vector2(2, 9), Vector2(1, 9), Vector2(0, 9)]
        self.direction = Vector2(1, 0)
        self.grow = False

    def draw_snake(self):
        for block in self.body:
            block_rect = pygame.Rect(block.x * CELL, block.y * CELL, CELL, CELL)
            pygame.draw.rect(self.game_window, SNAKE_COLOR, block_rect)

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
