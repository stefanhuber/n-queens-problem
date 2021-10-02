import random
import models.model as m
import helpers


class FirstChoiceHillClimbing(m.Model):
    def move_next(self):
        super().move_next()
        state_cost = self.cost
        next_state_candidates = helpers.generate_next_states(self.state)
        len_next_state_candidates = len(next_state_candidates)

        for i in range(len_next_state_candidates):
            random_index = random.randint(0, len_next_state_candidates - i - 1)
            next_state = next_state_candidates[random_index]
            next_state_cost = len(helpers.find_attacking_pairs(next_state))

            if next_state_cost < state_cost:
                self.state = next_state
                break


