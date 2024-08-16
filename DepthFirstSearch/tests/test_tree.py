import unittest
from uuid import UUID
from DepthFirstSearch.interface.model.tree import Tree, Node, TreeBuilder


class TestTreeStructure(unittest.TestCase):

    def setUp(self):
        """Set up a basic tree structure for testing."""
        self.tree = Tree()
        self.root_node = Node()
        self.root_node.set_value(1)
        self.tree.set_root_node(self.root_node)

        self.child_node1 = Node()
        self.child_node1.set_value(2)
        self.root_node.add_child_node(self.child_node1)

        self.child_node2 = Node()
        self.child_node2.set_value(3)
        self.root_node.add_child_node(self.child_node2)

    def test_node_creation(self):
        """Test that nodes are created with unique IDs and correct initial values."""
        node = Node()
        self.assertIsInstance(node.get_id(), UUID)
        self.assertEqual(node.get_value(), None)
        self.assertEqual(node.get_child_nodes(), [])
        self.assertEqual(node.get_parent_nodes(), [])

    def test_add_child_and_parent_nodes(self):
        """Test that child and parent nodes are correctly added."""
        child_node = Node()
        child_node.set_value(5)
        parent_node = Node()
        parent_node.set_value(10)

        child_node.add_parent_node(parent_node)
        parent_node.add_child_node(child_node)

        self.assertIn(child_node, parent_node.get_child_nodes())
        self.assertIn(parent_node, child_node.get_parent_nodes())

    def test_tree_structure(self):
        """Test that the tree structure is correct after adding nodes."""
        self.assertEqual(self.tree.get_root_node().get_value(), 1)
        child_values = [child.get_value() for child in self.tree.get_root_node().get_child_nodes()]
        self.assertIn(2, child_values)
        self.assertIn(3, child_values)

    def test_print_tree_empty(self):
        """Test that printing an empty tree results in the expected output."""
        empty_tree = Tree()
        self.assertIsNone(empty_tree.print_tree())

    def test_tree_builder(self):
        """Test that the TreeBuilder correctly builds a tree."""
        tree = TreeBuilder.build_tree_recursively(3, 2)
        self.assertIsNotNone(tree.get_root_node())
        self.assertGreater(len(tree.get_nodes()), 0)

    def test_tree_with_none_nodes(self):
        """Test that TreeBuilder handles None nodes correctly."""
        tree = TreeBuilder.build_tree_recursively(2, 3)
        nodes = tree.get_nodes()
        none_count = nodes.count(None)
        self.assertEqual(none_count, 0)

    def test_remove_none_values_from_tree(self):
        """Test that remove_none_values_from_tree correctly filters out None values."""
        nodes = [Node(), None, Node(), None, Node()]
        filtered_nodes = TreeBuilder.remove_none_values_from_tree(nodes)
        self.assertEqual(len(filtered_nodes), 3)
        self.assertNotIn(None, filtered_nodes)

if __name__ == '__main__':
    unittest.main()
