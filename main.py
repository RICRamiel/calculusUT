from typing import Tuple


class History:
    def __init__(self):
        self.data = []

    def store(self, entity: Tuple):
        self.data.append(entity)


class Calculus:

    def __init__(self):
        self.history = History()

    def sum(self, a: int, b: int):
        e = (a, b, a + b)
        self.history.store(e)
        return a + b
