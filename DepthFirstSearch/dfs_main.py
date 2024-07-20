import tkinter as tk
from DepthFirstSearch.interface.model.tree import TreeBuilder
from DepthFirstSearch.interface.controllers.dfs_controller import DFSController

root = tk.Tk()
tree = TreeBuilder.build_tree_recursively(4, 5)
tree.print_tree()
#print(tree.get_root_node().get_value())
#print(tree.get_root_node().get_child_nodes())
controller = DFSController(root, tree)
root.mainloop()
