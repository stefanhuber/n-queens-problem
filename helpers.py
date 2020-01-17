def generate_next_states(state=[]):
    successors = []
    n = len(state)

    for column in range(0, n):
        for row in range(0, n):
            if state[column] != row:
                successor = state.copy()
                successor[column] = row
                successors.append(successor)

    return successors


def find_attacking_pairs(state=[]):
    pairs = set()

    for index_1, item_1 in enumerate(state):
        for index_2, item_2 in enumerate(state):
            if index_1 == index_2 or index_1 > index_2:
                continue
            elif item_1 == item_2:  # check rows
                pairs.add(((index_1, item_1), (index_2, item_2)))
            elif abs(index_1 - index_2) == abs(item_1 - item_2):  # check diagonal
                pairs.add(((index_1, item_1), (index_2, item_2)))

    return pairs


def evaluate_next_states(state=[]):
    n = len(state)
    result = [[-1 for c in range(0, n)] for r in range(0, n)]

    for column in range(0, n):
        for row in range(0, n):
            if state[column] != row:
                successor = state.copy()
                successor[column] = row
                result[row][column] = len(find_attacking_pairs(successor))

    return result