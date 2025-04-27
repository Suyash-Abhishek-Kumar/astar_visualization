import math
import heapq

ROW = 9
COL = 10
ROOT2 = math.sqrt(2)

class Cell:
    def __init__(self):
        self.parent_i = 0
        self.parent_j = 0
        self.f = float('inf')  # Total cost (g + h)
        self.g = float('inf')  # Cost from start to this node
        self.h = 0  # Heuristic cost from this node to goal


class AStar:
    def __init__(self, grid, start, dest, heuristic_type='Euclidean', imported=False):
        self.imported = imported
        self.grid = grid
        self.ROW = len(grid) if imported else ROW
        self.COL = len(grid[0]) if imported else COL
        self.src = start
        self.dest = dest
        self.heuristic_type = heuristic_type
        self.found_dest = False
        self.open_list = []  # List of cells to be evaluated
        self.closed_list = []  # List of cells already evaluated
        self.cell_details = []  # Details of each cell

    # Check if given point is in the grid
    def is_valid(self, row, col): return (row >= 0) and (row < self.ROW) and (col >= 0) and (col < self.COL)

    # check if the given node is unblocked
    def is_unblocked(self, row, col): return self.grid[row][col] == 1

    # Check if a cell is the destination
    def is_destination(self, row, col): return row == self.dest[0] and col == self.dest[1]

    # Calculate the heuristic value of a cell (Euclidean/Manhattan/Diagonal distance to destination)
    def calculate_h_value(self, row, col):
        if self.heuristic_type == 'Manhattan':
            return abs(row - self.dest[0]) + abs(col - self.dest[1])
        elif self.heuristic_type == 'Diagonal':
            return ((row - self.dest[0]) + (col - self.dest[1])) + (ROOT2 - 2 * 1) * min((row - self.dest[0]), (col - self.dest[1]))
        else:  # Default to Euclidean
            return math.sqrt((row - self.dest[0]) ** 2 + (col - self.dest[1]) ** 2)
        
    # Trace the path from source to destination
    def trace_path(self, cell_details):
        if not self.imported: print("The Path is ")
        path = []
        row = self.dest[0]
        col = self.dest[1]

        # Trace the path from destination to source using parent cells
        while not (cell_details[row][col].parent_i == row and cell_details[row][col].parent_j == col):
            path.append((col, row))
            temp_row = cell_details[row][col].parent_i
            temp_col = cell_details[row][col].parent_j
            row = temp_row
            col = temp_col

        # Add the source cell to the path
        path.append((col, row))
        # Reverse the path to get the path from source to destination
        path.reverse()

        # Print the path
        if not self.imported:
            for i in path: print("->", i, end=" ")
            print()
    
    # Implement the A* search algorithm
    def a_star_search(self):
        # Check if the source and destination are valid
        if not self.is_valid(self.src[0], self.src[1]) or not self.is_valid(self.dest[0], self.dest[1]):
            if not self.imported:
                print("Source or destination is invalid")
                return
            else: return -1

        # Check if the source and destination are unblocked
        if not self.is_unblocked(self.src[0], self.src[1]) or not self.is_unblocked(self.dest[0], self.dest[1]):
            if not self.imported:
                print("Source or the destination is blocked")
                return
            else: return -2

        # Check if we are already at the destination
        if self.is_destination(self.src[0], self.src[1]):
            if not self.imported:
                print("We are already at the destination")
                return
            else: return 0

        # Initialize the closed list (visited cells)
        self.closed_list = [[False for _ in range(self.COL)] for _ in range(self.ROW)]
        # Initialize the details of each cell
        self.cell_details = [[Cell() for _ in range(self.COL)] for _ in range(self.ROW)]

        # Initialize the start cell details
        i = self.src[0]
        j = self.src[1]
        self.cell_details[i][j].f = 0
        self.cell_details[i][j].g = 0
        self.cell_details[i][j].h = 0
        self.cell_details[i][j].parent_i = i
        self.cell_details[i][j].parent_j = j

        # Initialize the open list (cells to be visited) with the start cell
        heapq.heappush(self.open_list, (0.0, i, j))

         # Main loop of A* search algorithm
        while len(self.open_list) > 0:
            # Pop the cell with the smallest f value from the open list
            p = heapq.heappop(self.open_list)

            # Mark the cell as visited
            i, j = p[1], p[2]
            self.closed_list[i][j] = True

            # For each direction, check the successors
            if self.heuristic_type == 'Manhattan':
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            else:
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
            for dir in directions:
                new_i = i + dir[0]
                new_j = j + dir[1]

                 # If the successor is valid, unblocked, and not visited
                if self.is_valid(new_i, new_j) and self.is_unblocked(new_i, new_j) and not self.closed_list[new_i][new_j]:
                    # If the successor is the destination
                    if self.is_destination(new_i, new_j):
                        # Set the parent of the destination cell
                        self.cell_details[new_i][new_j].parent_i = i
                        self.cell_details[new_i][new_j].parent_j = j
                        if not self.imported:
                            print("The destination cell is found")
                            # Trace and print the path from source to destination
                            self.trace_path(self.cell_details)
                            self.found_dest = True
                            return
                        else:
                            return 0
                    else:
                        # Calculate the new f, g, and h values
                        g_new = self.cell_details[i][j].g + 1.0
                        h_new = self.calculate_h_value(new_i, new_j)
                        f_new = g_new + h_new

                        # If the cell is not in the open list or the new f value is smaller
                        if self.cell_details[new_i][new_j].f == float('inf') or self.cell_details[new_i][new_j].f > f_new:
                            # Add the cell to the open list
                            heapq.heappush(self.open_list, (f_new, new_i, new_j))
                            # Update the cell details
                            self.cell_details[new_i][new_j].f = f_new
                            self.cell_details[new_i][new_j].g = g_new
                            self.cell_details[new_i][new_j].h = h_new
                            self.cell_details[new_i][new_j].parent_i = i
                            self.cell_details[new_i][new_j].parent_j = j

        # If the destination is not found after visiting all cells
        if not self.found_dest:
            if not self.imported:
                print("Failed to find the destination cell")
                return
            else: return -3

def main():
    # Define the grid (1 for unblocked, 0 for blocked)
    grid = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]
    ]

    # Define the source and destination
    src = [8, 0]
    dest = [0, 0]

    # Run the A* search algorithm
    astar = AStar(grid, src, dest, heuristic_type='Diagonal')
    astar.a_star_search()

if __name__ == "__main__":
    main()