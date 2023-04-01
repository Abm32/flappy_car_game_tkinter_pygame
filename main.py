import pygame
import random

# Initialize Pygame
pygame.init()

# Define some constants
WIDTH = 288
HEIGHT = 512
FPS = 60
FONT = pygame.font.SysFont('Comic Sans MS', 30)

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load the images
background_image = pygame.image.load("background.png").convert()
bird_image = pygame.image.load("bird.png").convert_alpha()
pipe_image = pygame.image.load("pipe.png").convert_alpha()

# Define the Bird class
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = bird_image
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = HEIGHT // 2
        self.speed = 0

    def update(self):
        self.speed += 1
        self.rect.y += self.speed

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.speed = 0

    def flap(self):
        self.speed = -12

# Define the Pipe class
class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, is_bottom):
        super().__init__()
        self.image = pipe_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        if is_bottom:
            self.rect.bottom = y
        else:
            self.rect.top = y - 320

    def update(self):
        self.rect.x -= 2
        if self.rect.right < 0:
            self.kill()

# Set up the groups
all_sprites = pygame.sprite.Group()
pipes = pygame.sprite.Group()

# Add the bird to the groups
bird = Bird()
all_sprites.add(bird)

# Set up the game loop
clock = pygame.time.Clock()
running = True
score = 0

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.flap()

    # Update the game state
    all_sprites.update()

    # Spawn pipes
    if len(pipes) < 4:
        for i in range(2):
            pipe = Pipe(WIDTH + i * 200, random.randint(100, 350), i)
            pipes.add(pipe)
            all_sprites.add(pipe)

    # Check for collisions
    if pygame.sprite.spritecollide(bird, pipes, False):
        running = False

    # Remove pipes that have gone off screen
    for pipe in pipes:
        if pipe.rect.right < 0:
            pipes.remove(pipe)

    # Draw everything
    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)
    score_text = FONT.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Increase the score
    score += 1

    # Wait for the next frame
    clock.tick(FPS)

# Clean up the game
pygame.quit()
           