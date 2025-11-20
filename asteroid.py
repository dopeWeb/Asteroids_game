import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,            # surface to draw on
            "white",           # color
            self.position,     # center of the circle
            self.radius,       # radius of the asteroid
            LINE_WIDTH         # thickness of the line
        )

    def update(self, dt):
        self.position += self.velocity * dt