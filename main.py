import tkinter as tk

from GUIs.controllers.a_star_controller import AStarController
from GUIs.views.a_star_view import AStarView

root = tk.Tk()
controller = AStarController()
view = AStarView(root, controller)
root.mainloop()