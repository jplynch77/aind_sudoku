assignments = []

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a + b for a in A for b in B]
    pass

rows = 'ABCDEFGHI'
cols = '123456789'

boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
diagonal_unit1 = [''.join(d) for d in list(zip(rows, cols))]
diagonal_unit2 = [''.join(d) for d in list(zip(rows, cols[::-1]))]
diagonal_units = [diagonal_unit1, diagonal_unit2]

unitlist = row_units + column_units + square_units + diagonal_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.

    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'.
    If the box has no value, then the value will be '123456789'.
    """

    # This turns the grids string into a list of individual characters
    char_list = [s for s in grid]
    char_list = [s.replace('.', '123456789') for s in char_list]

    # This zips together the list of sudoko boxes and grid characters
    # and returns a list of tuples.
    tuple_list = zip(boxes, char_list)

    # Converts the list of tuples to a dictionary
    return dict(tuple_list)
    pass

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return
    pass

def eliminate(values):
    """
    Eliminates values of solved boxes from their peers.

    Args:
        values(dict): The sudoku in dictionary form.
    Returns:
        A suduko in dictionary form with some possibilities eliminated.
    """
    solved_boxes = [s for s in boxes if len(values[s]) == 1]
    for s in solved_boxes:
        elim_value = values[s]
        for r in list(peers[s]):
            assign_value(values, r, str.replace(values[r], elim_value, ''))

    return(values)
    pass

def only_choice(values):
    """
    Loops through all units in the sudoku and assigns boxes a value when that
    is the only possible value for the box.

    Args:
        values(dict): The sudoku in dictionary form.
    Returns:
        A suduko in dictionary form with some possibilities eliminated.
    """
    new_values = values.copy()

    for unit in unitlist:
        # Create a single string of all values in first unit.
        values_list = [values[box] for box in unit]
        values_string = ''.join(values_list)

        # Creates a list of counts of the numbers 1-9 in values_string.
        count = [values_string.count(num) for num in '123456789']

        # Returns the position of the items in count + 1 if the items
        # are equal to one, i.e. if there are only one of those numbers
        # in the unit.
        single_values = [i+1 for i,item in enumerate(count) if item == 1]

        # Converts single values list to a string.
        single_values_string = ''.join(map(str, single_values))

        # Subset dictionary
        values_unit = {k:v for k,v in values.items() if k in unit}

        # Replace values.
        for key, value in values_unit.items():
            for j in single_values_string:
                if j in value:
                    assign_value(new_values, key, j)

    return(new_values)
    pass

def reduce_puzzle(values):
    """
    Runs elimination and only_choice functions in a loop until the puzzle or is
    solved or can't be reduced further.

    Args:
        values(dict): The sudoku in dictionary form.
    Returns:
        A suduko in dictionary form with some possibilities eliminated.
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        values = eliminate(values)
        values = only_choice(values)

        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values
    pass

def search(values):
    """
    This function uses DFS combined with the reduce_puzzle function to search through
    possible sudoku's in an efficient way and then reduce them to a solution.

    Args:
        values(dict): The sudoku in dictionary form.
    Returns:
        A solved sudoku.
    """
    values = reduce_puzzle(values)

    if values is False:
        return False
    if all(len(values[s]) == 1 for s in boxes):
        return values

    # choose a square with few possibilities then reduce puzzle
    value_list = [v for k,v in values.items() if len(v) != 1]
    min_length = min(list(map(len, value_list)))

    subset_dict = {k:v for k,v in values.items() if len(v) == min_length}
    box_choice = list(subset_dict.keys())[0]

    for value in values[box_choice]:
        new_suduko = values.copy()
        assign_value(new_suduko, box_choice, value)
        attempt = search(new_suduko)
        if attempt:
            return attempt
    pass

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    for unit in unitlist:
        # Find all values of length 2 in unit.
        pairs = {k:v for k,v in values.items() if k in unit and len(v) == 2}

        # Return naked twin boxes as a dictionary
        naked_pairs = {k:v for k,v in pairs.items() if v in [r for s,r in pairs.items() if s!= k]}

        # Extract values from naked twins to remove.
        elim_nums = ''.join(set(''.join(list(naked_pairs.values()))))

        # Create list of units excluding naked twins to loop through.
        elim_units = [box for box in unit if box not in naked_pairs.keys()]

        # Remove naked twins values from other boxes in unit.
        for elim_num in elim_nums:
            for box in elim_units:
                assign_value(values, box, str.replace(values[box], elim_num, ''))
    return values
    pass

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    return search(grid_values(grid))

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
