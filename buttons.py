import pygame # type: ignore
import colors

class Button:
    def __init__(self, screen, loc, width, name, func, text_color = colors.BLACK, button_color = colors.WHITE, button_img = None, fixed_size = None, tiny = False, hover = "highlight"):
        self.regular_font = pygame.font.Font(".\\fonts\\basic_types\\Roboto-Medium.ttf", 16)
        self.tiny_font = pygame.font.Font(".\\fonts\\basic_types\\Roboto-Medium.ttf", 8)
        self.screen = screen
        self.location = loc
        self.width = width
        self.bold_width = self.width + 2
        self.width_copy = width
        self.button_color = button_color
        self.hover = hover
        self.neg = False
        self.back_color = colors.update_brightness(button_color, -min(50, min(button_color)))
        if not tiny:
            self.name = self.regular_font.render(name, False, text_color)
            self.name_negative = self.regular_font.render(name, False, colors.negative(text_color))
        else:
            self.name = self.tiny_font.render(name, False, text_color)
            self.name_negative = self.tiny_font.render(name, False, colors.negative(text_color))
        self.name_rect = self.name.get_rect()

        if fixed_size:
            self.box_rect = pygame.Rect(loc, fixed_size)
        else:
            self.box_rect = pygame.Rect(loc, (self.name_rect.size[0] + 15, self.name_rect.size[1] + 2))

        self.name_size = self.name_rect.size
        self.name_rect.center = self.location
        self.box_rect.center = self.name_rect.center
        self.function = func
        self.img = None
        if button_img:
            self.img = button_img
            self.box_rect.size = (self.box_rect.size[0] + 17, self.box_rect.size[1] + 2)
            self.box_rect.center = self.name_rect.center
            self.img = pygame.transform.smoothscale(self.img, self.box_rect.size)

    def run(self):
        self.collision_check()
        if self.img:
            self.screen.blit(self.img, self.box_rect)
        else:
            pygame.draw.rect(self.screen, self.back_color, self.box_rect, border_radius=7)
            if self.hover == "darken" and self.width == -1:
                pygame.draw.rect(self.screen, self.button_color, self.box_rect, 0, border_radius=7)
            if self.hover == "highlight":
                pygame.draw.rect(self.screen, self.button_color, self.box_rect, self.width, border_radius=7)
        if self.neg:
            self.screen.blit(self.name_negative, self.name_rect)
        else:
            self.screen.blit(self.name, self.name_rect)

    def collision_check(self):
        mouse_pos = pygame.mouse.get_pos()
        if abs(mouse_pos[0] - self.location[0]) < self.box_rect.size[0] // 2 and abs(
                mouse_pos[1] - self.location[1]) < self.box_rect.size[1] // 2:
            if self.img:
                pygame.draw.rect(self.screen, pygame.Color(200, 200, 200, a = 255), self.box_rect, 0, 10)
            else:
                if self.hover == "highlight":
                    self.width = self.bold_width
                elif self.hover == "darken":
                    self.width = -1
                    self.neg = True
            return True
        else:
            if not self.img:
                self.width = self.width_copy
                self.neg = False
            return False
        
