import tkinter as tk


class View:
    def __init__(self, root, width, height):
        self.root = root
        self.width = width
        self.height = height
        self.canvas = tk.Canvas(root, width=width, height=height)
        self.canvas.pack()

        self.menu_bar = tk.Frame(root, height=30)
        self.menu_bar.pack(fill=tk.X, side=tk.BOTTOM)

        self.start_button = tk.Button(self.menu_bar, text="Start", command=self.start_simulation)
        self.start_button.pack(side=tk.TOP, pady=5)

        self.start_callback = None

    def draw_artifacts(self, artifacts):
        self.canvas.delete("all")
        for artifact in artifacts:
            x, y = artifact.position
            color = self.get_color(artifact.type)
            self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill=color)

    def get_color(self, artifact_type):
        if artifact_type == 0:
            return 'red'  # Rock
        elif artifact_type == 1:
            return 'green'  # Paper
        elif artifact_type == 2:
            return 'blue'  # Scissors

    def update(self):
        self.root.update_idletasks()
        self.root.update()

    def set_start_callback(self, callback):
        self.start_callback = callback

    def start_simulation(self):
        if self.start_callback:
            self.start_callback()