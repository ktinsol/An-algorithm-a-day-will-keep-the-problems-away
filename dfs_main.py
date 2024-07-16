import time
import tkinter as tk
from Datastructures.tree import TreeBuilder

from GUIs.controllers.dfs_controller import DFSController
from GUIs.views.dfs_view import DFSView
from depth_first_search import DFS

root = tk.Tk()
tree = TreeBuilder.build_tree_recursively(4, 5)
controller = DFSController(root, tree)
root.mainloop()

for node in tree.get_nodes():
    print(node.get_value())
