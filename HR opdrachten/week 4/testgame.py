import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Game variables
bird_width = 40
bird_height = 30
gravity = 0.5
jump_strength = -8

pipe_width = 60
pipe_gap = 150
pipe_velocity = -3
pipe_frequency = 1500  # milliseconds

# Load assets (Optional: You can load images and sounds if you have them)
font = pygame.font.SysFont('sans', 30)

# Function to draw bird
def draw_bird(bird_x, bird_y):
    pygame.draw.rect(screen, RED, (bird_x, bird_y, bird_width, bird_height))

# Function to generate pipes
def generate_pipe():
    pipe_top_height = random.randint(100, HEIGHT - pipe_gap - 40)
    pipe_bottom_height = HEIGHT - pipe_top_height - pipe_gap
    return pipe_top_height, pipe_bottom_height

# Function to draw pipes
def draw_pipe(pipe_x, pipe_top_height, pipe_bottom_height):
    pygame.draw.rect(screen, GREEN, (pipe_x, 0, pipe_width, pipe_top_height))
    pygame.draw.rect(screen, GREEN, (pipe_x, HEIGHT - pipe_bottom_height, pipe_width, pipe_bottom_height))

# Function to reset the game
def reset_game():
    global bird_x, bird_y, bird_velocity, pipes, score, game_over
    bird_x = 50
    bird_y = HEIGHT // 2
    bird_velocity = 0
    pipes = []
    score = 0
    game_over = False

# Game clock
clock = pygame.time.Clock()

# Initial game state
reset_game()

# Pipe list to manage multiple pipes
pipe_timer = pygame.USEREVENT + 1
pygame.time.set_timer(pipe_timer, pipe_frequency)

# Main game loop
running = True
while running:
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_SPACE:
                bird_velocity = jump_strength
        if event.type == pipe_timer and not game_over:
            pipe_top, pipe_bottom = generate_pipe()
            pipes.append([WIDTH, pipe_top, pipe_bottom])
    
    # Bird movement
    if not game_over:
        bird_velocity += gravity
        bird_y += bird_velocity
    
    # Draw bird
    draw_bird(bird_x, bird_y)
    
    # Pipe movement and drawing
    for pipe in pipes:
        pipe[0] += pipe_velocity
        draw_pipe(pipe[0], pipe[1], HEIGHT - pipe[2])

    # Pipe removal
    pipes = [pipe for pipe in pipes if pipe[0] > -pipe_width]

    # Collision detection
    for pipe in pipes:
        if bird_x + bird_width > pipe[0] and bird_x < pipe[0] + pipe_width:
            if bird_y < pipe[1] or bird_y + bird_height > HEIGHT - pipe[2]:
                game_over = True
    
    # Check if bird hits the ground or flies off the screen
    if bird_y >= HEIGHT - bird_height or bird_y <= 0:
        game_over = True
    
    # Score update
    if not game_over:
        for pipe in pipes:
            if pipe[0] + pipe_width < bird_x and not pipe[0] < bird_x - pipe_width:
                score += 1

    # Display score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    
    # Game over handling
    if game_over:
        # Pause for a moment and reset the game
        pygame.time.delay(1000)  # Wait for 1 second
        reset_game()  # Reset the game state

    pygame.display.update()
    clock.tick(60)

# Quit Pygame
pygame.quit()
