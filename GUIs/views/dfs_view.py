import tkinter as tk
import math


class DFSView:
    def __init__(self, master, tree):
        self.master = master
        self.tree = tree
        self.canvas = tk.Canvas(master, width=800, height=600, bg='white')
        self.canvas.pack()
        self.node_positions = {}
        self.draw_tree()

    def draw_tree(self):
        root = self.tree.get_root_node()
        level_nodes = [[root]]
        self.node_positions[root] = (400, 50)
        self._draw_node(root, 400, 50)

        y_gap = 100
        while level_nodes:
            next_level_nodes = []
            for node in level_nodes.pop(0):
                x, y = self.node_positions[node]
                child_count = len(node.get_child_nodes())
                if child_count > 0:
                    x_gap = 800 // (child_count + 1)
                    for i, child in enumerate(node.get_child_nodes()):
                        child_x = x - 400 + x_gap * (i + 1)
                        child_y = y + y_gap
                        self.node_positions[child] = (child_x, child_y)
                        self._draw_node(child, child_x, child_y)
                        self._draw_line(x, y, child_x, child_y)
                        next_level_nodes.append(child)
            if next_level_nodes:
                level_nodes.append(next_level_nodes)

    def _draw_node(self, node, x, y):
        r = 20
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill='lightblue')
        self.canvas.create_text(x, y, text=node.get_value())

    def _draw_line(self, x1, y1, x2, y2):
        self.canvas.create_line(x1, y1, x2, y2)
