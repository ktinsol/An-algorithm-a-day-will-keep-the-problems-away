import math


class AStarPathfinder:

    def __init__(self):
        self.grid = None
        self.start_node = None
        self.end_node = None
        self.open_list = []
        self.closed_list = []
        self.on_add_to_open_list = None
        self.on_select_next_node = None

    def set_grid(self, grid):
        self.grid = grid

    def create_nodes(self):
        rows, cols = 10, 10
        self.grid = [[Node(j, i) for i in range(rows)] for j in range(cols)]

    # Could be reworked to start node = array
    def select_start_node(self, row, col):
        print("Start: " + str(row) + ", " + str(col))
        self.start_node = self.grid[row][col]
        # self.grid[row][col] = self.start_node

    def select_end_node(self, row, col):
        self.end_node = self.grid[row][col]
        # self.grid[row][col] = self.end_node

    def init_the_algo(self):
        self.open_list.append(self.start_node)
        self.start_node.g = 0
        self.start_node.h = self.start_node.calculate_h(self.end_node.index_0, self.end_node.index_1)
        self.start_node.f = self.start_node.g + self.start_node.h
        self.start_node.parent_node = None
        if self.on_add_to_open_list:
            self.on_add_to_open_list(self.start_node)

    def find_best_path(self):
        while self.open_list:
            current_node = AStarPathfinder.find_node_with_min_f(self.open_list)

            print(str(current_node.index_0) + ", " + str(current_node.index_1))
            if current_node == self.end_node:
                print("Hello")
                return AStarPathfinder.reconstruct_best_path(current_node)

            if self.on_select_next_node:
                self.on_select_next_node(current_node)

            self.closed_list.append(current_node)
            self.open_list.remove(current_node)

            neighbors = self.find_neighbors(current_node)
            for neighbor in neighbors:
                if neighbor in self.closed_list:
                    continue
                tentative_g = AStarPathfinder.calculate_tentative_g(current_node, neighbor)
                if neighbor not in self.open_list:
                    self.open_list.append(neighbor)
                    neighbor.update_values(tentative_g, self.end_node)
                    neighbor.parent_node = current_node
                    if self.on_add_to_open_list:
                        self.on_add_to_open_list(neighbor)
                elif neighbor in self.open_list and tentative_g < neighbor.g:
                    neighbor.update_values(tentative_g, self.end_node)
                    neighbor.parent_node = current_node

        return None

    @staticmethod
    def reconstruct_best_path(node):
        best_path = [node]
        current_node = node.parent_node
        while current_node.parent_node is not None:
            best_path.append(current_node)
            current_node = current_node.parent_node
        if current_node.parent_node is None:
            best_path.append(current_node)
        return best_path

    def find_neighbors(self, node):
        neighbors = []
        row, col = node.index_0, node.index_1
        rows, cols = len(self.grid), len(self.grid[0])

        # Define all 8 possible movements (including diagonals)
        directions = [
            (-1, 0), (1, 0),  # Up, Down
            (0, -1), (0, 1),  # Left, Right
            (-1, -1), (-1, 1),  # Up-Left, Up-Right
            (1, -1), (1, 1)  # Down-Left, Down-Right
        ]

        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols:  # Check if within bounds
                if self.grid[nr][nc].is_wall is False:
                    neighbors.append(self.grid[nr][nc])

        return neighbors

    @staticmethod
    def calculate_tentative_g(current_node, neighbor_node):
        """
        # Calculate the tentative g cost from current_node to neighbor_node
        dx = abs(current_node.index_0 - neighbor_node.index_0)
        dy = abs(current_node.index_1 - neighbor_node.index_1)
        if dx == 1 and dy == 1:  # Diagonal movement
            return current_node.g + math.sqrt(2)
        else:  # Horizontal or vertical movement
            return current_node.g + 1
        """
        return current_node.g + 1

    @staticmethod
    def find_node_with_min_f(list_of_nodes):
        node_with_min_f = list_of_nodes[0]
        min_f = node_with_min_f.f
        for node in list_of_nodes:
            if node.f < min_f:
                min_f = node.f
                node_with_min_f = node
        return node_with_min_f


class Node:

    def __init__(self, index_0, index_1):
        self.index_0 = index_0
        self.index_1 = index_1
        self.g = 0
        self.h = 0
        self.f = 0
        self.parent_node = None
        self.is_start = False
        self.is_end = False
        self.is_wall = False
        # print(self.index_0, self.index_1)

    def calculate_h(self, node_index_0, node_index_1):
        return abs(self.index_0 - node_index_0) + abs(self.index_1 - node_index_1)

    def calculate_f(self):
        return self.g + self.h

    def update_values(self, g, node):
        self.g = g
        self.h = self.calculate_h(node.index_0, node.index_1)
        self.f = self.calculate_f()
