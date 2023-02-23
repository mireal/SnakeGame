import pygame
from pygame.math import Vector2
from config import CELL, SNAKE_HEAD, SNAKE_BODY, SNAKE_TAIL, SNAKE_TURN


class Snake:
    def __init__(self, game_window):
        self.game_window = game_window
        self.body = [Vector2(2, 9), Vector2(1, 9), Vector2(0, 9)]
        self.direction = Vector2(1, 0)
        self.grow = False

        self.head_image = pygame.transform.scale(SNAKE_HEAD, (CELL, CELL))
        self.tail_image = pygame.transform.scale(SNAKE_TAIL, (CELL, CELL))
        self.body_image = pygame.transform.scale(SNAKE_BODY, (CELL, CELL))
        self.turn_image = pygame.transform.scale(SNAKE_TURN, (CELL, CELL))

    def draw_snake(self):
        for index, block in enumerate(self.body):
            block_rect = pygame.Rect(block.x * CELL, block.y * CELL, CELL, CELL)
            if block == self.body[0]:  # draw head
                next_block = self.body[1]
                head = self.head_image
                if block.y < next_block.y:  # up
                    head = pygame.transform.rotate(head, 90)
                elif block.y > next_block.y:  # down
                    head = pygame.transform.rotate(head, -90)
                    head = pygame.transform.flip(head, True, False)
                elif block.x < next_block.x:  # left
                    head = pygame.transform.flip(head, True, False)

                self.game_window.blit(head, block_rect)

            elif block == self.body[-1]:  # draw tail
                prev_block = self.body[-2]
                tail = self.tail_image
                if block.y > prev_block.y:
                    tail = pygame.transform.rotate(tail, 90)
                elif block.y < prev_block.y:  # facing down
                    tail = pygame.transform.rotate(tail, -90)
                    tail = pygame.transform.flip(tail, True, False)  # flip to match previous sprite
                elif block.x > prev_block.x:  # facing left
                    tail = pygame.transform.flip(tail, True, False)

                self.game_window.blit(tail, block_rect)
            else:  # draw body
                prev_block = self.body[index - 1]
                next_block = self.body[index + 1]
                body = self.body_image
                turn = self.turn_image
                if block.x == prev_block.x and block.x == next_block.x:  # straight body on x line
                    body = pygame.transform.rotate(body, 90)

                    self.game_window.blit(body, block_rect)

                elif block.y == prev_block.y and block.y == next_block.y:  # straight body on y line
                    self.game_window.blit(body, block_rect)

                elif block.x != prev_block.x or block.x != next_block.x:  # check turning

                    if block.x < next_block.x or block.x < prev_block.x:  # if one block at the right
                        if block.y < next_block.y or block.y < prev_block.y:  # if block below
                            self.game_window.blit(turn, block_rect)
                        if block.y > next_block.y or block.y > prev_block.y:  # if block above
                            turn = pygame.transform.rotate(turn, 90)
                            self.game_window.blit(turn, block_rect)

                    if block.x > next_block.x or block.x > prev_block.x:  # if one block at the left
                        if block.y > next_block.y or block.y > prev_block.y:  # if block above
                            turn = pygame.transform.rotate(turn, 180)
                            self.game_window.blit(turn, block_rect)
                        if block.y < next_block.y or block.y < prev_block.y:  # if block below
                            turn = pygame.transform.rotate(turn, -90)
                            self.game_window.blit(turn, block_rect)

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
