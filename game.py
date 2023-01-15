import sys
import pygame

class AlienINvasion:
    """class to manage the game assets and behavior"""
    def __init__(self) -> None:
        """initialise the game"""
        pygame.init()

        self.screen = pygame.display.set_mode(1200, 800)
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """The game main loop"""
        while True:
            # listen for keyboard and mouse events
            for event in pygame.events.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # make a game instance and run the game
    ai = AlienINvasion()
    ai.run_game()