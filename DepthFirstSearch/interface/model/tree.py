import random
import uuid


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

    def print_tree(self):
        if self.get_root_node() is None:
            return None
        stack = [self.get_root_node()]
        self.print_recursively(len(stack), stack)

    def print_recursively(self, size, stack):
        if size <= 0:
            return
        output_string = ""
        for i in range(size):
            current_node = stack.pop(0)
            parent_node_value = ""
            if current_node is None:
                continue
            for parent_node in current_node.get_parent_nodes():
                if parent_node is not None:
                    parent_node_value += str(hex(id(parent_node)))
                else:
                    parent_node_value = ""
            # output_string += " " + str(current_node.get_value()) + "(" + parent_node_value + ")"
            output_string += " " + str(hex(id(current_node))) + "(" + parent_node_value + ")"
            if current_node.get_child_nodes() is None:
                continue
            for child in current_node.get_child_nodes():
                stack.append(child)
        print(output_string)
        self.print_recursively(len(stack), stack)


class Node:

    def __init__(self):
        self.__value = None
        self.__child_nodes = []
        self.__parent_nodes = []
        self.__id = Node.generate_id()

    def add_child_node(self, node):
        self.__child_nodes.append(node)

    def add_parent_node(self, node):
        self.__parent_nodes.append(node)

    def get_child_nodes(self):
        return self.__child_nodes

    def get_parent_nodes(self):
        return self.__parent_nodes

    def set_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def get_id(self):
        return self.__id

    @staticmethod
    def generate_id():
        unique_id = uuid.uuid1()
        return unique_id


class TreeBuilder:

    @staticmethod
    def build_tree_recursively(depth, width):
        # Create tree object
        tree = Tree()
        # Create tree recursively
        tree.set_root_node(TreeBuilder.recursive_build_tree(0, depth, width, None))
        # Build the tree array based on the returned node with its children
        tree.set_nodes(TreeBuilder.construct_tree(tree.get_root_node()))
        # Clean the tree of none values
        tree.set_nodes(TreeBuilder.remove_none_values_from_tree(tree.get_nodes()))
        # Return the tree object as output
        return tree

    @staticmethod
    def recursive_build_tree(depth, limit, width, parent):
        if depth == limit:
            return None
        else:
            child_node = None
            for i in range(width):
                child_node = TreeBuilder.create_node_randomly(depth)
                if child_node is None:
                    continue
                child_node.add_parent_node(parent)
                if parent is not None:
                    parent.add_child_node(child_node)
                # parent.add_child_node(TreeBuilder.recursive_build_tree(depth+1, limit, width, child_node))
                child_node.add_child_node(TreeBuilder.recursive_build_tree(depth + 1, limit, width, child_node))
            return child_node

    @staticmethod
    def create_node_randomly(level):
        random_int = random.randint(0, level+1)
        if random_int <= 1:
            return TreeBuilder.create_node()
        else:
            return None

    @staticmethod
    def create_node():
        node = Node()
        node.set_value(random.randint(0, 10))
        return node

    @staticmethod
    def create_parent_and_child_relations(tree):
        pass

    @staticmethod
    def construct_tree(root_node):
        nodes = [root_node]
        index = 0
        current_node = root_node
        while current_node:
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


