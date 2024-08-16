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

        level_nodes = [[root]]
        self.node_positions[id(root)] = (self.width // 2, 50)
        self._draw_node(root, self.width // 2, 50)

        y_gap = 100
        max_width = 0
        while level_nodes:
            next_level_nodes = []
            for j, node in enumerate(level_nodes.pop(0)):
                x, y = self.node_positions[id(node)]
                x += j * 30
                child_count = len(node.get_child_nodes())
                if child_count > 0:
                    x_gap = min(self.width // (child_count + 1), 200)
                    start_x = x - (x_gap * (child_count - 1)) // 2
                    for i, child in enumerate(node.get_child_nodes()):
                        if child is None:
                            continue
                        child_x = start_x + (x_gap * i)
                        child_y = y + y_gap
                        self.node_positions[id(child)] = (child_x, child_y)
                        self._draw_node(child, child_x, child_y)
                        self._draw_line(x, y, child_x, child_y)
                        next_level_nodes.append(child)
                        max_width = max(max_width, abs(child_x - self.width // 2))
            if next_level_nodes:
                level_nodes.append(next_level_nodes)

        # Adjust scaling to fit within the screen dimensions
        max_height = y + y_gap
        scale_factor = min(self.width / (2 * max_width), self.height / max_height, 1)

        self._scale_tree(scale_factor)

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

    def _scale_tree(self, scale_factor):
        # Adjust positions based on scale factor
        if scale_factor < 1:
            for node_id, (x, y) in self.node_positions.items():
                new_x = self.width // 2 + scale_factor * (x - self.width // 2)
                new_y = 50 + scale_factor * (y - 50)
                self.node_positions[node_id] = (new_x, new_y)

            self.canvas.delete("all")
            for node_id, (x, y) in self.node_positions.items():
                node = next(node for node in self.tree.get_nodes() if id(node) == node_id)
                self._draw_node(node, x, y)
                for child in node.get_child_nodes():
                    if id(child) in self.node_positions:
                        child_x, child_y = self.node_positions[id(child)]
                        self._draw_line(x, y, child_x, child_y)

    def exit_fullscreen(self, event=None):
        self.master.attributes('-fullscreen', False)
        self.master.geometry(f"{self.width}x{self.height}")
        self.master.quit()  # Properly end the Tkinter event loop
        self.master.destroy()  # Destroy the window
