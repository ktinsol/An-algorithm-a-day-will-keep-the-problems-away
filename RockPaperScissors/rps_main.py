import tkinter as tk
from RockPaperScissors.interface.controllers.rps_controller import Controller

root = tk.Tk()
app = Controller(root)
root.mainloop()
