import tkinter as tk

from GUIs.controllers.dfs_controller import DFSController
from GUIs.views.dfs_view import DFSView

root = tk.Tk()
controller = DFSController()
view = DFSView(root, controller)
root.mainloop()
