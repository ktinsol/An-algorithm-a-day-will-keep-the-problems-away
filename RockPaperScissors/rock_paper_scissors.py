import random


class RockPaperScissors:

    def __init__(self):
        self.population = []

    def run_simulation(self):
        # Generate the starting population
        self.generate_start_population()
        # Now we have to run the simulation
        self.simulation_loop()

    def generate_start_population(self):
        for i in range(69):
            self.population.append(Artifact())

    def simulation_loop(self):
        # Artifacts move one space
        self.update_population_position()

    def update_population_position(self):
        for artifact in self.population:
            movement = random.randint(4)
            if movement == 0:

            elif movement == 1:

            elif movement == 2:

            else:


class Artifact:

    def __init__(self):
        self.type = random.randint(0, 3)
        self.position = (0, 0)

    def move_up(self):
        self.position = (self.position)
