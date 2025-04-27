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
        self.grid = grid
        self.src = src
        self.dest = dest
        self.cell_size = 12
        self.path = []
        self.board_x = ((self.x // self.cell_size - len(grid[0])) // 2) * self.cell_size
        self.error_message = "Failed to find the destination cell"
        self.width = len(grid[0]) * self.cell_size
        self.height = len(grid) * self.cell_size
        self.astar = AStar(self.grid, self.src, self.dest, heuristic_type='Euclidian', imported=True)
        self.buttons = [Button(self.screen, (self.x // 2, self.y // 2 + 250), 2, "Start", self.start, colors.BLACK, colors.LIGHT_GRAY)]
        self.clock = pygame.time.Clock()
        self.running = True
    
    def start(self):
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
        print("Found", self.path)
    
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
            
            self.screen.fill(colors.update_brightness(colors.GRAY, 115))
            self.draw_grid()
            for i in self.buttons:
                i.run()
            if self.error_message:
                self.draw_erro_log(self.error_message)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
    
    def draw_erro_log(self, text):
        font = pygame.font.Font(None, 36)
        text_surface = font.render(text, True, colors.update_brightness(colors.RED, -50))
        text_rect = text_surface.get_rect(center=(self.x // 2, self.y - 25))
        self.screen.blit(text_surface, text_rect)

    def draw_grid(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                color = (255, 255, 255) if self.grid[i][j] == 1 else (0, 0, 0)
                if [i, j] == self.src:
                    pygame.draw.rect(self.screen, (0, 255, 0), (j * self.cell_size + self.board_x, i * self.cell_size + 100, self.cell_size, self.cell_size))
                elif [i, j] == self.dest:
                    pygame.draw.rect(self.screen, (255, 0, 0), (j * self.cell_size + self.board_x, i * self.cell_size + 100, self.cell_size, self.cell_size))
                elif (i, j) in self.path:
                    pygame.draw.rect(self.screen, (0, 0, 255), (j * self.cell_size + self.board_x, i * self.cell_size + 100, self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(self.screen, color, (j * self.cell_size + self.board_x, i * self.cell_size + 100, self.cell_size, self.cell_size))
        pygame.draw.rect(self.screen, colors.GRAY, (0, self.y - 50, self.x, 50))
        
        # Testing for symmetry
        for i in range(len(self.grid)):
            pygame.draw.line(self.screen, colors.LIGHT_GRAY, (i * self.cell_size + self.board_x, 100), (i * self.cell_size + self.board_x, 100 + self.height), 1)
        for i in range(len(self.grid[0])):
            pygame.draw.line(self.screen, colors.LIGHT_GRAY, (self.board_x , i * self.cell_size + 100), (self.board_x + self.width, i * self.cell_size + 100), 1)
        pygame.draw.rect(self.screen, colors.BLACK, (self.board_x - self.cell_size, 100 - self.cell_size, self.width + 2 * self.cell_size, self.height + 2 * self.cell_size), 11)

x = GUI([[0] * 30] + [[0] + [1] * 28 + [0]] * 28 + [[0] * 30], [2, 3], [26, 17])
x.run()