import tkinter as tk
from tkinter import messagebox


class AStarView:

    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.grid_buttons = []
        self.start_selected = False
        self.end_selected = False
        self.start_button = None
        self.create_widgets()
        self.controller.set_view(self)

    def create_widgets(self):
        self.root.title("A* Pathfinding Visualizer")
        for i in range(10):
            row_buttons = []
            for j in range(10):
                btn = tk.Button(self.root, width=4, height=2, command=lambda i=i, j=j: self.on_node_click(i, j))
                btn.grid(row=i, column=j)
                row_buttons.append(btn)
            self.grid_buttons.append(row_buttons)
        self.start_button = tk.Button(self.root, text="Start Algorithm", command=self.start_algorithm)
        self.start_button.grid(row=10, columnspan=10)
        self.start_button.grid_remove()

    def on_node_click(self, row, col):
        print(row, col)
        if not self.start_selected:
            self.controller.set_start_node(row, col)
            self.grid_buttons[row][col].configure(bg="green")
            self.start_selected = True
        elif not self.end_selected:
            self.controller.set_end_node(row, col)
            self.grid_buttons[row][col].configure(bg="red")
            self.end_selected = True
            self.start_button.grid()

    def start_algorithm(self):
        best_path = self.controller.start_algorithm()
        if best_path:
            for elem in best_path:
                self.grid_buttons[elem.index_0][elem.index_1].configure(bg="yellow")
        else:
            messagebox.showinfo("No Path", "No path could be found between the selected nodes.")

    def update_node_color(self, row, col, color):
        self.grid_buttons[row][col].configure(bg=color)
