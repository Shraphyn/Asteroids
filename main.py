import pygame
from constants import *
from player import *
from asteroids import *
from asteroidfield import *
import sys
from bullets import *
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    
    AsteroidField.containers = (updatable,)
    New_AsteroidField = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) 
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt_ms = clock.tick(60)
        dt_seconds = dt_ms / 1000
        updatable.update(dt_seconds)
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                sys.exit()
        
        for asteroid in asteroids:
            for bullet in shots:
                if bullet.collision(asteroid):
                    bullet.kill()
                    asteroid.split()
        screen.fill("black")
        for drawabl in drawable:
            drawabl.draw(screen)
        pygame.display.flip()

        

        
        

if __name__ == "__main__":
    main()



