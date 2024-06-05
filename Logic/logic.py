import random

class SnakeGame:
    def __init__(self, width, height):
        # Initialize the game with the given width and height
        self.width = width
        self.height = height
        self.high_score = 0
        self.reset()

    def reset(self):
        # Reset the game state
        self.snake = [(self.width // 2, self.height // 2)]
        self.direction = "UP"
        self.food = self._place_food()
        self.score = 0
        self.game_over = False

    def reset_game(self):
        # Reset the game state (duplicate method for reset)
        self.snake = [(self.width // 2, self.height // 2)]
        self.direction = "UP"
        self.food = self._place_food()
        self.score = 0
        self.game_over = False

    def _place_food(self):
        # Place food at a random position not occupied by the snake
        while True:
            food = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
            if food not in self.snake:
                return food

    def change_direction(self, direction):
        # Change the direction of the snake
        if (direction == "LEFT" and self.direction != "RIGHT") or \
           (direction == "RIGHT" and self.direction != "LEFT") or \
           (direction == "UP" and self.direction != "DOWN") or \
           (direction == "DOWN" and self.direction != "UP"):
            self.direction = direction

    def update(self):
        # Update the snake's position and check for collisions
        if self.game_over:
            return

        head_x, head_y = self.snake[0]
        if self.direction == "LEFT":
            head_x -= 1
        elif self.direction == "RIGHT":
            head_x += 1
        elif self.direction == "UP":
            head_y -= 1
        elif self.direction == "DOWN":
            head_y += 1

        new_head = (head_x, head_y)
        if (new_head in self.snake or
            head_x < 0 or head_x >= self.width or
            head_y < 0 or head_y >= self.height):
            self.game_over = True
            if self.score > self.high_score:
                self.high_score = self.score
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.food = self._place_food()
        else:
            self.snake.pop()

    def get_snake(self):
        # Get the current snake positions
        return self.snake

    def get_food(self):
        # Get the current food position
        return self.food

    def get_score(self):
        # Get the current score
        return self.score

    def get_high_score(self):
        # Get the high score
        return self.high_score

    def is_game_over(self):
        # Check if the game is over
        return self.game_over
