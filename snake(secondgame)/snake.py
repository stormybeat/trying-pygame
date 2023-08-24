# Import the modules used for the program
import pygame

# Import pygame.locals for easier access to key coordinates
from pygame.locals import (
    RLEACCEL,
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

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
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