BLACK = (0, 0, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
BLUE = (0, 0, 255)
SKY_BLUE = (0, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
ROYAL_BLUE = (100, 150, 255)
DARK_NAVY_BLUE = (30, 30, 46)
PINK = (255, 155, 205)
GRAY = (127, 127, 127)
LIGHT_GRAY = (200, 200, 200)
ORANGE = (255, 155, 0)
color = [0, 0, 255]
cur = [0, 1]
new_color = {}
    
def scrolling(speed: int):
    for i in range(len(color)):
        if i == cur[0]: color[i] = min(255, color[i] + speed)
        elif i == cur[1]: color[i] = max(0, color[i] - speed)
        else: pass
        if color.count(255) == 2 and color.count(0) == 1:
            cur[0] = (cur[0] + 1) % 3
            cur[1] = (cur[1] + 1) % 3
    return color

def update_brightness(color: list, value: int) -> list:
    if value > 255:
        return WHITE
    new_color = [0, 0, 0]
    for i in range(3):
        new_color[i] = max(0, min(255, color[i] + value))
    return tuple(new_color)

def negative(color: list) -> list:
    new_color = [0, 0, 0]
    for i in range(3):
        new_color[i] = 255 - color[i]
    return tuple(new_color)