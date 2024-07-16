import random


class Tree:

    def __init__(self):
        self.__nodes = []
        self.__root_node = None

    def add_node(self, node):
        self.__nodes.append(node)

    def set_root_node(self, node):
        self.__root_node = node

    def get_root_node(self):
        return self.__root_node

    def get_nodes(self):
        return self.__nodes

    def set_nodes(self, nodes):
        self.__nodes = nodes


class Node:

    def __init__(self):
        self.__value = None
        self.__child_nodes = []
        self.__parent_nodes = []

    def add_child_node(self, node):
        self.__child_nodes.append(node)

    def add_parent_node(self, node):
        self.__parent_nodes.append(node)

    def get_child_nodes(self):
        return self.__child_nodes

    def get_parent_nodes(self):
        return self.get_parent_nodes()

    def set_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value


class TreeBuilder:

    @staticmethod
    def build_tree(depth, width):
        # Create tree object
        tree = Tree()
        # Create root node
        root_node = TreeBuilder.create_node()
        # Connect root node and tree object
        tree.set_root_node(root_node)
        # Create other nodes and add them to the tree
        for i in range(depth-1):
            for j in range(width):
                node = TreeBuilder.create_node_randomly()
                if node is not None:
                    tree.add_node(node)
        # Create child and parent relations
        tree = TreeBuilder.create_parent_and_child_relations(tree)
        return tree

    @staticmethod
    def build_tree_recursively(depth, width):
        # Create tree object
        tree = Tree()
        # Create root node
        root_node = TreeBuilder.create_node()
        # Create tree recursively
        tree.set_root_node(TreeBuilder.recursive_build_tree(0, depth, width, root_node))
        print(tree.get_root_node())
        # Build the tree based on the returned node with its children
        tree.set_nodes(TreeBuilder.construct_tree(tree.get_root_node()))
        print(tree.get_nodes())
        # Clean the tree of none values
        tree.set_nodes(TreeBuilder.remove_none_values_from_tree(tree.get_nodes()))
        print(tree.get_nodes())
        # Return the tree object as output
        return tree
        
    @staticmethod
    def recursive_build_tree(depth, limit, width, parent):
        if depth == limit:
            return None
        else:
            for i in range(width):
                child_node = TreeBuilder.create_node_randomly()
                if child_node is None:
                    continue
                child_node.add_parent_node(parent)
                parent.add_child_node(TreeBuilder.recursive_build_tree(depth+1, limit, width, child_node))
            return child_node

    @staticmethod
    def create_node_randomly():
        random_int = random.randint(0, 3)
        if random_int >= 0:
            return TreeBuilder.create_node()
        else:
            return None

    @staticmethod
    def create_node():
        node = Node()
        node.set_value(TreeBuilder.generate_random_value(0, 10))
        return node

    @staticmethod
    def generate_random_value(min_limit, max_limit):
        return random.randint(min_limit, max_limit)

    @staticmethod
    def create_parent_and_child_relations(tree):
        pass

    @staticmethod
    def construct_tree(root_node):
        nodes = [root_node]
        index = 0
        current_node = root_node
        while True:
            for child_node in current_node.get_child_nodes():
                if child_node is not None:
                    nodes.append(child_node)
            if index + 1 < len(nodes):
                index += 1
            else:
                break
            current_node = nodes[index]
        return nodes

    @staticmethod
    def remove_none_values_from_tree(tree):
        return [value for value in tree if value is not None]


