from pynput.keyboard import Key, Listener
from random import randint
from os import system
HEIGHT = 10
WIDTH = 10
board = ['_']*HEIGHT*WIDTH

def gameboard(board):
    for ind, x in enumerate(board):
        if (ind + 1) % 10 == 0:
            print(x)
        else:
            print(x, end='  ')

class Snake:
    def __init__(self, head = 55):
        self.board = board
        self.head = head
        self.size = 3

    def headMove(self):
        self.board[self.head] = 'O'


    def moveRight(self):
        self.board[self.head] = '_'
        self.head += 1
        self.headMove()

    def moveLeft(self):
        self.board[self.head] = '_'
        self.head -= 1
        self.headMove()

    def moveUp(self):
        self.board[self.head] = '_'
        self.head -= 10
        self.headMove()

    def moveDown(self):
        self.board[self.head] = '_'
        self.head += 10
        self.headMove()

class Tail(Snake):
    def tail_place:






snake = Snake(55)

def on_press(key):
    try:
        pressed_key = key.char
    except:
        pressed_key = None


    if pressed_key == 'w' or key == Key.up:
        snake.moveUp()

    if pressed_key == 'a' or key == Key.left:
        snake.moveLeft()

    if pressed_key == 's' or key == Key.down:
        snake.moveDown()

    if pressed_key == 'd' or key == Key.right:
        snake.moveRight()

def food(board):
    coord = randint(0,99)
    board[coord] = '@'


def on_release(key):
    if key:
        quit()

food(board)
gameboard(board)
while True:
    gameboard(board)
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    system('cls')


