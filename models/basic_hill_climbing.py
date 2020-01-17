import models.model as m
import helpers

class BasicHillClimbing(m.Model):

    def move_next(self):
        super().move_next()
        state_cost = len(helpers.find_attacking_pairs(self.state))

        for next_state in helpers.generate_next_states(self.state):
            next_state_cost = len(helpers.find_attacking_pairs(next_state))

            if next_state_cost < state_cost:
                self.state = next_state
                break


