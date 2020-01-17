import models.model as m
import helpers
import random as rand
import math

class SimulatedAnnealing(m.Model):

    @property
    def schedule(self):
        schedule = 100 - (self.step * 5)

        if schedule > 0:
            return schedule
        else:
            return 0.00001 # avoid division by 0

    def move_next(self):
        super().move_next()
        state_cost = len(helpers.find_attacking_pairs(self.state))

        while state_cost > 0:
            random_next_state = rand.choice(helpers.generate_next_states(self.state))
            random_next_state_cost = len(helpers.find_attacking_pairs(random_next_state))

            difference = state_cost - random_next_state_cost

            if difference > 0:
                self.state = random_next_state
                break
            elif math.pow(math.e, difference / self.schedule) > 0.8:
                self.state = random_next_state
                break


