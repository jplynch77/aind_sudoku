import random

grid2 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
values = grid_values(grid2)


values = reduce_puzzle(values)

def search(values):
   # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes):
        return values ## Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt
    pass


def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)

    if values is False:
        return False
    if all(len(values[s]) == 1 for s in boxes):
        return values

    ## choose a square with few possibilities then reduce puzzle
    value_list = [v for k,v in values.items() if len(v) != 1]
    box_lengths = list(map(len, value_list))
    min_unsolved_length = min(box_lengths)

    subset_dict = {k:v for k,v in values.items() if len(v) == min_unsolved_length}
    box_choice = list(subset_dict.keys())[0]

    for value in values[s]:
        suduko = values.copy()
        new_suduko[s] = value
        attempt = search(new_suduko)
        if attempt:
            return attempt
    pass
