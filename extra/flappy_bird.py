import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird (Python)")

# Colors
WHITE = (255, 255, 255)
BLUE = (135, 206, 250)
GREEN = (0, 200, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Bird settings
bird_x, bird_y = 50, HEIGHT // 2
bird_radius = 15
bird_velocity = 0
gravity = 0.5
jump_strength = -8

# Pipe settings
pipe_width = 70
pipe_gap = 150
pipe_speed = 3
pipes = []

# Score
score = 0
font = pygame.font.SysFont(None, 40)

def draw_bird(x, y):
    pygame.draw.circle(screen, (255, 255, 0), (x, int(y)), bird_radius)

def create_pipe():
    height = random.randint(100, 400)
    return {"x": WIDTH, "top": height, "bottom": height + pipe_gap}

def draw_pipes(pipes):
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, (pipe["x"], 0, pipe_width, pipe["top"]))
        pygame.draw.rect(screen, GREEN, (pipe["x"], pipe["bottom"], pipe_width, HEIGHT - pipe["bottom"]))

def check_collision(bird_y, pipes):
    if bird_y - bird_radius < 0 or bird_y + bird_radius > HEIGHT:
        return True
    for pipe in pipes:
        if (bird_x + bird_radius > pipe["x"] and bird_x - bird_radius < pipe["x"] + pipe_width):
            if bird_y - bird_radius < pipe["top"] or bird_y + bird_radius > pipe["bottom"]:
                return True
    return False

# Main game loop
running = True
frame = 0
while running:
    clock.tick(FPS)
    screen.fill(BLUE)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = jump_strength

    # Bird movement
    bird_velocity += gravity
    bird_y += bird_velocity

    # Pipes movement
    if frame % 90 == 0:  # Add new pipe every 90 frames
        pipes.append(create_pipe())

    for pipe in pipes:
        pipe["x"] -= pipe_speed

    pipes = [pipe for pipe in pipes if pipe["x"] + pipe_width > 0]  # Remove off-screen pipes

    # Check for score
    for pipe in pipes:
        if pipe["x"] + pipe_width == bird_x:
            score += 1

    # Draw
    draw_bird(bird_x, bird_y)
    draw_pipes(pipes)

    # Score display
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Collision check
    if check_collision(bird_y, pipes):
        print("Game Over! Final Score:", score)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    frame += 1