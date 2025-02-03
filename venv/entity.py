from pygame.sprite import Sprite
class Entity(Sprite):
    def __init__(self):
        super().__init__()
        # Default attributes for all entities
        self.pos = (0, 0)
        self.acceleration = 2.0
        self.decceleration = 1.0
        self.momentum_x, self.momentum_y = 0.0, 0.0
        self.max_momentum = 8.0
        # Used for animation purposes only
        self.additional_animation_pos = (0.0, 0.0)

        self.moving_up = False
        self.moving_left = False
        self.moving_down = False
        self.moving_right = False

    def update(self):
        self.handle_momentum()
        self.rect_update()

    def rect_update(self):
        self.rect.center = (self.rect.center[0] + self.momentum_x + self.additional_animation_pos[0],
                            self.rect.center[1] + self.axis_adjustment(self.momentum_y + self.additional_animation_pos[1]))

    def handle_momentum(self):
        # Add momentum since button is pressed
        if self.moving_up:
            self.momentum_y = max(self.momentum_y - self.acceleration, -self.max_momentum)
        if self.moving_down:
            self.momentum_y = min(self.momentum_y + self.acceleration, self.max_momentum)
        if self.moving_left:
            self.momentum_x = max(self.momentum_x - self.acceleration, -self.max_momentum)
        if self.moving_right:
            self.momentum_x = min(self.momentum_x + self.acceleration, self.max_momentum)
        # Start stopping if opposite buttons pressed
        if self.moving_down == self.moving_up:
            if self.momentum_y > 0:
                self.momentum_y = max(self.momentum_y - self.decceleration, 0)
            elif self.momentum_y < 0:
                self.momentum_y = min(self.momentum_y + self.decceleration, 0)
        if self.moving_left == self.moving_right:
            if self.momentum_x > 0:
                self.momentum_x = max(self.momentum_x - self.decceleration, 0)
            elif self.momentum_x < 0:
                self.momentum_x = min(self.momentum_x + self.decceleration, 0)

    def axis_adjustment(self, momentum_y):
        return momentum_y * 0.5
