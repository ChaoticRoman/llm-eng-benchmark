Here's a simple implementation of the Snake game in Python using the Pygame library:

```python
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Define game variables
snake_size = 20
snake_speed = 15
clock = pygame.time.Clock()

# Define snake and food
snake_x = width // 2
snake_y = height // 2
snake_dx, snake_dy = 0, 0
snake_body = []
food_x = round(random.randrange(0, width - snake_size) / snake_size) * snake_size
food_y = round(random.randrange(0, height - snake_size) / snake_size) * snake_size

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_dx != snake_size:
                snake_dx, snake_dy = -snake_size, 0
            elif event.key == pygame.K_RIGHT and snake_dx != -snake_size:
                snake_dx, snake_dy = snake_size, 0
            elif event.key == pygame.K_UP and snake_dy != snake_size:
                snake_dx, snake_dy = 0, -snake_size
            elif event.key == pygame.K_DOWN and snake_dy != -snake_size:
                snake_dx, snake_dy = 0, snake_size

    # Move the snake
    snake_x += snake_dx
    snake_y += snake_dy

    # Check for collision with walls
    if snake_x < 0 or snake_x >= width or snake_y < 0 or snake_y >= height:
        running = False

    # Check for collision with food
    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, width - snake_size) / snake_size) * snake_size
        food_y = round(random.randrange(0, height - snake_size) / snake_size) * snake_size
    else:
        snake_body.pop(0)

    # Add new segment to the snake
    snake_body.append((snake_x, snake_y))

    # Check for collision with itself
    for segment in snake_body[:-1]:
        if segment == (snake_x, snake_y):
            running = False

    # Clear the window
    window.fill(black)

    # Draw the snake
    for segment in snake_body:
        pygame.draw.rect(window, white, [segment[0], segment[1], snake_size, snake_size])

    # Draw the food
    pygame.draw.rect(window, red, [food_x, food_y, snake_size, snake_size])

    # Update the display
    pygame.display.update()

    # Set the game clock
    clock.tick(snake_speed)

# Quit the game
pygame.quit()
```

This code sets up a basic Snake game using Pygame. The snake moves around the screen, and the player controls its direction using the arrow keys. The objective is to eat the food (red squares) that appear randomly on the screen. Each time the snake eats the food, it grows longer. The game ends if the snake collides with the walls or with its own body.

Make sure you have Pygame installed (`pip install pygame`) before running the code. You can customize the game by modifying the window size, snake size, snake speed, colors, and adding additional features like scoring and game over screens.
