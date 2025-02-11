from pygame.sprite import Sprite
from lowLevelUtilities import vector_value
class Entity(Sprite):
    def __init__(self):
        super().__init__()
        # Default attributes for all entities
        self.pos = (0, 0)
        self.momentum = (0.0, 0.0)
        self.max_momentum_value = 1.2
        self.acceleration = 0.2
        self.decceleration = self.acceleration * 1.5
        self.momentum_multiplier = 8.0
        self.is_joystic_controlled = False
        # Used for animation purposes only
        self.additional_animation_pos = (0.0, 0.0)

        self.moving_up = False
        self.moving_left = False
        self.moving_down = False
        self.moving_right = False

    def rect_update(self):
        self.rect.center = (self.pos[0] + self.additional_animation_pos[0],
                            self.pos[1] + self.additional_animation_pos[1])

    def apply_friction_y(self):
        if self.momentum[1] > 0:
            self.momentum = (self.momentum[0], max(self.momentum[1] - self.decceleration, 0.0))
        elif self.momentum[1] < 0:
            self.momentum = (self.momentum[0], min(self.momentum[1] + self.decceleration, 0.0))

    def apply_friction_x(self):
        if self.momentum[0] > 0:
            self.momentum = (max(self.momentum[0] - self.decceleration, 0.0), self.momentum[1])
        elif self.momentum[0] < 0:
            self.momentum = (min(self.momentum[0] + self.decceleration, 0.0), self.momentum[1])

    def apply_momentum(self):
        self.pos = (self.pos[0] + self.momentum[0] * self.momentum_multiplier,
                    self.pos[1] + self.axis_adjustment(self.momentum[1] * self.momentum_multiplier))

    """
    The reason for getting those lines out of "handle_momentum()" is because the acceleration litteraly means an entity
    is moving, while "handle_movement" is more about physics of the movements. For example, when a player attacks he
    does interrupt his movement, thus not being able to move while attack animation is not over, although the 
    decceleration effects have to continue, otherwise hitting attack while running will instantly make the player stop.
    """
    def apply_acceleration(self):
        if self.is_joystic_controlled:
            pass
        else:
            # Add momentum since button is pressed
            if self.moving_up:
                self.momentum = (self.momentum[0], self.momentum[1] - self.acceleration)
            if self.moving_down:
                self.momentum = (self.momentum[0], self.momentum[1] + self.acceleration)
            if self.moving_left:
                self.momentum = (self.momentum[0] - self.acceleration, self.momentum[1])
            if self.moving_right:
                self.momentum = (self.momentum[0] + self.acceleration, self.momentum[1])
            self.cut_momentum()

    def cut_momentum(self):
        vv = vector_value(self.momentum)
        if vv > self.max_momentum_value:
            delta = self.max_momentum_value / vv
            self.momentum = (self.momentum[0] * delta, self.momentum[1] * delta)

    def move(self, dx, dy):
        self.pos = (self.pos[0] + dx, self.pos[1] + dy)

    def axis_adjustment(self, momentum_y):
        return momentum_y * 1.0
