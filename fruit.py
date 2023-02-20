import pygame
from pygame.math import Vector2
from config import CELL, FRUIT_COLOR, SIDE
from random import randint


class Fruit:
    def __init__(self, game_window):
        self.set_position()
        self.game_window = game_window

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * CELL, self.pos.y * CELL, CELL, CELL)
        pygame.draw.rect(self.game_window, FRUIT_COLOR, fruit_rect)

    def set_position(self):
        self.x = randint(0, SIDE - 1)
        self.y = randint(0, SIDE - 1)
        self.pos = Vector2(self.x, self.y)
