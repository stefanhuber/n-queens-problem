from models.basic_hill_climbing import BasicHillClimbing
from models.steepest_ascent_hill_climbing import SteepestAscentHillClimbing
from models.stochastic_hill_climbing import StochasticHillClimbing
from models.simulated_annealing import SimulatedAnnealing

class Controller:
    def __init__(self, view):
        self.__view = view
        self.__view.init_listener = self.init_board
        self.__view.next_listener = self.next_board
        self.__view.selection_listener = self.change_selection
        self.change_selection("Basic Hill-Climbing")

    def start(self):
        self.__view.show()

    def change_selection(self, selection):
        if selection == "Basic Hill-Climbing":
            self.__model = BasicHillClimbing()
        elif selection == "Steepest Ascent Hill-Climbing":
            self.__model = SteepestAscentHillClimbing()
        elif selection == "Stochastic Hill-Climbing":
            self.__model = StochasticHillClimbing()
        elif selection == "Simulated Annealing":
            self.__model = SimulatedAnnealing()

        self.__model.generate_initial_state()
        self.draw()

    def next_board(self):
        self.__model.move_next()
        self.draw()

    def init_board(self):
        self.__model.generate_initial_state()
        self.draw()

    def draw(self):
        self.__view.draw_board()
        self.__view.cost = self.__model.cost
        self.__view.step = self.__model.step

        for column, row in enumerate(self.__model.state):
            self.__view.draw_position(column, row)

        for row_index, row in enumerate(self.__model.evaluate_next_states()):
            for column_index, value in enumerate(row):
                if value >= 0:
                    self.__view.draw_value(column_index, row_index, value)
