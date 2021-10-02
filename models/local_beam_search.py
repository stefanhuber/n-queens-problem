import random
import models.model as m
import helpers


class LocalBeamSearch(m.Model):

    def __init__(self, k=1):
        super().__init__()
        self.__k_states = []
        self.__k = k

    @staticmethod
    def select_best_states(states, k=1):
        candidates = []

        for state in states:
            state_cost = len(helpers.find_attacking_pairs(state))
            candidates.append([state, state_cost])

        return [item[0] for item in sorted(candidates, key=lambda item: item[1])[:k]]

    @staticmethod
    def get_random_following_states(state, k=1):
        next_states = helpers.generate_next_states(state)
        return [random.choice(next_states) for _ in range(k)]

    def move_next(self):
        super().move_next()

        # init k states
        if not self.__k_states:
            self.__k_states = LocalBeamSearch.get_random_following_states(self.state, self.__k)

        next_state_canditates = []
        for state in self.__k_states:
            next_state_canditates += helpers.generate_next_states(state)

        self.__k_states = LocalBeamSearch.select_best_states(next_state_canditates, self.__k)

        # set best state for visual display of the k states
        self.state = LocalBeamSearch.select_best_states(self.__k_states)[0]






