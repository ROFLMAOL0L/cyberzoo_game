import pygame
from screenSettings import ScreenSettings

global screen, screen_settings, screen_clock

def mainGameInit():
    global screen, screen_settings, screen_clock
    pygame.init()
    screen_settings = ScreenSettings()
    pygame.display.set_caption("CyberZoo")
    screen = pygame.display.set_mode((screen_settings.width, screen_settings.height))
    screen_clock = pygame.time.Clock()


def mainGame():
    RUNNING = True
    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill((100, 100, 100))

        pygame.display.update()
        screen_clock.tick(screen_settings.fps)


if __name__ == "__main__":
    mainGameInit()
    mainGame()
