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
        self.rect.center = (self.pos[0] + self.momentum_x + self.additional_animation_pos[0],
                            self.pos[1] + self.axis_adjustment(self.momentum_y + self.additional_animation_pos[1]))

    def handle_momentum(self):
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
        self.pos = (self.pos[0] + self.momentum_x, self.pos[1] + self.momentum_y)

    """
    The reason for getting those lines out of "handle_momentum()" is because the acceleration litteraly means an entity
    is moving, while "handle_movement" is more about physics of the movements. For example, when a player attacks he
    does interrupt his movement, thus not being able to move while attack animation is not over, although the 
    decceleration effects have to continue, otherwise hitting attack while running will instantly make the player stop.
    """
    def apply_acceleration(self):
        # Add momentum since button is pressed
        if self.moving_up:
            self.momentum_y = max(self.momentum_y - self.acceleration, -self.max_momentum)
        if self.moving_down:
            self.momentum_y = min(self.momentum_y + self.acceleration, self.max_momentum)
        if self.moving_left:
            self.momentum_x = max(self.momentum_x - self.acceleration, -self.max_momentum)
        if self.moving_right:
            self.momentum_x = min(self.momentum_x + self.acceleration, self.max_momentum)

    def axis_adjustment(self, momentum_y):
        return momentum_y * 0.5
