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
                if child_count > 0 and node.get_child_nodes() is not None:
                    x_gap = 800 // (child_count + 1)
                    for i, child in enumerate(node.get_child_nodes()):
                        if child is not None:
                            child_x = x - 400 + x_gap * (i + 1)
                            child_y = y + y_gap
                            self.node_positions[child] = (child_x, child_y)
                            self._draw_node(child, child_x, child_y)
                            self._draw_line(x, y, child_x, child_y)
                            next_level_nodes.append(child)
                        else:
                            continue
            if next_level_nodes:
                level_nodes.append(next_level_nodes)

    def _draw_node(self, node, x, y):
        r = 20
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill='lightblue')
        self.canvas.create_text(x, y, text=node.get_value())

    def _draw_line(self, x1, y1, x2, y2):
        r = 20  # radius of the node circle

        # Calculate the coordinates of the intersection points
        len_ab = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        xa = x1 + r * (x2 - x1) / len_ab
        ya = y1 + r * (y2 - y1) / len_ab
        xb = x2 - r * (x2 - x1) / len_ab
        yb = y2 - r * (y2 - y1) / len_ab

        # Draw the line between the intersection points
        self.canvas.create_line(xa, ya, xb, yb)
