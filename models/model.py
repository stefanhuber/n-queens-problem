import random as rand
import helpers


class Model:

    @property
    def cost(self):
        return len(helpers.find_attacking_pairs(self.state))

    @property
    def step(self):
        return self.__step

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        self.__state = state

    def __init__(self):
        self.__state = []
        self.__step = 0

    def generate_initial_state(self, n=8):
        self.__state = [-1] * n
        self.__step = 0

        for column in range(0, n):
            self.__state[column] = rand.randint(0, n - 1)

    def evaluate_next_states(self):
        return helpers.evaluate_next_states(self.state)

    def move_next(self):
        self.__step += 1
