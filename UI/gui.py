import pygame
import sys

class SnakeGameGUI:
    def __init__(self, game, cell_size=20):
        # Initialize the GUI with the game and cell size
        self.game = game
        self.cell_size = cell_size
        self.width = game.width * cell_size
        self.height = game.height * cell_size
        self.state = 'MENU'
        self.showing_popup = False
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Snake Game')

        # Load background images
        self.menu_background = pygame.image.load(r'C:\Users\david\OneDrive\שולחן העבודה\snake\Images/HD-wallpaper-classic-snake-adventures-snake-game.jpg')
        self.menu_background = pygame.transform.scale(self.menu_background, (self.width, self.height))
        self.game_background = pygame.image.load(r'C:\Users\david\OneDrive\שולחן העבודה\snake\Images/6.png')
        self.game_background = pygame.transform.scale(self.game_background, (self.width, self.height))
        self.game_over_background = pygame.image.load(r'C:\Users\david\OneDrive\שולחן העבודה\snake\Images/game_over_background.jpg')
        self.game_over_background = pygame.transform.scale(self.game_over_background, (self.width, self.height))

        # Load snake images
        self.snake_head_image = pygame.image.load(r'C:\Users\david\OneDrive\שולחן העבודה\snake\Images/snake_head.png')
        self.snake_head_image = pygame.transform.scale(self.snake_head_image, (self.cell_size, self.cell_size))
        self.snake_body_image = pygame.image.load(r'C:\Users\david\OneDrive\שולחן העבודה\snake\Images/snake_body.png')
        self.snake_body_image = pygame.transform.scale(self.snake_body_image, (self.cell_size, self.cell_size))

        # Define buttons
        self.button_width = 120
        self.button_height = 50
        self.start_button = pygame.Rect(self.width // 2 - self.button_width // 2, self.height // 2 - self.button_height - 10, self.button_width, self.button_height)
        self.restart_button = pygame.Rect(self.width // 2 - self.button_width // 2, self.height // 2 - 50, self.button_width, self.button_height)  # Moved up
        self.quit_button = pygame.Rect(self.width // 2 - self.button_width // 2, self.height // 2 + 20, self.button_width, self.button_height)  # Moved up
        self.menu_button = pygame.Rect(self.width // 2 - self.button_width // 2, self.height // 2 + 90, self.button_width + 40, self.button_height)  # Moved up and increased width
        self.exit_button = pygame.Rect(self.width // 2 - self.button_width // 2, self.height // 2 + 150, self.button_width, self.button_height)  # Added exit button
        self.popup_yes_button = pygame.Rect(self.width // 2 - 60, self.height // 2, 50, 30)
        self.popup_no_button = pygame.Rect(self.width // 2 + 10, self.height // 2, 50, 30)

    def draw(self):
        # Draw the game screen
        self.screen.blit(self.game_background, (0, 0))
        for i, (x, y) in enumerate(self.game.get_snake()):
            if i == 0:
                self.screen.blit(self.snake_head_image, (x * self.cell_size, y * self.cell_size))
            else:
                self.screen.blit(self.snake_body_image, (x * self.cell_size, y * self.cell_size))
        food_x, food_y = self.game.get_food()
        self._draw_rectangle(food_x, food_y, (255, 0, 0))
        self._draw_score()
        pygame.display.flip()

    def _draw_rectangle(self, x, y, color):
        # Draw a rectangle (used for drawing food)
        rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
        pygame.draw.rect(self.screen, color, rect)

    def _draw_score(self):
        # Draw the current score on the screen
        font = pygame.font.SysFont(None, 35)
        score_text = font.render(f'Score: {self.game.get_score()}', True, (255, 255, 255))
        high_score_text = font.render(f'High Score: {self.game.get_high_score()}', True, (255, 255, 255))
        self.screen.blit(score_text, (5, 5))
        self.screen.blit(high_score_text, (self.width - 200, 5))

    def show_menu(self):
        # Display the menu screen
        self.screen.blit(self.menu_background, (0, 0))
        
        # Center the title text at the top
        title_font = pygame.font.SysFont(None, 50)
        title_text = title_font.render('Snake Game', True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(self.width // 2, self.height // 5))
        self.screen.blit(title_text, title_rect.topleft)
        
        # Draw the "Start Game" button below the title with wider background
        start_button_width = self.button_width + 40
        start_button_height = self.button_height
        self.start_button = pygame.Rect(self.width // 2 - start_button_width // 2, self.height // 2 - start_button_height // 2, start_button_width, start_button_height)
        pygame.draw.rect(self.screen, (0, 255, 0), self.start_button)
        
        # Render the "Start Game" text centered on the button
        button_font = pygame.font.SysFont(None, 35)
        start_text = button_font.render('Start Game', True, (0, 0, 0))
        start_text_rect = start_text.get_rect(center=self.start_button.center)
        self.screen.blit(start_text, start_text_rect.topleft)

        # Draw the "Exit Game" button below the "Start Game" button
        self.exit_button = pygame.Rect(self.width // 2 - self.button_width // 2, self.height // 2 + start_button_height, self.button_width, self.button_height)
        pygame.draw.rect(self.screen, (255, 0, 0), self.exit_button)
        
        # Render the "Exit Game" text centered on the button
        exit_text = button_font.render('Exit Game', True, (0, 0, 0))
        exit_text_rect = exit_text.get_rect(center=self.exit_button.center)
        self.screen.blit(exit_text, exit_text_rect.topleft)
        
        pygame.display.flip()

    def show_game_over(self):
        # Display the game over screen
        self.screen.blit(self.game_over_background, (0, 0))  # Use colorful background
        font = pygame.font.SysFont(None, 75)
        game_over_text = font.render('GAME OVER', True, (255, 0, 0))

        # Raise the high score text a bit higher above "GAME OVER" text
        high_score_font = pygame.font.SysFont(None, 35)
        high_score_text = high_score_font.render(f'High Score: {self.game.get_high_score()}', True, (255, 255, 255))
        self.screen.blit(high_score_text, (self.width // 2 - high_score_text.get_width() // 2, self.height // 4 - 80))

        # Raise the "GAME OVER" text a bit higher
        self.screen.blit(game_over_text, (self.width // 4, self.height // 4 - 30))

        # Draw the buttons with appropriate font size
        button_font = pygame.font.SysFont(None, 30)
        pygame.draw.rect(self.screen, (0, 255, 0), self.restart_button)
        pygame.draw.rect(self.screen, (255, 0, 0), self.quit_button)
        pygame.draw.rect(self.screen, (0, 0, 255), self.menu_button)
        restart_text = button_font.render('Restart', True, (0, 0, 0))
        self.screen.blit(restart_text, (self.restart_button.x + 15, self.restart_button.y + 10))
        quit_text = button_font.render('Quit', True, (0, 0, 0))
        self.screen.blit(quit_text, (self.quit_button.x + 30, self.quit_button.y + 10))
        menu_text = button_font.render('Back to Menu', True, (0, 0, 0))
        self.screen.blit(menu_text, (self.menu_button.x + 5, self.menu_button.y + 10))

        pygame.display.flip()

    def show_popup(self):
        # Show a popup confirmation window
        popup_width = 200
        popup_height = 100
        popup_rect = pygame.Rect(self.width // 2 - popup_width // 2, self.height // 2 - popup_height // 2, popup_width, popup_height)
        pygame.draw.rect(self.screen, (200, 200, 200), popup_rect)
        pygame.draw.rect(self.screen, (0, 0, 0), popup_rect, 2)

        # Render popup text
        font = pygame.font.SysFont(None, 35)
        text = font.render('Return to Menu?', True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2 - 20))
        self.screen.blit(text, text_rect.topleft)

        # Draw "Yes" button
        pygame.draw.rect(self.screen, (0, 255, 0), self.popup_yes_button)
        yes_text = font.render('Yes', True, (0, 0, 0))
        yes_text_rect = yes_text.get_rect(center=self.popup_yes_button.center)
        self.screen.blit(yes_text, yes_text_rect.topleft)

        # Draw "No" button
        pygame.draw.rect(self.screen, (255, 0, 0), self.popup_no_button)
        no_text = font.render('No', True, (0, 0, 0))
        no_text_rect = no_text.get_rect(center=self.popup_no_button.center)
        self.screen.blit(no_text, no_text_rect.topleft)

        pygame.display.flip()

    def handle_events(self):
        # Handle user inputs and events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.game.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    self.game.change_direction("RIGHT")
                elif event.key == pygame.K_UP:
                    self.game.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    self.game.change_direction("DOWN")
                elif event.key == pygame.K_RETURN:
                    if self.state == 'MENU':
                        self.state = 'GAME'
                    elif self.game.is_game_over():
                        self.game.reset()
                        self.state = 'GAME'
                elif event.key == pygame.K_ESCAPE and not self.showing_popup:
                    self.showing_popup = True
                    self.show_popup()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.state == 'MENU':
                    if self.start_button.collidepoint(event.pos):
                        self.state = 'GAME'
                    elif self.exit_button.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                elif self.game.is_game_over():
                    if self.restart_button.collidepoint(event.pos):
                        self.game.reset()
                        self.state = 'GAME'
                    elif self.quit_button.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                    elif self.menu_button.collidepoint(event.pos):
                        self.state = 'MENU'
                elif self.showing_popup:
                    if self.popup_yes_button.collidepoint(event.pos):
                        self.showing_popup = False
                        self.state = 'MENU'
                    elif self.popup_no_button.collidepoint(event.pos):
                        self.showing_popup = False

    def tick(self, fps):
        # Control the game frame rate
        self.clock.tick(fps)

    def run(self):
        # Main loop for the GUI
        while True:
            if self.state == 'MENU':
                self.show_menu()
            elif self.state == 'GAME':
                self.draw()
            elif self.game.is_game_over():
                self.show_game_over()
            self.handle_events()
            self.tick(10)
