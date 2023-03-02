import pygame
from config import BACKGROUND_COLOR_1, FONT_COLOR, WIN_SIZE, BUTTON_COLOR

# Menu items
menu_items = ["Start", "Settings", "Exit"]

# Define y-coordinate of top of first menu item
menu_top = 130


class GameMenu:
    def __init__(self, game_window, font, screen_event):
        self.game_window = game_window
        self.game_state = 'menu'
        self.screen_event = screen_event
        self.font = font

    def main_menu(self):
        while self.game_state == 'menu':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    # Check if mouse click is within a menu item
                    for i, item in enumerate(menu_items):
                        item_text = self.font.render(item, True, FONT_COLOR)
                        item_width, item_height = item_text.get_size()
                        item_left = (WIN_SIZE - item_width) / 2
                        item_top = menu_top + i * item_height
                        item_rect = pygame.Rect(item_left, item_top, item_width, item_height)
                        if item_rect.collidepoint(mouse_pos):
                            if item == "Start":
                                print("Start game")
                                self.game_state = 'game'
                                break
                            elif item == "Settings":
                                print("Open settings")
                            elif item == "Exit":
                                pygame.quit()

            # Clear the screen
            # self.game_window.fill(BACKGROUND_COLOR_1)

            # Draw menu items
            for i, item in enumerate(menu_items):
                item_text = self.font.render(item, True, FONT_COLOR)
                item_width, item_height = item_text.get_size()
                item_left = (WIN_SIZE - item_width) / 2
                item_top = menu_top + i * item_height
                item_rect = pygame.Rect(item_left, item_top, item_width, item_height)
                # Highlight menu item if mouse is over it
                if item_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.rect(self.game_window, BUTTON_COLOR, item_rect)
                self.game_window.blit(item_text, (item_left, item_top))

            # Update the screen
            pygame.display.flip()

    def settings_menu(self):
        pass
