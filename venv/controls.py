from pygame import KEYDOWN, KEYUP, K_w, K_a, K_s, K_d, K_SPACE, MOUSEBUTTONDOWN, JOYDEVICEADDED
from pygame.mouse import get_pressed, get_pos
from pygame.joystick import Joystick
from lowLevelUtilities import get_angle, get_sin, get_cos

class Controls:
    def __init__(self, events):
        self.using_joystic = False
        for event in events:
            if event.type == JOYDEVICEADDED:
                self.joystic = Joystick(event.device_index)
                self.using_joystic = True
    def handle_controls(self, event, main_hero):   # how the f*ck does it even work????
        if self.using_joystic:
            #main_hero.move(get_sin(get_atan(self.joystic.get_axis(0), self.joystic.get_axis(1))), 0)
            stick_angle = get_angle(self.joystic.get_axis(0), -self.joystic.get_axis(1))
            if stick_angle != 0:
                dx, dy = get_cos(stick_angle) * abs(self.joystic.get_axis(0)), \
                    get_sin(stick_angle) * abs(self.joystic.get_axis(1))
                main_hero.move(dx, dy)
                '''
                if dx > 0:
                    main_hero.move_right()
                    main_hero.move_stop_left()
                elif dx < 0:
                    main_hero.move_left()
                    main_hero.move_stop_right()
                else:
                    main_hero.move_stop_right()
                    main_hero.move_stop_left()
                if dy > 0:
                    main_hero.move_up()
                    main_hero.move_stop_down()
                elif dy < 0:
                    main_hero.move_down()
                    main_hero.move_stop_up()
                else:
                    main_hero.move_stop_down()
                    main_hero.move_stop_up()
                    '''
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
