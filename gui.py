from astar import AStar
import pygame #type: ignore

pygame.init()

class GUI:
    def __init__(self, grid, src, dest):
        self.grid = grid
        self.src = src
        self.dest = dest
        self.cell_size = 40
        self.width = len(grid[0]) * self.cell_size
        self.height = len(grid) * self.cell_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("A* Pathfinding Algorithm")
        self.clock = pygame.time.Clock()
        self.running = True

    def draw_grid(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                color = (255, 255, 255) if self.grid[i][j] == 1 else (0, 0, 0)
                pygame.draw.rect(self.screen, color, (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size), 0)
                if [i, j] == self.src:
                    pygame.draw.rect(self.screen, (0, 255, 0), (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size), 0)
                elif [i, j] == self.dest:
                    pygame.draw.rect(self.screen, (255, 0, 0), (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size), 0)
    
    def run(self):
        astar = AStar(self.grid, self.src, self.dest, heuristic_type='Diagonal')
        astar.a_star_search()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.screen.fill((0, 0, 0))
            self.draw_grid()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

x = GUI([[1, 1, 1, 1, 1],
         [1, 0, 0, 0, 1],
         [1, 1, 1, 0, 1],
         [1, 0, 0, 0, 1],
         [1, 1, 1, 1, 1]], 
        [0, 0], [4, 4])
x.run()