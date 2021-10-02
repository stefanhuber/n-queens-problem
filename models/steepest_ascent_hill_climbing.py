import models.model as m
import helpers

class SteepestAscentHillClimbing(m.Model):
    def move_next(self):
        super().move_next()
        next_states = helpers.generate_next_states(self.state)
        next_state_costs = []

        # calculate state costs of each successor state
        for next_state in next_states:
            next_state_costs.append(len(helpers.find_attacking_pairs(next_state)))

        # find the lowest state cost of all successsors
        minimum_cost_index = 0
        for index, next_state_cost in enumerate(next_state_costs):
            if next_state_cost < next_state_costs[minimum_cost_index]:
                minimum_cost_index = index

        # if there is the lowest cost successor has lower cost than
        # current state, select this successor
        if next_state_costs[minimum_cost_index] < self.cost:
            self.state = next_states[minimum_cost_index]
