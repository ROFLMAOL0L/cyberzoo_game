from entity import Entity
from pygame.image import load
from pygame.time import get_ticks
from pygame import Surface
from pygame.transform import scale
from VFX import VFX
class MainHero(Entity):
    def __init__(self, main_hero_group):
        super().__init__()
        self.sprite_sheet_128 = load("../sources/sprites/entities/main_hero/main_hero_sprites_128.png").convert_alpha()
        self.sprite_sheet_128_width = 6
        self.sprite_sheet_256 = load("../sources/sprites/entities/main_hero/main_hero_sprites_256.png").convert_alpha()
        self.sprite_sheet_256_width = 4
        # Attributes for animation and sprites
        self.stand_sprites = [(0, 0), (0, 1)]
        self.run_left_sprites = [(0, 2), (0, 3), (0, 4), (0, 5), (1, 0), (1, 1)]
        self.run_right_sprites = [(1, 2), (1, 3), (1, 4), (1, 5), (2, 0), (2, 1)]
        self.run_up_sprites = [(3,0), (3, 1), (3, 2), (3, 3), (3,0), (3, 2)]
        self.jump_left_sprites = [(2, 2), (2, 3)]
        self.jump_right_sprites = [(2, 4), (2, 5)]
        self.attack_left_sprites = [(0, 0), (0, 1), (0, 1)]
        self.attack_right_sprites = [(0, 2), (0, 3), (0, 3)]

        self.set_sprite_128(self.stand_sprites[0])
        self.rect = self.image.get_rect()
        self.pos = (1280 // 2, 720 // 2)
        self.rect.center = self.pos
        self.run_animation_frame = 0
        self.max_run_animation_frame = 5
        self.next_stand_animation = self.stand_sprites[0]
        self.last_animation_tick = get_ticks()
        self.face_direction = 0   # 0 - left, 1 - right, 2 - up

        self.is_in_jump = False
        self.jump_momentum = 0.0
        self.jump_acceleration = 1.0
        self.jump_starting_momentum = 17.0


        self.is_in_attack = False
        self.attack_animation_frame = 0
        self.max_attack_animation_frame = 2

        self.sword_attack_vfx_left = ["../sources/sprites/vfx/main_hero/main_hero_attack_left_vfx_1.png",
                                      "../sources/sprites/vfx/main_hero/main_hero_attack_left_vfx_2.png",
                                      "../sources/sprites/vfx/main_hero/main_hero_attack_left_vfx_2.png",
                                      "../sources/sprites/vfx/main_hero/main_hero_attack_left_vfx_3.png",
                                      "../sources/sprites/vfx/main_hero/main_hero_attack_left_vfx_3.png",
                                      "../sources/sprites/vfx/main_hero/main_hero_attack_left_vfx_4.png",
                                      "../sources/sprites/vfx/main_hero/main_hero_attack_left_vfx_4.png",
                                      "../sources/sprites/vfx/main_hero/main_hero_attack_left_vfx_5.png",
                                      "../sources/sprites/vfx/main_hero/main_hero_attack_left_vfx_5.png"
                                      ]
        self.sword_attack_vfx_right = ["../sources/sprites/vfx/main_hero/main_hero_attack_right_vfx_1.png",
                                      "../sources/sprites/vfx/main_hero/main_hero_attack_right_vfx_2.png",
                                      "../sources/sprites/vfx/main_hero/main_hero_attack_right_vfx_2.png",
                                      "../sources/sprites/vfx/main_hero/main_hero_attack_right_vfx_3.png",
                                      "../sources/sprites/vfx/main_hero/main_hero_attack_right_vfx_3.png",
                                      "../sources/sprites/vfx/main_hero/main_hero_attack_right_vfx_4.png",
                                      "../sources/sprites/vfx/main_hero/main_hero_attack_right_vfx_4.png",
                                      "../sources/sprites/vfx/main_hero/main_hero_attack_right_vfx_5.png",
                                      "../sources/sprites/vfx/main_hero/main_hero_attack_right_vfx_5.png"
                                      ]
        self.main_hero_group = main_hero_group

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
            self.apply_momentum()
        elif self.is_in_attack:
            self.handle_attack()
            self.apply_friction_x()
            self.apply_friction_y()
        else:
            self.apply_acceleration()
            self.apply_momentum()
            if (self.moving_down == self.moving_up):
                self.apply_friction_y()
            if(self.moving_left == self.moving_right):
                self.apply_friction_x()

    def handle_jump(self):
        # Apply gravity
        if self.jump_momentum - self.jump_acceleration > 0:
            self.jump_momentum -= self.jump_acceleration
        # Apply 1.5 gravity if falling
        elif self.jump_momentum - self.jump_acceleration * 1.5 > -self.jump_starting_momentum:
            self.jump_momentum -= self.jump_acceleration * 1.5
        else:
            self.additional_animation_pos = (self.additional_animation_pos[0], 0)
            self.jump_momentum = 0.0
            self.jump_end()
        # Add it to animation addition
        self.additional_animation_pos = (self.additional_animation_pos[0],
                                         self.additional_animation_pos[1] - self.jump_momentum)

    def handle_attack(self):
        pass

    def handle_animation(self):
        if self.is_in_jump:
            if self.moving_left and self.jump_momentum >= 0:
                self.set_sprite_128(self.jump_left_sprites[0])
            elif self.moving_left and self.jump_momentum < 0:
                self.set_sprite_128(self.jump_left_sprites[1])
            elif self.moving_right and self.jump_momentum >= 0:
                self.set_sprite_128(self.jump_right_sprites[0])
            elif self.moving_right and self.jump_momentum < 0:
                self.set_sprite_128(self.jump_right_sprites[1])
        elif self.is_in_attack:
            if self.face_direction == 0:
                self.set_sprite_256(self.attack_left_sprites[self.attack_animation_frame])
            elif self.face_direction == 1:
                self.set_sprite_256(self.attack_right_sprites[self.attack_animation_frame])
        elif (self.moving_left):
            self.set_sprite_128(self.run_left_sprites[self.run_animation_frame])
            self.next_stand_animation = self.stand_sprites[0]
            self.face_direction = 0
        elif (self.moving_right):
            self.set_sprite_128(self.run_right_sprites[self.run_animation_frame])
            self.next_stand_animation = self.stand_sprites[1]
            self.face_direction = 1
        elif (self.moving_up):
            self.set_sprite_128(self.run_up_sprites[self.run_animation_frame])
            self.next_stand_animation = self.stand_sprites[0]
            self.face_direction = 2
        else:
            if self.momentum_y == 0 and self.momentum_x == 0:
                self.set_sprite_128(self.next_stand_animation)
                self.run_animation_frame = 0
        # Move through anomation frames
        current_ticks = get_ticks()
        if current_ticks - self.last_animation_tick > 100:
            self.run_animation_frame = (self.run_animation_frame + 1) % self.max_run_animation_frame
            if self.is_in_attack:
                self.attack_animation_frame += 1
                if self.attack_animation_frame > self.max_attack_animation_frame:
                    self.stop_attack()
                    self.attack_animation_frame = 0
            self.last_animation_tick = current_ticks

    def set_sprite_128(self, index: tuple):
        self.image = Surface((128, 128)).convert_alpha()
        self.image.blit(self.sprite_sheet_128, (0, 0), (index[1] * 128,
                                                        index[0] * 128, 128, 128))
        self.image.set_colorkey((0, 0, 0))
    def set_sprite_256(self, index: tuple):
        self.image = Surface((256, 256)).convert_alpha()
        self.image.blit(self.sprite_sheet_256, (0, 0), (index[1] * 256,
                                                        index[0] * 256, 256, 256))
        self.image.set_colorkey((0, 0, 0))

    def move_up(self):
        self.moving_up = True

    def move_left(self):
        self.run_animation_frame = 0
        self.moving_left = True

    def move_down(self):
        self.moving_down = True

    def move_right(self):
        self.run_animation_frame = 0
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

    def attack(self):
        if self.is_in_attack:
            return
        self.is_in_attack = True
        self.attack_animation_frame = 0
        self.additional_animation_pos = (self.additional_animation_pos[0] - 128,
                                         self.additional_animation_pos[1] - 256)
        # Spawn a vfx
        if self.face_direction == 0:
            self.main_hero_group.add(VFX(self.sword_attack_vfx_left, (self.pos[0] - 192, self.pos[1] - 192)))
        elif self.face_direction == 1:
            self.main_hero_group.add(VFX(self.sword_attack_vfx_right, (self.pos[0] - 192, self.pos[1] - 192)))

    def stop_attack(self):
        if self.is_in_attack:
            self.is_in_attack = False
            self.additional_animation_pos = (self.additional_animation_pos[0] + 128,
                                             self.additional_animation_pos[1] + 256)
