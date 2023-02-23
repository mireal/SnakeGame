import pygame
from pygame.math import Vector2

CELL = 30
WIN_SIZE = CELL * 10
SIDE = int(WIN_SIZE / CELL)
FPS = 60
GAME_SPEED = 200

BACKGROUND_COLOR_1 = (200, 200, 200)
BACKGROUND_COLOR_2 = (210, 210, 210)
FONT_COLOR = (0, 0, 0)
BUTTON_COLOR = (50, 50, 50)

MOVE_UP = Vector2(0, -1)
MOVE_DOWN = Vector2(0, 1)
MOVE_LEFT = Vector2(-1, 0)
MOVE_RIGHT = Vector2(1, 0)

SNAKE_HEAD = pygame.image.load('assets/snake_head.png')
SNAKE_TAIL = pygame.image.load('assets/snake_tail.png')
SNAKE_BODY = pygame.image.load('assets/snake_body.png')
SNAKE_TURN = pygame.image.load('assets/snake_turn.png')
