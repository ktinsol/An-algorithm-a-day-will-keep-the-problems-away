import math


class AStarPathfinder:

    def __init__(self):
        self.nodes = None
        self.start_node = None
        self.end_node = None
        self.open_list = []
        self.closed_list = []
        self.on_add_to_open_list = None
        self.on_select_next_node = None

    def create_nodes(self):
        rows, cols = 10, 10
        self.nodes = [[Node(i, j) for i in range(cols)] for j in range(rows)]

    def select_start_node(self, row, col):
        self.start_node = Node(row, col)
        self.nodes[row][col] = self.start_node

    def select_end_node(self, row, col):
        self.end_node = Node(row, col)
        self.nodes[row][col] = self.end_node

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
            next_node = AStarPathfinder.find_node_with_min_f(self.open_list)

            if next_node == self.end_node:
                best_path = AStarPathfinder.reconstruct_best_path(next_node)
                return best_path

            if self.on_select_next_node:
                self.on_select_next_node(next_node)

            self.closed_list.append(next_node)
            self.open_list.remove(next_node)

            neighbors = self.find_neighbors(next_node)

            for neighbor in neighbors:
                if neighbor in self.closed_list:
                    continue
                tentative_g = AStarPathfinder.calculate_tentative_g(next_node, neighbor)
                if neighbor not in self.open_list:
                    self.open_list.append(neighbor)
                    neighbor.update_values(tentative_g, self.end_node)
                    neighbor.parent_node = next_node
                    if self.on_add_to_open_list:
                        self.on_add_to_open_list(neighbor)
                elif tentative_g < neighbor.g:
                    neighbor.update_values(tentative_g, self.end_node)
                    neighbor.parent_node = next_node

        return None  # If no path is found

    @staticmethod
    def reconstruct_best_path(node):
        best_path = [node]
        current_node = node.parent_node
        while current_node.parent_node is not None:
            best_path.append(current_node)
            current_node = current_node.parent_node
        for elem in best_path:
            print(str(elem.index_0) + ", " + str(elem.index_1))
        return best_path

    def find_neighbors(self, node):
        neighbors = []
        row, col = node.index_0, node.index_1
        rows, cols = len(self.nodes), len(self.nodes[0])

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
                neighbors.append(self.nodes[nr][nc])

        return neighbors

    @staticmethod
    def calculate_tentative_g(current_node, neighbor_node):
        # Calculate the tentative g cost from current_node to neighbor_node
        dx = abs(current_node.index_0 - neighbor_node.index_0)
        dy = abs(current_node.index_1 - neighbor_node.index_1)
        if dx == 1 and dy == 1:  # Diagonal movement
            return current_node.g + math.sqrt(2)
        else:  # Horizontal or vertical movement
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

    def calculate_h(self, node_index_0, node_index_1):
        return abs(self.index_0 - node_index_0) + abs(self.index_1 - node_index_1)

    def calculate_f(self):
        return self.g + self.h

    def update_values(self, g, node):
        self.g = g
        self.h = self.calculate_h(node.index_0, node.index_1)
        self.f = self.calculate_f()
        self.parent_node = node
