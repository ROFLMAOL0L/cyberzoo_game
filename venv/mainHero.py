from pygame.sprite import Sprite
from pygame.image import load
class MainHero(Sprite):
    def __init__(self):
        super().__init__()

        # Attributes for animation and sprites
        self.stand_sprites = []
        self.stand_sprites.append(load("../sources/sprites/entities/main_hero/main_hero_left_128.png"))
        self.stand_sprites.append(load("../sources/sprites/entities/main_hero/main_hero_right_128.png"))
        self.run_left_sprites = []
        self.run_left_sprites.append(load("../sources/sprites/entities/main_hero/main_hero_run_left_1.png"))
        self.run_left_sprites.append(load("../sources/sprites/entities/main_hero/main_hero_run_left_2.png"))
        self.run_right_sprites = []
        self.run_right_sprites.append(load("../sources/sprites/entities/main_hero/main_hero_run_right_1.png"))
        self.run_right_sprites.append(load("../sources/sprites/entities/main_hero/main_hero_run_right_2.png"))
        self.image = self.stand_sprites[0]
        self.rect = self.image.get_rect()
        self.rect.center = (1280 // 2, 720 // 2)
        self.animation_frame = 0
        self.animation_frame_max = 60
        self.next_stand_animation = self.image

        # Attributes for movement
        self.acceleration_x = 2.0
        self.decceleration_x = 1.0
        self.acceleration_y = 1.5
        self.decceleration_y = 0.66
        self.momentum_x = 0.0
        self.momentum_y = 0.0
        self.max_momentum = 8.0
        self.moving_up = False
        self.moving_left = False
        self.moving_down = False
        self.moving_right = False

    def handle_momentum(self):
        if self.moving_up:
            self.momentum_y = max(self.momentum_y - self.acceleration_y, -self.max_momentum)
        if self.moving_down:
            self.momentum_y = min(self.momentum_y + self.acceleration_y, self.max_momentum)
        if self.moving_left:
            self.momentum_x = max(self.momentum_x - self.acceleration_x, -self.max_momentum)
        if self.moving_right:
            self.momentum_x = min(self.momentum_x + self.acceleration_x, self.max_momentum)
        if self.moving_down == self.moving_up:
            if self.momentum_y > 0:
                self.momentum_y = max(self.momentum_y - self.decceleration_y, 0)
            elif self.momentum_y < 0:
                self.momentum_y = min(self.momentum_y + self.decceleration_y, 0)
        if self.moving_left == self.moving_right:
            if self.momentum_x > 0:
                self.momentum_x = max(self.momentum_x - self.decceleration_x, 0)
            elif self.momentum_x < 0:
                self.momentum_x = min(self.momentum_x + self.decceleration_x, 0)

    def update(self):
        self.handle_momentum()
        self.rect.center = (self.rect.center[0] + self.momentum_x,
                            self.rect.center[1] + self.momentum_y)
        if (self.moving_left):
            self.image = self.run_left_sprites[round(self.animation_frame / self.animation_frame_max)]
            self.next_stand_animation = self.stand_sprites[0]
        elif (self.moving_right):
            self.image = self.run_right_sprites[round(self.animation_frame / self.animation_frame_max)]
            self.next_stand_animation = self.stand_sprites[1]
        else:
            if self.momentum_y == 0 and self.momentum_y == 0:
                self.image = self.next_stand_animation
        self.animation_frame = (self.animation_frame + 2) % self.animation_frame_max




    def move_up(self):
        self.moving_up = True
    def move_left(self):
        self.animation_frame = 0
        self.moving_left = True

    def move_down(self):
        self.moving_down = True

    def move_right(self):
        self.animation_frame = 0
        self.moving_right = True

    def move_stop_up(self):
        self.moving_up = False

    def move_stop_left(self):
        self.moving_left = False

    def move_stop_down(self):
        self.moving_down = False

    def move_stop_right(self):
        self.moving_right = False
