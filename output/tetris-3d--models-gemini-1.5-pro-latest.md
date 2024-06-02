```python
import pygame
import random

# Initialize Pygame
pygame.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

# Block size
BLOCK_SIZE = 30

# Game speed
FPS = 60

# Tetromino shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
    [[1, 1], [1, 1]],  # O
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]]  # Z
]

# Colors for each shape
COLORS = [
    (0, 255, 255),  # Cyan
    (128, 0, 128),  # Purple
    (255, 165, 0),  # Orange
    (0, 0, 255),  # Blue
    (255, 255, 0),  # Yellow
    (0, 255, 0),  # Green
    (255, 0, 0)  # Red
]

# Function to draw a block


def draw_block(x, y, color):
    pygame.draw.rect(screen, color, (x * BLOCK_SIZE, y *
                     BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, BLACK, (x * BLOCK_SIZE, y *
                     BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

# Function to draw the grid


def draw_grid():
    for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (SCREEN_WIDTH, y))

# Function to create a new tetromino


def new_tetromino():
    shape = random.choice(SHAPES)
    color = COLORS[SHAPES.index(shape)]
    x = SCREEN_WIDTH // (2 * BLOCK_SIZE) - len(shape[0]) // 2
    y = -len(shape)
    return shape, color, x, y

# Function to draw a tetromino


def draw_tetromino(shape, color, x, y):
    for row_index, row in enumerate(shape):
        for col_index, cell in enumerate(row):
            if cell:
                draw_block(x + col_index, y + row_index, color)

# Function to check for collision


def check_collision(shape, grid, x, y):
    for row_index, row in enumerate(shape):
        for col_index, cell in enumerate(row):
            if cell:
                # Check if out of bounds
                if x + col_index < 0 or x + col_index >= SCREEN_WIDTH // BLOCK_SIZE or y + row_index >= SCREEN_HEIGHT // BLOCK_SIZE:
                    return True
                # Check if colliding with existing block
                if y + row_index >= 0 and grid[y + row_index][x + col_index]:
                    return True
    return False

# Function to clear complete lines


def clear_lines(grid):
    lines_cleared = 0
    for row_index in range(len(grid)):
        if all(grid[row_index]):
            grid.pop(row_index)
            grid.insert(0, [0 for _ in range(SCREEN_WIDTH // BLOCK_SIZE)])
            lines_cleared += 1
    return lines_cleared

# Function to display game over screen


def game_over():
    font = pygame.font.Font(None, 72)
    text = font.render("Game Over", True, WHITE)
    text_rect = text.get_rect(
        center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.delay(3000)

# Initialize the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("3D Tetris")

# Game variables
grid = [[0 for _ in range(SCREEN_WIDTH // BLOCK_SIZE)]
        for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)]
current_shape, current_color, current_x, current_y = new_tetromino()
next_shape, next_color, _, _ = new_tetromino()
clock = pygame.time.Clock()
game_over_flag = False

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and not game_over_flag:
                if not check_collision(current_shape, grid, current_x - 1, current_y):
                    current_x -= 1
            if event.key == pygame.K_RIGHT and not game_over_flag:
                if not check_collision(current_shape, grid, current_x + 1, current_y):
                    current_x += 1
            if event.key == pygame.K_DOWN and not game_over_flag:
                if not check_collision(current_shape, grid, current_x, current_y + 1):
                    current_y += 1
            if event.key == pygame.K_SPACE and not game_over_flag:  # Rotate shape
                new_shape = list(
                    zip(*current_shape[::-1]))  # Rotate 90 degrees
                if not check_collision(new_shape, grid, current_x, current_y):
                    current_shape = new_shape

    # Game logic
    if not game_over_flag:
        # Move tetromino down
        if not check_collision(current_shape, grid, current_x, current_y + 1):
            current_y += 1
        else:
            # Place tetromino
            for row_index, row in enumerate(current_shape):
                for col_index, cell in enumerate(row):
                    if cell:
                        grid[current_y + row_index][current_x +
                                                     col_index] = current_color
            # Create new tetromino
            current_shape, current_color, current_x, current_y = next_shape, next_color, _, _
            next_shape, next_color, _, _ = new_tetromino()

            # Check for game over
            if check_collision(current_shape, grid, current_x, current_y):
                game_over_flag = True

        # Clear complete lines
        lines_cleared = clear_lines(grid)

    # Drawing
    screen.fill(BLACK)  # Clear the screen
    draw_grid()  # Draw the grid
    draw_tetromino(current_shape, current_color,
                   current_x, current_y)  # Draw current tetromino
    draw_tetromino(next_shape, next_color, SCREEN_WIDTH //
                   BLOCK_SIZE + 2, 2)  # Draw next tetromino

    # Game over screen
    if game_over_flag:
        game_over()
        running = False

    # Update the display
    pygame.display.flip()

    # Control game speed
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
```

**Explanation:**

1. **Initialization and Setup:**
   - Imports `pygame` and `random`.
   - Defines colors, screen dimensions, block size, game speed, tetromino shapes and colors.
   - Creates functions for drawing blocks, the grid, and tetrominos.

2. **Game Functions:**
   - `new_tetromino()`: Generates a random tetromino with its color, initial x, and y positions.
   - `check_collision()`: Checks if a tetromino collides with the game grid boundaries or other placed blocks.
   - `clear_lines()`: Removes complete horizontal lines from the grid and shifts rows down.
   - `game_over()`: Displays the "Game Over" message and pauses for a few seconds.

3. **Main Game Loop:**
   - Initializes game variables like the grid, current tetromino, next tetromino, clock, and game over flag.
   - Enters the main game loop, which continues until the user quits.

4. **Event Handling:**
   - Checks for events like keyboard presses (left, right, down arrows for movement, space for rotation) and the close button.
   - Updates the game state based on user input.

5. **Game Logic:**
   - Moves the current tetromino down at regular intervals.
   - If the tetromino collides, it's added to the grid, a new one is generated, and collision for game over is checked.
   - Clears any completed lines and updates the score.

6. **Drawing:**
   - Clears the screen.
   - Draws the grid, current tetromino, and the next tetromino.
   - Displays the game over screen if the game is over.

7. **Updating and Controlling Speed:**
   - Updates the display to show the changes.
   - Uses `clock.tick(FPS)` to control the game's frames per second.

**To run this code:**

1. Make sure you have Pygame installed (`pip install pygame`).
2. Save the code as a `.py` file (e.g., `tetris.py`).
3. Run the file from your terminal using `python tetris.py`.

This will give you a functional (but basic) 2D Tetris game. Remember, this is a starting point. You can add more features, like:

- **Scorekeeping:** Keep track of lines cleared and display the score.
- **Levels:** Increase the game speed as the player clears lines.
- **Music and Sound Effects:** Add audio elements to enhance the gameplay experience.
- **Improved Graphics:** Use images instead of simple rectangles for blocks and background. 
