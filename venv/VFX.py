from pygame.sprite import Sprite
from pygame.image import load
from pygame.time import get_ticks

class VFX(Sprite):
    def __init__(self, list_of_sprites, pos):
        super().__init__()
        self.pos = (0, 0)
        self.animation_list = []
        for path in list_of_sprites:
            self.animation_list.append(load(path).convert_alpha())
        self.image = self.animation_list[0]
        self.animation_frame = 0
        self.rect = self.animation_list[0].get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.previous_time = get_ticks()

    def update(self):
        current_time = get_ticks()
        if current_time - self.previous_time > 50:
            if self.animation_frame >= len(self.animation_list):
                self.kill()
                return
            self.image = self.animation_list[self.animation_frame]
            self.animation_frame += 1
            self.previous_time = current_time
