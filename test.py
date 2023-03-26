import pygame

# Initializing Pygame
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((400, 300))

# Initializing Color
color = (48, 141, 70)
rect = pygame.Rect(30, 30, 100, 100)

# Drawing Rectangle
pygame.draw.rect(surface, color, rect,width= 10, border_radius= 20)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False