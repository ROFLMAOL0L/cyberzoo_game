from pygame import KEYDOWN, KEYUP, K_w, K_a, K_s, K_d, K_SPACE, MOUSEBUTTONDOWN, JOYDEVICEADDED
from pygame.mouse import get_pressed, get_pos
from pygame.joystick import Joystick

class Controls:
    def __init__(self, events):
        self.using_joystic = False
        for event in events:
            if event.type == JOYDEVICEADDED:
                self.joystic = Joystick(event.device_index)
                self.using_joystic = True
    def handle_controls(self, event, main_hero):   # how the f*ck does it even work????
        if self.using_joystic:
            pass
        else:
            if event.type == KEYDOWN:
                if event.key == K_w:
                    main_hero.move_up()
                if event.key == K_a:
                    main_hero.move_left()
                if event.key == K_s:
                    main_hero.move_down()
                if event.key == K_d:
                    main_hero.move_right()
                if event.key == K_SPACE:
                    main_hero.jump()
            if event.type == KEYUP:
                if event.key == K_w:
                    main_hero.move_stop_up()
                if event.key == K_a:
                    main_hero.move_stop_left()
                if event.key == K_s:
                    main_hero.move_stop_down()
                if event.key == K_d:
                    main_hero.move_stop_right()
            if event.type == MOUSEBUTTONDOWN:
                mouse_pressed = get_pressed()
                if mouse_pressed[0]:
                    main_hero.attack()
                elif mouse_pressed[2]:
                    main_hero.dash_start()
