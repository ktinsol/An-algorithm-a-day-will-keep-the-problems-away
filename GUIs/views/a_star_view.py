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

        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate maximum button size to fit 25x25 grid within screen dimensions
        max_button_width = screen_width // 25
        max_button_height = screen_height // 25

        # Set button size (use the smaller of the two dimensions to maintain aspect ratio)
        button_size = min(max_button_width, max_button_height)

        for i in range(25):
            row_buttons = []
            for j in range(25):
                btn = tk.Button(self.root, width=button_size // 10, height=button_size // 20,
                                command=lambda i=i, j=j: self.on_node_click(i, j))
                btn.grid(row=i, column=j, padx=1, pady=1)
                row_buttons.append(btn)
            self.grid_buttons.append(row_buttons)

        self.start_button = tk.Button(self.root, text="Start Algorithm", command=self.start_algorithm)
        self.start_button.grid(row=26, columnspan=25)
        self.start_button.grid_remove()

        # Adjust window size to fit the grid
        self.root.geometry(f"{button_size * 25}x{button_size * 25 + 50}")

    def on_node_click(self, row, col):
        if not self.start_selected:
            self.controller.set_start_node(row, col)
            self.grid_buttons[row][col].configure(bg="green")
            self.start_selected = True
        elif not self.end_selected:
            self.controller.set_end_node(row, col)
            self.grid_buttons[row][col].configure(bg="red")
            self.end_selected = True
            self.start_button.grid()
        else:
            self.controller.set_wall_node(row, col)
            self.grid_buttons[row][col].configure(bg="grey")

    def start_algorithm(self):
        best_path = self.controller.start_algorithm()
        if best_path:
            for elem in best_path:
                self.grid_buttons[elem.index_0][elem.index_1].configure(bg="yellow")
        else:
            messagebox.showinfo("No Path", "No path could be found between the selected nodes.")

    def update_node_color(self, row, col, color):
        self.grid_buttons[row][col].configure(bg=color)
