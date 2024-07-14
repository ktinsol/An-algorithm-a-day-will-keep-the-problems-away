import tkinter as tk

from GUIs.controllers.dfs_controller import DFSController
from GUIs.views.dfs_view import DFSView
from depth_first_search import DFS

root = tk.Tk()
controller = DFSController()
view = DFSView(root, controller)



root.mainloop()
