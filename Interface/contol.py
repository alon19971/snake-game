import pygame
from Logic.logic import SnakeGame
from UI.gui import SnakeGameGUI

class SnakeGameController:
    def __init__(self):
        # Initialize the game controller
        pygame.init()
        self.state = 'MENU'
        self.game = SnakeGame(width=30, height=20)
        self.gui = SnakeGameGUI(self.game)
        self.fps = 10

    def run(self):
        # Main game loop
        while True:
            if self.state == 'MENU':
                self.show_menu()
            elif self.state == 'GAME':
                self.play_game()
            elif self.state == 'GAME_OVER':
                self.show_game_over()
            self.gui.tick(self.fps)

    def show_menu(self):
        # Display the menu screen
        self.gui.show_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.start_game()
                elif event.key == pygame.K_ESCAPE:
                    self.gui.showing_popup = True
                    self.gui.show_popup()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.gui.start_button.collidepoint(event.pos):
                    self.start_game()
                elif self.gui.exit_button.collidepoint(event.pos):
                    pygame.quit()
                    exit()
                elif self.gui.showing_popup:
                    if self.gui.popup_yes_button.collidepoint(event.pos):
                        self.gui.showing_popup = False
                        self.state = 'MENU'
                    elif self.gui.popup_no_button.collidepoint(event.pos):
                        self.gui.showing_popup = False

    def start_game(self):
        # Start a new game
        self.game.reset_game()
        self.state = 'GAME'

    def play_game(self):
        # Play the game
        self.gui.handle_events()
        if not self.game.is_game_over():
            self.game.update()
        else:
            self.state = 'GAME_OVER'
        self.gui.draw()

    def show_game_over(self):
        # Display the game over screen
        self.gui.show_game_over()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.gui.restart_button.collidepoint(event.pos):
                    self.start_game()
                elif self.gui.quit_button.collidepoint(event.pos):
                    pygame.quit()
                    exit()
                elif self.gui.menu_button.collidepoint(event.pos):
                    self.state = 'MENU'
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.start_game()
                elif event.key == pygame.K_ESCAPE:
                    self.gui.showing_popup = True
                    self.gui.show_popup()

if __name__ == '__main__':
    # Start the game controller if this file is executed
    controller = SnakeGameController()
    controller.run()
