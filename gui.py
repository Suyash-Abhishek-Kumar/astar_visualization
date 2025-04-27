from astar import AStar
import colors
from buttons import Button
import pygame #type: ignore

pygame.init()

class GUI:
    def __init__(self, grid, src, dest):
        self.x, self.y = 600, 800
        self.screen = pygame.display.set_mode((self.x, self.y))
        pygame.display.set_caption("A* Pathfinding Algorithm")
        self.regular_font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        self.heading_font = pygame.font.Font(".\\fonts\\AstronBoyWonder.ttf", 36)
        self.grid = grid
        self.src = src
        self.dest = dest
        self.cell_size = 12
        self.path = []
        self.astar = None
        self.draw_mode = 3
        self.board_x = ((self.x // self.cell_size - len(grid[0])) // 2) * self.cell_size
        self.error_message = None
        self.width = len(grid[0]) * self.cell_size
        self.height = len(grid) * self.cell_size
        self.buttons = [
            Button(self.screen, (175, self.y // 2 + 150), 2, "Euclidian", self.euclidian_search, colors.BLACK, colors.update_brightness(colors.SKY_BLUE, 150), fixed_size=(100, 25)),
            Button(self.screen, (175, self.y // 2 + 185), 2, "Mannhatan", self.mannhatan_search, colors.BLACK, colors.update_brightness(colors.SKY_BLUE, 150), fixed_size=(100, 25)),
            Button(self.screen, (175, self.y // 2 + 250), 2, "Clear", self.clear, colors.BLACK, colors.update_brightness(colors.DARK_NAVY_BLUE, 150), fixed_size=(100, 25)),
            Button(self.screen, (175, self.y // 2 + 285), 2, "Reset Board", self.reset, colors.BLACK, colors.update_brightness(colors.DARK_NAVY_BLUE, 150), fixed_size=(100, 25))
        ]
        self.clock = pygame.time.Clock()
        self.last_click = pygame.time.get_ticks()
        self.click_wait = 500
        self.can_click = True
        self.running = True
    
    def euclidian_search(self):
        self.start('Euclidian')
    def mannhatan_search(self):
        self.start('Manhattan')
    def clear(self):
        self.path = []
    def reset(self):
        self.grid = [[0] * 30] + [[0] + [1] * 28 + [0] for _ in range(28)] + [[0] * 30]
        self.path = []

    def start(self, type):
        self.astar = AStar(self.grid, self.src, self.dest, heuristic_type=type, imported=True)
        x = self.astar.a_star_search()
        if x == -3:
            self.error_message = "Failed to find the destination cell"
        elif x == -2:
            self.error_message = "Source or the destination is blocked"
        elif x == -1:
            self.error_message = "Source or destination is invalid"
        else:
            self.error_message = None
            self.path = self.astar.trace_path()
    
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for i in self.buttons:
                            if i.collision_check():
                                i.function()
                        
            
            self.screen.fill(colors.update_brightness(colors.GRAY, 100))
            self.draw_scene()
            if self.can_click: self.input()
            self.mouse_input()
            for i in self.buttons:
                i.run()
            if self.error_message:
                self.draw_erro_log(self.error_message)
            self.cooldown()
            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
    
    def draw_erro_log(self, text):
        font = pygame.font.Font(None, 36)
        text_surface = font.render(text, True, colors.update_brightness(colors.RED, 125))
        text_rect = text_surface.get_rect(center=(self.x // 2, self.y - 25))
        self.screen.blit(text_surface, text_rect)

    def draw_text(self):
        heading = self.heading_font.render("A* Pathfinding Algorithm", True, colors.BLACK)
        heading_rect = heading.get_rect(center=(self.x // 2, 50))
        self.screen.blit(heading, heading_rect)

        pygame.draw.rect(self.screen, colors.LIGHT_GRAY, (self.x // 4 - 75, self.height + 125, self.x // 2 - 100, 250), 0, 15)
        pygame.draw.rect(self.screen, colors.LIGHT_GRAY, (3 *self.x // 4 - 125, self.height + 125, self.x // 2 - 100, 250), 0, 15)

        solve = self.small_font.render("Click to solve:", True, colors.BLACK)
        solve_rect = solve.get_rect(center=(self.x // 4 + 25, self.height + 100 + 50))
        self.screen.blit(solve, solve_rect)

        guide = self.small_font.render("Right click to draw:", True, colors.BLACK)
        guide_rect = guide.get_rect(center=(3 * self.x // 4 - 25, self.height + 100 + 50))
        self.screen.blit(guide, guide_rect)

        one = self.small_font.render("1 - Source", True, colors.BLACK)
        two = self.small_font.render("2 - Destination", True, colors.BLACK)
        three = self.small_font.render("3 - Wall", True, colors.BLACK)
        four = self.small_font.render("4 - Empty Space", True, colors.BLACK)
        
        one_rect = one.get_rect(topleft=(3 * self.x // 4 - 75, self.height + 100 + 50 + 50))
        two_rect = two.get_rect(topleft=(3 * self.x // 4 - 75, self.height + 100 + 50 + 75))
        three_rect = three.get_rect(topleft=(3 * self.x // 4 - 75, self.height + 100 + 50 + 100))
        four_rect = four.get_rect(topleft=(3 * self.x // 4 - 75, self.height + 100 + 50 + 125))

        self.screen.blit(one, one_rect)
        self.screen.blit(two, two_rect)
        self.screen.blit(three, three_rect)
        self.screen.blit(four, four_rect)

        pygame.draw.rect(self.screen, colors.update_brightness(colors.GREEN, -50), (3 * self.x // 4 - 105, self.height + 200, self.cell_size, self.cell_size))
        pygame.draw.rect(self.screen, colors.BLACK, (3 * self.x // 4 - 106, self.height + 199, self.cell_size + 2, self.cell_size + 2), 1)
        pygame.draw.rect(self.screen, colors.RED, (3 * self.x // 4 - 105, self.height + 225, self.cell_size, self.cell_size))
        pygame.draw.rect(self.screen, colors.BLACK, (3 * self.x // 4 - 106, self.height + 224, self.cell_size + 2, self.cell_size + 2), 1)
        pygame.draw.rect(self.screen, colors.BLACK, (3 * self.x // 4 - 105, self.height + 250, self.cell_size, self.cell_size))
        pygame.draw.rect(self.screen, colors.BLACK, (3 * self.x // 4 - 106, self.height + 249, self.cell_size + 2, self.cell_size + 2), 1)
        pygame.draw.rect(self.screen, colors.WHITE, (3 * self.x // 4 - 105, self.height + 275, self.cell_size, self.cell_size))
        pygame.draw.rect(self.screen, colors.BLACK, (3 * self.x // 4 - 106, self.height + 274, self.cell_size + 2, self.cell_size + 2), 1)

    def draw_scene(self):
        self.draw_text()
        
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                color = (255, 255, 255) if self.grid[i][j] == 1 else (0, 0, 0)
                if [i, j] == self.src:
                    pygame.draw.rect(self.screen, colors.update_brightness(colors.GREEN, -50), (j * self.cell_size + self.board_x, i * self.cell_size + 100, self.cell_size, self.cell_size))
                elif [i, j] == self.dest:
                    pygame.draw.rect(self.screen, colors.RED, (j * self.cell_size + self.board_x, i * self.cell_size + 100, self.cell_size, self.cell_size))
                elif (i, j) in self.path:
                    pygame.draw.rect(self.screen, colors.ROYAL_BLUE, (j * self.cell_size + self.board_x, i * self.cell_size + 100, self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(self.screen, color, (j * self.cell_size + self.board_x, i * self.cell_size + 100, self.cell_size, self.cell_size))
        pygame.draw.rect(self.screen, colors.GRAY, (0, self.y - 50, self.x, 50))
        
        # Testing for symmetry
        for i in range(len(self.grid)):
            pygame.draw.line(self.screen, colors.LIGHT_GRAY, (i * self.cell_size + self.board_x, 100), (i * self.cell_size + self.board_x, 100 + self.height), 1)
        for i in range(len(self.grid[0])):
            pygame.draw.line(self.screen, colors.LIGHT_GRAY, (self.board_x , i * self.cell_size + 100), (self.board_x + self.width, i * self.cell_size + 100), 1)
        pygame.draw.rect(self.screen, colors.BLACK, (self.board_x - self.cell_size, 100 - self.cell_size, self.width + 2 * self.cell_size, self.height + 2 * self.cell_size), 11)
    
    def input(self):
        keys = pygame.key.get_pressed()
        key = None
        if keys[pygame.K_1] or keys[pygame.K_KP1]:
            key = 1
        elif keys[pygame.K_2] or keys[pygame.K_KP2]:
            key = 2
        elif keys[pygame.K_3] or keys[pygame.K_KP3]:
            key = 3
        elif keys[pygame.K_4] or keys[pygame.K_KP4]:
            key = 4
        
        if key is not None:
            self.can_click = False
            self.draw_mode = key
            key = None
            self.last_click = pygame.time.get_ticks()
    
    def mouse_input(self):
        mouse = pygame.mouse.get_pressed()
        if mouse[2] == 1:
            mouse_pos = pygame.mouse.get_pos()
            for i in range(len(self.grid)):
                for j in range(len(self.grid[0])):
                    if self.board_x + j * self.cell_size < mouse_pos[0] < self.board_x + (j + 1) * self.cell_size and 100 + i * self.cell_size < mouse_pos[1] < 100 + (i + 1) * self.cell_size:
                        if self.draw_mode == 1:
                            self.src = [i, j]
                        elif self.draw_mode == 2:
                            self.dest = [i, j]
                        elif self.draw_mode == 3:
                            self.grid[i][j] = 0
                        else:
                            self.grid[i][j] = 1

    
    def cooldown(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_click >= self.click_wait:
            self.can_click = True

x = GUI([[0] * 30] + [[0] + [1] * 28 + [0] for _ in range(28)] + [[0] * 30], [2, 3], [26, 17])
x.run()