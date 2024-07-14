class DFS:
    def __init__(self):
        self.__input = None
        self.__search_value = None
        self.__visited = []

    def set_input(self, input):
        self.__input = input

    def set_search_value(self, value):
        self.__search_value = value

    def run_algorithm(self):

        # Define root node
        root = None

        # Run the algorithm based on the root node and return the value
        return self.algorithm_loop(root)

    def algorithm_loop(self, node):

        # Check if search value == current node
        if self.__search_value == node.value:
            return node

        # Find neighbors of the current node which have not yet been visited
        neighbors = self.find_not_visited_neighbors(node)

        # For each neighbor run the dfs algorithm
        for neighbor in neighbors:
            self.algorithm_loop(neighbor)

        return None

    def find_not_visited_neighbors(self, node):
        pass
