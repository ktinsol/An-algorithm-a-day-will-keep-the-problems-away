import random


class RandomArrayGenerator:

    def __init__(self):
        pass

    @staticmethod
    def generate_random_array(size=None):
        if size is None:
            size = 20
        return [random.randint(0, 100) for i in range(size)]
