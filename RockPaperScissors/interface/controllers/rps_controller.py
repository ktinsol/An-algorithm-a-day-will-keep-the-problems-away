import tkinter as tk
import random
import time
from RockPaperScissors.interface.views.rps_view import View
from RockPaperScissors.rock_paper_scissors import RockPaperScissors, Artifact


class Controller:
    def __init__(self, root):
        self.view = View(root, 600, 600)
        self.simulation = RockPaperScissors()
        self.simulation.generate_start_population()
        self.view.set_start_callback(self.run_simulation)
        self.view.draw_artifacts(self.simulation.population)

    def run_simulation(self):
        while len(self.simulation.population) > 1:
            self.simulation.update_population_position()
            self.simulation.update_population()
            self.view.draw_artifacts(self.simulation.population)
            self.view.update()
            time.sleep(0.1)  # Pause to see the simulation step-by-step
