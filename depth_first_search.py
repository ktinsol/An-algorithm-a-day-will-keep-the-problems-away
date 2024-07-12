class DFS:
    def __init__(self):
        self.input = None
        self.search_value = None
        self.visited = []

    def set_input(self, input):
        self.input = input

    def set_search_value(self, value):
        self.search_value = value

    def run_algorithm(self):

        # Define root node
        root = None

        # Run the algorithm based on the root node and return the value
        return self.dfs_algorithm(root)

    def dfs_algorithm(self, node):

        # Check if search value == current node
        if self.search_value == node.value:
            return node

        # Find neighbors of the current node which have not yet been visited
        neighbors = self.find_not_visited_neighbors(node)

        # For each neighbor run the dfs algorithm
        for neighbor in neighbors:
            self.dfs_algorithm(neighbor)

        return None

    def find_not_visited_neighbors(self, node):
        pass
