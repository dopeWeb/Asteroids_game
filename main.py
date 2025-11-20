import sys
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
import pygame 
from constants import SCREEN_WIDTH,SCREEN_HEIGHT
from logger import log_state
from logger import log_event
from shot import Shot



def main():
    print("Starting Asteroids with pygame version: VERSION")
    print(f"Screen width: {SCREEN_WIDTH} Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    shots = pygame.sprite.Group()         
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)   


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    player_start_x = SCREEN_WIDTH / 2
    player_start_y = SCREEN_HEIGHT / 2
    player = Player(x=player_start_x, y=player_start_y)

    asteroid_field = AsteroidField() 

    running = True
    while running:
        # 1) Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 2) Time step
        dt = clock.tick(60) / 1000.0

        # 3) Update
        log_state()
        updatable.update(dt)

        # 3.5) Player vs asteroids
        for rock in asteroids:
            if player.collides_with(rock):
                log_event("player_hit")
                print("Game over!")
                pygame.quit()
                sys.exit()

        # 3.6) Shots vs asteroids
        for rock in asteroids:
            for shot in shots:
                if rock.collides_with(shot):
                    log_event("asteroid_shot")
                    rock.split()
                    shot.kill()
                    break

        # 4) Draw
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

    pygame.quit()




if __name__ == "__main__":
    main() 