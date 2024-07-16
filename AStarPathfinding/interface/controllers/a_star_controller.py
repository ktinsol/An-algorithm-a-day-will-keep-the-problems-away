from AStarPathfinding.a_star_pathfinding import AStarPathfinder
from AStarPathfinding.a_star_pathfinding import Node


class AStarController:

    def __init__(self):
        self.grid = [[Node(row, col) for col in range(25)] for row in range(25)]
        self.pathfinder = AStarPathfinder()
        self.pathfinder.set_grid(self.grid)
        # self.pathfinder.create_nodes()
        self.pathfinder.on_add_to_open_list = self.on_add_to_open_list
        self.pathfinder.on_select_next_node = self.on_select_next_node
        self.view = None

    def set_view(self, view):
        self.view = view

    def set_start_node(self, row, col):
        self.pathfinder.select_start_node(row, col)

    def set_end_node(self, row, col):
        self.pathfinder.select_end_node(row, col)

    def set_wall_node(self, row, col):
        node = self.grid[row][col]
        node.is_wall = True

    def start_algorithm(self):
        self.pathfinder.init_the_algo()
        return self.pathfinder.find_best_path()

    def on_add_to_open_list(self, node):
        if self.view:
            self.view.update_node_color(node.index_0, node.index_1, "light blue")

    def on_select_next_node(self, node):
        if self.view:
            self.view.update_node_color(node.index_0, node.index_1, "orange")

