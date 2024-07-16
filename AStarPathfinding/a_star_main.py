import tkinter as tk

from AStarPathfinding.interface.controllers.a_star_controller import AStarController
from AStarPathfinding.interface.views.a_star_view import AStarView

root = tk.Tk()
controller = AStarController()
view = AStarView(root, controller)
root.mainloop()
