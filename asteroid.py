# asteroid.py
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # Call the parent class's constructor with x, y, and radius
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        # Draw the asteroid as a circle
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)
        
    def update(self, dt):
        # Move the asteroid based on its velocity
        self.position += self.velocity * dt
    
    def split(self):
        # Kill the current asteroid
        self.kill()
    
        # If this is a small asteroid, don't spawn new ones
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Calculate new radius for the smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        # Generate a random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)
        
        # Create two new velocity vectors by rotating the current velocity
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)
        
        # Create two new smaller asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        # Set their velocities (scaled up by 1.2 for faster movement)
        asteroid1.velocity = new_velocity1 * 1.2
        asteroid2.velocity = new_velocity2 * 1.2