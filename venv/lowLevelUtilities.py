from math import atan, pi, sin, cos, sqrt, pow
def read_config(path: str) -> dict:
    out_dict = {}
    with open(path, "r") as config_file:
        for config_line in config_file:
            out_dict[config_line.split(" = ")[0]] = config_line.split(" = ")[1][:-1]
    return out_dict

def get_angle(dx, dy):
    if dx == 0 and dy == 0:
        return -1
    if dx > 0:
        if dy > 0:
            return atan(dy / dx) / pi * 180
        else:
            return 360 + atan(dy / dx) / pi * 180
    else:
        if dy > 0:
            if dx == 0:
                return 90.0
            return 180 + atan(dy / dx) / pi * 180
        else:
            if dx == 0:
                return 270
            return 180 + atan(dy / dx) / pi * 180

def get_sin(angle):
    if angle == -1:
        return 0
    return sin(angle / 180 * pi)

def get_cos(angle):
    if angle == -1:
        return 0
    return cos(angle / 180 * pi)

def vector_value(vector: tuple):
    return sqrt(pow(vector[0], 2) + pow(vector[1], 2))
