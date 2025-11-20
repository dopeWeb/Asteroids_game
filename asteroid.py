import random
from logger import log_event
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH

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


    def split(self):
        old_radius = self.radius

        self.kill()

        if old_radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        angle = random.uniform(20, 50)

        vel1 = self.velocity.rotate(angle)
        vel2 = self.velocity.rotate(-angle)

        new_radius = old_radius - ASTEROID_MIN_RADIUS

        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)

        a1.velocity = vel1 * 1.2
        a2.velocity = vel2 * 1.2