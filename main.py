# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        
        for object in updatable:
            update = object.update(dt)
            if isinstance(object, Player) and update != None:
                updatable.add(update)
                drawable.add(update)
                shots.add(update)  

        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                return
            for shot in shots:
    
                if asteroid.check_collision(shot):
                    shot.kill()
                    asteroid.kill()
                    new_asteroids = asteroid.split()
                    if isinstance(new_asteroids, tuple):
                        asteroids.add(new_asteroids[0], new_asteroids[1])
                        updatable.add(new_asteroids[0], new_asteroids[1])
                        drawable.add(new_asteroids[0], new_asteroids[1])
                
        for object in drawable:
            object.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()