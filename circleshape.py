import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    def collides_with(self, other):
        # Calculate the distance between the centers of the two circular objects
        distance = self.position.distance_to(other.position)
        # If the distance is less than the sum of the radii, the circles are colliding
        return distance < (self.radius + other.radius)