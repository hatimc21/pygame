from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        # Call the parent class's constructor with x, y, and SHOT_RADIUS
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen):
        # Draw the shot as a small filled circle
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius)
    
    def update(self, dt):
        # Move the shot based on its velocity
        self.position += self.velocity * dt