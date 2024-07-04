from a_star_pathfinding import A_Star_Pathfinder


class AStarController:

    def __init__(self):
        self.pathfinder = A_Star_Pathfinder()
        self.pathfinder.create_nodes()

    def set_start_node(self, row, col):
        self.pathfinder.select_start_node(row, col)

    def set_end_node(self, row, col):
        self.pathfinder.select_end_node(row, col)

    def start_algorithm(self):
        self.pathfinder.init_the_algo()
        return self.pathfinder.find_best_path()
