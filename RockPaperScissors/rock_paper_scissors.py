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
        # Register contact and update population
        self.update_population()

    def update_population_position(self):
        for artifact in self.population:
            movement = random.randint(0, 4)
            if movement == 0:
                artifact.move_up()
            elif movement == 1:
                artifact.move_right()
            elif movement == 2:
                artifact.move_down()
            else:
                artifact.move_left()

    def update_population(self):
        # Find all artifacts that share the same position
        for artifact in self.population:
            for other_artifact in self.population:
                if artifact.position == other_artifact.position:
                    if RockPaperScissors.rock_paper_scissors(artifact, other_artifact) == artifact:
                        self.population.remove(other_artifact)
                    elif RockPaperScissors.rock_paper_scissors(artifact, other_artifact) == other_artifact:
                        self.population.remove(artifact)
                        break

    @staticmethod
    def rock_paper_scissors(artifact_a, artifact_b):
        if artifact_a.type == artifact_b.type:
            return None
        elif artifact_a == 0 and artifact_b != 1:
            return artifact_a
        elif artifact_a == 1 and artifact_b != 2:
            return artifact_a
        elif artifact_a == 2 and artifact_b != 3:
            return artifact_a
        else:
            return artifact_b


class Artifact:

    def __init__(self):
        # 0 = Rock, 1 = Paper, 2 = Scissors
        self.type = random.randint(0, 3)
        self.position = [random.randint(5, 500-5), random.randint(5, 500-5)]

    def move_up(self):
        self.position[1] -= 1

    def move_down(self):
        self.position[1] += 1

    def move_left(self):
        self.position[0] -= 1

    def move_right(self):
        self.position[0] += 1
