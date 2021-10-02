import models.model as m
import helpers
import random as rand

class StochasticHillClimbing(m.Model):
    def move_next(self):
        super().move_next()
        state_cost = self.cost
        next_state_canditates = []

        # select all states which have a lower cost than current
        for next_state in helpers.generate_next_states(self.state):
            next_state_cost = len(helpers.find_attacking_pairs(next_state))

            if next_state_cost < state_cost:
                next_state_canditates.append(next_state)

        if len(next_state_canditates) > 0:
            self.state = rand.choice(next_state_canditates)