from lowLevelUtilities import read_config

SCREEN_CONFIG_PATH="../config/screen.config"
class ScreenSettings:
    def __init__(self):
        settings_dict = read_config(SCREEN_CONFIG_PATH)
        self.width = int(settings_dict['screen_width'])
        self.height = int(settings_dict['screen_height'])
        self.fps = int(settings_dict['screen_fps'])
