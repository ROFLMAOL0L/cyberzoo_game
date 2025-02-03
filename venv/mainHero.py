from entity import Entity
from pygame.image import load
from pygame.time import get_ticks
class MainHero(Entity):
    def __init__(self):
        super().__init__()

        # Attributes for animation and sprites
        self.stand_sprites = []
        self.stand_sprites.append(load("../sources/sprites/entities/main_hero/main_hero_stand_left_1.png"))
        self.stand_sprites.append(load("../sources/sprites/entities/main_hero/main_hero_stand_right_1.png"))
        self.run_left_sprites = []
        self.run_left_sprites.append(load("../sources/sprites/entities/main_hero/main_hero_run_left_1.png"))
        self.run_left_sprites.append(load("../sources/sprites/entities/main_hero/main_hero_run_left_2.png"))
        self.run_left_sprites.append(load("../sources/sprites/entities/main_hero/main_hero_run_left_3.png"))
        self.run_left_sprites.append(load("../sources/sprites/entities/main_hero/main_hero_run_left_4.png"))
        self.run_left_sprites.append(load("../sources/sprites/entities/main_hero/main_hero_run_left_5.png"))
        self.run_left_sprites.append(load("../sources/sprites/entities/main_hero/main_hero_run_left_6.png"))
        self.run_right_sprites = []
        self.run_right_sprites.append(load("../sources/sprites/entities/main_hero/main_hero_run_right_1.png"))
        self.run_right_sprites.append(load("../sources/sprites/entities/main_hero/main_hero_run_right_2.png"))
        self.run_right_sprites.append(load("../sources/sprites/entities/main_hero/main_hero_run_right_3.png"))
        self.run_right_sprites.append(load("../sources/sprites/entities/main_hero/main_hero_run_right_4.png"))
        self.run_right_sprites.append(load("../sources/sprites/entities/main_hero/main_hero_run_right_5.png"))
        self.run_right_sprites.append(load("../sources/sprites/entities/main_hero/main_hero_run_right_6.png"))
        self.jump_right_sprites = []
        self.jump_right_sprites.append(load("../sources/sprites/entities/main_hero/main_hero_jump_right_1.png"))
        self.jump_right_sprites.append(load("../sources/sprites/entities/main_hero/main_hero_jump_right_2.png"))
        self.jump_left_sprites = []
        self.jump_left_sprites.append(load("../sources/sprites/entities/main_hero/main_hero_jump_left_1.png"))
        self.jump_left_sprites.append(load("../sources/sprites/entities/main_hero/main_hero_jump_left_2.png"))
        self.image = self.stand_sprites[0]
        self.rect = self.image.get_rect()
        self.rect.center = (1280 // 2, 720 // 2)
        self.run_animation_frame = 0
        self.max_run_animation_frame = 5
        self.next_stand_animation = self.image
        self.last_animation_tick = get_ticks()

        self.is_in_jump = False
        self.jump_momentum = 0.0
        self.jump_acceleration = 1.0
        self.jump_starting_momentum = 20.0

    def update(self):
        # Handle momentum according to the keys pressed
        self.handle_controls()
        # Change the position according to momentum
        self.rect_update()
        # Animate
        self.handle_animation()

    def handle_controls(self):
        # Handle jump if jumped
        if self.is_in_jump:
            self.handle_jump()
        else:
            self.handle_momentum()

    def handle_jump(self):
        # Apply gravity
        if self.jump_momentum - self.jump_acceleration > 0:
            self.jump_momentum -= self.jump_acceleration
        # Apply 1.5 gravity if falling
        elif self.jump_momentum - self.jump_acceleration > -self.jump_starting_momentum:
            self.jump_momentum -= self.jump_acceleration * 1.5
        else:
            self.jump_momentum = 0.0
            self.jump_end()
        # Add it to animation addition
        self.additional_animation_pos = (self.additional_animation_pos[0], -self.jump_momentum)

    def handle_animation(self):
        if self.is_in_jump:
            if self.moving_left and self.jump_momentum >= 0:
                self.image = self.jump_left_sprites[0]
            elif self.moving_left and self.jump_momentum < 0:
                self.image = self.jump_left_sprites[1]
            elif self.moving_right and self.jump_momentum >= 0:
                self.image = self.jump_right_sprites[0]
            elif self.moving_right and self.jump_momentum < 0:
                self.image = self.jump_right_sprites[1]
        elif (self.moving_left):
            self.image = self.run_left_sprites[self.run_animation_frame]
        elif (self.moving_right):
            self.image = self.run_right_sprites[self.run_animation_frame]
        else:
            if self.momentum_y == 0 and self.momentum_x == 0:
                self.image = self.next_stand_animation
                self.animation_frame = 0
        if self.moving_left:
            self.next_stand_animation = self.stand_sprites[0]
        elif self.moving_right:
            self.next_stand_animation = self.stand_sprites[1]
        # Move through anomation frames
        current_ticks = get_ticks()
        if current_ticks - 100 > self.last_animation_tick:
            self.run_animation_frame = (self.run_animation_frame + 1) % self.max_run_animation_frame
            self.last_animation_tick = current_ticks

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

    def jump(self):
        if not self.is_in_jump:
            self.is_in_jump = True
            self.jump_momentum = self.jump_starting_momentum

    def jump_end(self):
        self.is_in_jump = False
