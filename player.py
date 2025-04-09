from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED,PLAYER_SPEED,PLAYER_SHOOT_SPEED,PLAYER_SHOOT_COOLDOWN
from circleshape import CircleShape
from shot import Shot
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        # Call the parent class's constructor with x, y, and PLAYER_RADIUS
        super().__init__(x, y, PLAYER_RADIUS)
        # Initialize rotation to 0
        self.rotation = 0
        self.cool_down = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        # Draw the player as a triangle
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.cool_down -=dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_q]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_z]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.cool_down <= 0:
            self.cool_down = PLAYER_SHOOT_COOLDOWN
            # Create a new shot at the player's position
            shot = Shot(self.position.x, self.position.y)
            
            # Calculate velocity direction based on player rotation
            shot_direction = pygame.Vector2(0, 1).rotate(self.rotation)
            
            # Set the shot's velocity (scaled by PLAYER_SHOOT_SPEED)
            shot.velocity = shot_direction * PLAYER_SHOOT_SPEED
            
            return shot