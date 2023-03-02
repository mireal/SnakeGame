import pygame

# set up pygame
pygame.init()

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# set up window and font
WIN_SIZE = (300, 300)
FONT_SIZE = 30
font = pygame.font.SysFont('arial', FONT_SIZE)
window = pygame.display.set_mode(WIN_SIZE)

# define cell size and number of cells
CELL_SIZE = 30
NUM_CELLS = 10

# calculate total window size
WIN_WIDTH = CELL_SIZE * NUM_CELLS
WIN_HEIGHT = CELL_SIZE * NUM_CELLS
WINDOW_SIZE = (WIN_WIDTH, WIN_HEIGHT)

# create rectangles for each letter
letters = ['S', 'T', 'A', 'R', 'T']
rects = []
for i in range(len(letters)):
    letter_surface = font.render(letters[i], True, BLACK)
    letter_rect = letter_surface.get_rect()
    letter_rect.x = i * CELL_SIZE
    letter_rect.y = 0
    rects.append(letter_rect)

# draw rectangles on screen
for rect in rects:
    pygame.draw.rect(window, WHITE, rect)
    letter_surface = font.render(letters[rects.index(rect)], True, BLACK)
    window.blit(letter_surface, rect)

# update display
pygame.display.update()

# wait for user to close window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()