import tkinter as tk

class View:

    @property
    def init_listener(self):
        return self.__init_listener

    @init_listener.setter
    def init_listener(self, listener):
        self.__init_listener = listener

    @property
    def next_listener(self):
        return self.__next_listener

    @next_listener.setter
    def next_listener(self, listener):
        self.__next_listener = listener

    @property
    def selection_listener(self):
        return self.__selection_listener

    @selection_listener.setter
    def selection_listener(self, listener):
        self.__selection_listener = listener

    @property
    def cost(self):
        return self.__cost['text']

    @cost.setter
    def cost(self, cost):
        self.__cost['text'] = "Current cost: {}".format(cost)

    @property
    def step(self):
        return self.__step['text']

    @step.setter
    def step(self, step):
        self.__step['text'] = "Step: {}".format(step)

    def __init__(self, boardsize=400):
        self.__init_listener = None
        self.__next_listener = None
        self.__boardsize = boardsize
        self.__cellsize = boardsize / 8

        self.__window = tk.Tk()
        self.__window.title("8-queens problem < > local search")
        self.__window.resizable(False, False)

        self.__canvas = tk.Canvas(self.__window, bg="gray", height=400, width=400)
        self.__canvas.pack()

        buttons = tk.Frame(self.__window)
        buttons.pack(side=tk.BOTTOM)

        init = tk.Button(buttons, text="Init", command=self.on_init)
        init.pack(side=tk.LEFT, padx=10, pady=10)

        next = tk.Button(buttons, text="Next", command=self.on_next)
        next.pack(side=tk.LEFT, padx=10, pady=10)

        choices = (
            "Basic Hill-Climbing",
            "Steepest Ascent Hill-Climbing",
            "Stochastic Hill-Climbing",
            "First Choice (Stochastic) Hill-Climbing",
            "Simulated Annealing",
            "Local Beam Search (k=2)",
            "Local Beam Search (k=3)",
            "Local Beam Search (k=4)",
        )
        self.__choice_var = tk.StringVar(self.__window, choices[0])
        self.__choice_var.trace("w", self.on_select)

        select = tk.OptionMenu(buttons, self.__choice_var, *choices)
        select.pack(side=tk.LEFT, padx=10, pady=10)

        labels = tk.Frame(self.__window)
        labels.pack(side=tk.BOTTOM)

        self.__cost = tk.Label(labels)
        self.__cost.pack(side=tk.LEFT, padx=10, pady=10)

        self.__step = tk.Label(labels)
        self.__step.pack(side=tk.LEFT, padx=10, pady=10)

    def draw_board(self, positions=[]):
        self.__canvas.delete("all")

        for r in range(0, 8):
            for c in range(0, 4):
                start_x = (c * self.__cellsize * 2) + (self.__cellsize if r % 2 == 1 else 0)
                start_y = r * self.__cellsize
                self.__canvas.create_rectangle(start_x, start_y, start_x + self.__cellsize, start_y + self.__cellsize, fill="white", width=0)

    def draw_position(self, column=0, row=0):
        start_x = (column * self.__cellsize) + int(self.__cellsize * 0.15)
        start_y = (row * self.__cellsize) + int(self.__cellsize * 0.15)
        end_x = start_x + int(self.__cellsize * 0.7)
        end_y = start_y + int(self.__cellsize * 0.7)

        self.__canvas.create_oval(start_x, start_y, end_x, end_y, fill="red", width=0)

    def draw_value(self, column=0, row=0, value="99"):
        start_x = (column * self.__cellsize) + int(self.__cellsize * 0.8)
        start_y = (row * self.__cellsize) + int(self.__cellsize * 0.2)

        self.__canvas.create_text(start_x, start_y, text=str(value), fill="blue")

    def on_init(self):
        if self.__init_listener:
            self.__init_listener()

    def on_next(self):
        if self.__next_listener:
            self.__next_listener()

    def on_select(self, *args):
        if self.__selection_listener:
            self.__selection_listener(self.__choice_var.get())

    def show(self):
        self.__window.mainloop()
