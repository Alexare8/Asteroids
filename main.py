import pygame
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Establish object groups for easier handling of many similar objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    # Player objects should be part of these groups
    Player.containers = (updatable, drawable)

    # Instantiate a player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0 #delta-time

    # MAIN GAME LOOP
    while True: 
        # Exit the program, if requested
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update each updatable object
        updatable.update(dt)

        screen.fill("black")

        # Draw each drawable object
        for obj in drawable:
            obj.draw(screen)

        # Show the newly updated screen
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
