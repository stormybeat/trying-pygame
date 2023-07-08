# Import the modules used for the program
import pygame
import random
# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
screenWidth = 800
screenHeight = 600

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressedKeys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressedKeys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressedKeys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressedKeys[K_RIGHT]:
            self.rect.move_ip(5, 0)


        # Keep player on screen.
        if self.rect.left <0:
            self.rect.left = 0
        if self.rect.right > screenWidth:
            self.rect.right = screenWidth
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screenHeight:
            self.rect.bottom = screenHeight 


# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(screenWidth + 20, screenWidth + 100),
                random.randint(0, screenHeight),
            )
        )
        self.speed = random.randint(5, 20)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


# Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant screenWidth and screenHeight
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Create event for adding an enemy.
addEnemy = pygame.USEREVENT + 1
pygame.time.set_timer(addEnemy, 250)
# Instantiate player. Right now, this is just a rectangle.
player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Setup the clock for a decent framerate
clock = pygame.time.Clock()

# Variable to keep the main loop running
running = True

# Main loop
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False
        #adding an enemy
        elif event.type == addEnemy:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
    
    # Get the set of keys pressed and check for user input
    pressedKeys = pygame.key.get_pressed()

    # Update enemy position
    enemies.update()

    # Update the player sprite based on user keypresses
    player.update(pressedKeys)

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
    
    # If so, then remove the player and stop the loop
        player.kill()
        running = False

    # Update the display
    pygame.display.flip()
    
    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)

