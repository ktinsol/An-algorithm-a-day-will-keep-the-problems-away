import tkinter as tk
from DepthFirstSearch.interface.model.tree import TreeBuilder

from DepthFirstSearch.interface.controllers.dfs_controller import DFSController

root = tk.Tk()
tree = TreeBuilder.build_tree_recursively(4, 5)
controller = DFSController(root, tree)
root.mainloop()

for node in tree.get_nodes():
    print(node.get_value())
