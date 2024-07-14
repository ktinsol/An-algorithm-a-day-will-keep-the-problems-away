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
        return self.get_child_nodes()

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
        # Connect root node and tree object
        tree.set_root_node(root_node)
        # Create tree recursively
        tree.add_node(TreeBuilder.recursive_build_tree(0, depth, width, tree.get_root_node()))
        
    @staticmethod
    def recursive_build_tree(depth, limit, width, parent):
        if depth == limit:
            return None
        else:
            for i in range(width):
                node = TreeBuilder.create_node_randomly()
                node.add_parent_node(parent)
                node.add_child_node(TreeBuilder.recursive_build_tree(depth+1,limit,width, node))
                return node
    @staticmethod
    def create_node_randomly():
        random_int = random.randint(0, 3)
        if random_int == 3:
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


