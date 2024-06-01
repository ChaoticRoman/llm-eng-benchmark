Here is a simple implementation of the classic Snake game in Python using the Pygame library:

```python
import pygame
import time
import random

pygame.init()

# Set up display
width = 800
height = 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake properties
snake_block = 10
snake_speed = 15

# Initialize snake
snake_list = []
snake_length = 1

# Initial position of snake
x = width / 2
y = height / 2
x_change = 0
y_change = 0

# Food position
food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

# Game over flag
game_over = False

# Function to draw snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, green, [x[0], x[1], snake_block, snake_block])

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -snake_block
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = snake_block
                y_change = 0
            elif event.key == pygame.K_UP:
                y_change = -snake_block
                x_change = 0
            elif event.key == pygame.K_DOWN:
                y_change = snake_block
                x_change = 0

    if x >= width or x < 0 or y >= height or y < 0:
        game_over = True

    x += x_change
    y += y_change

    display.fill(black)
    pygame.draw.rect(display, red, [food_x, food_y, snake_block, snake_block])

    snake_head = []
    snake_head.append(x)
    snake_head.append(y)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    for x in snake_list[:-1]:
        if x == snake_head:
            game_over = True

    draw_snake(snake_block, snake_list)

    pygame.display.update()

    if x == food_x and y == food_y:
        food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
        snake_length += 1

    pygame.time.Clock().tick(snake_speed)

pygame.quit()
quit()
```

To run this code, you will need to have the Pygame library installed. You can install it using pip:

```
pip install pygame
```

This code creates a simple Snake game where the player controls the snake using the arrow keys to eat the food and grow in length. The game ends if the snake runs into the walls or itself.
