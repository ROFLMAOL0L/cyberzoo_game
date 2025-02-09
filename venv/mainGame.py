import pygame
from screenSettings import ScreenSettings
from controls import Controls
from mainHero import MainHero

global screen, screen_settings, screen_clock, controls

def mainGameInit():
    global screen, screen_settings, screen_clock, controls
    pygame.init()
    screen_settings = ScreenSettings()
    pygame.display.set_caption("CyberZoo")
    screen = pygame.display.set_mode((screen_settings.width, screen_settings.height))
    screen_clock = pygame.time.Clock()
    controls = Controls(pygame.event.get())

def mainGame():
    background = pygame.image.load("../sources/sprites/background/street_bg_1.jpg")

    # Main hero sprites
    main_hero_group = pygame.sprite.Group()
    main_hero = MainHero(main_hero_group)
    main_hero_group.add(main_hero)

    RUNNING = True
    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()
            controls.handle_controls(event, main_hero)


        screen.blit(background, (0,0))
        main_hero_group.update()
        main_hero_group.draw(screen)

        pygame.display.flip()
        screen_clock.tick(screen_settings.fps)


if __name__ == "__main__":
    mainGameInit()
    mainGame()
