import random

class SnakeGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.high_score = 0
        self.reset()

    def reset(self):
        self.snake = [(self.width // 2, self.height // 2)]
        self.direction = "UP"
        self.food = self._place_food()
        self.score = 0
        self.game_over = False

    def reset_game(self):
        self.snake = [(self.width // 2, self.height // 2)]
        self.direction = "UP"
        self.food = self._place_food()
        self.score = 0
        self.game_over = False

    def _place_food(self):
        free_spaces = [(x, y) for x in range(self.width) for y in range(self.height) if (x, y) not in self.snake]
        return random.choice(free_spaces) if free_spaces else None

    def change_direction(self, direction):
        if (direction == "LEFT" and self.direction != "RIGHT") or \
           (direction == "RIGHT" and self.direction != "LEFT") or \
           (direction == "UP" and self.direction != "DOWN") or \
           (direction == "DOWN" and self.direction != "UP"):
            self.direction = direction

    def update(self):
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
        return self.snake

    def get_food(self):
        return self.food

    def get_score(self):
        return self.score

    def get_high_score(self):
        return self.high_score

    def is_game_over(self):
        return self.game_over
