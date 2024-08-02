import tkinter as tk
import math


class DFSView:
    def __init__(self, master, tree):
        self.master = master
        self.tree = tree

        # Set full-screen mode
        self.master.attributes('-fullscreen', True)
        self.master.bind('<Escape>', self.exit_fullscreen)

        # Get the screen width and height
        self.width = self.master.winfo_screenwidth()
        self.height = self.master.winfo_screenheight()

        self.canvas = tk.Canvas(master, width=self.width, height=self.height, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.node_positions = {}
        self.draw_tree()

    def draw_tree(self):
        root = self.tree.get_root_node()
        if not root:
            return

        level_nodes = [[root]]
        self.node_positions[root] = (self.width // 2, 50)
        self._draw_node(root, self.width // 2, 50)

        y_gap = 100
        while level_nodes:
            next_level_nodes = []
            for node in level_nodes.pop(0):
                x, y = self.node_positions[node]
                child_count = len(node.get_child_nodes())
                if child_count > 0:
                    x_gap = min(self.width // (child_count + 1), 200)
                    for i, child in enumerate(node.get_child_nodes()):
                        if child is None:
                            continue
                        child_x = x - (x_gap * (child_count // 2)) + (x_gap * i)
                        child_y = y + y_gap
                        self.node_positions[child] = (child_x, child_y)
                        self._draw_node(child, child_x, child_y)
                        self._draw_line(x, y, child_x, child_y)
                        next_level_nodes.append(child)
            if next_level_nodes:
                level_nodes.append(next_level_nodes)

        # Scale down if necessary
        self._scale_tree()

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

    def _scale_tree(self):
        # Get bounding box of all nodes
        all_x_positions = [pos[0] for pos in self.node_positions.values()]
        all_y_positions = [pos[1] for pos in self.node_positions.values()]

        min_x, max_x = min(all_x_positions), max(all_x_positions)
        min_y, max_y = min(all_y_positions), max(all_y_positions)

        tree_width = max_x - min_x
        tree_height = max_y - min_y

        scale_factor = min(self.width / tree_width, self.height / tree_height, 1)

        # Adjust positions based on scale factor
        if scale_factor < 1:
            for node, (x, y) in self.node_positions.items():
                new_x = self.width // 2 + scale_factor * (x - self.width // 2)
                new_y = 50 + scale_factor * (y - 50)
                self.node_positions[node] = (new_x, new_y)

            self.canvas.delete("all")
            for node, (x, y) in self.node_positions.items():
                if node is None:
                    return
                self._draw_node(node, x, y)
                for child in node.get_child_nodes():
                    if child in self.node_positions:
                        child_x, child_y = self.node_positions[child]
                        self._draw_line(x, y, child_x, child_y)

    def exit_fullscreen(self, event=None):
        self.master.attributes('-fullscreen', False)
        self.master.geometry(f"{self.width}x{self.height}")