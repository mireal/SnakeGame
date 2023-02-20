from pygame.math import Vector2

CELL = 30
WIN_SIZE = CELL * 10
SIDE = int(WIN_SIZE / CELL)
FPS = 60
GAME_SPEED = 200

BACKGROUND = (200, 200, 200)
FRUIT_COLOR = (200, 100, 100)
SNAKE_COLOR = (100, 100, 200)

MOVE_UP = Vector2(0, -1)
MOVE_DOWN = Vector2(0, 1)
MOVE_LEFT = Vector2(-1, 0)
MOVE_RIGHT = Vector2(1, 0)
