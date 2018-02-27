
grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
hard_grid = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'

# Convert diag_grid into a dictionary.
values = grid_values(diag_grid)
values = grid_values(grid)
values = grid_values(hard_grid)
unitlist = row_units + column_units + square_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

values = grid_values(grid)

# Diagonal sudoku grid.
diag_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
values = grid_values(diag_grid)

# Display in grid format.
display(values)

# Run eliminate function. This works for diagonal sudoku now because we added
# the two diagonals to the 'units' and 'peers'. The eliminate function loops
# through all of the (solved) squares in the values dictionary and eliminates
# the valued in those solved squares from all of the solved squares peers, which
# in this case includes the diagonal units. However this is not sufficient to
# completely solve the suduko.
eliminate(values)

# This loops through all of the units and if it finds in a particular unit
# that there is only one occurence of a particular value in that unit that
# we assign that value to be the value of the square in which it occurs. This
# does not modify the values list but return an updated value list.
new_values = only_choice(values)

# We then call reduce_puzzle which repeatedly runs eliminate and
# only_choice until the puzzle can't be reduced anymore. Sometimes
# this is enough to completely solve a puzzle. Other times it is not
# sufficient. The harder the sudoku the less likely just using elimination
# and only_choice will be sufficient to solve the puzzle. For example
# for hard_grid the puzzle can't be solved with just these two techniques.
reduce_values = reduce_puzzle(values)



    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers

    # What are naked twins?
    # When two boxes in the same unit have two values that are both the
    # same we can eliminate those two values from all the other boxes
    # in that unit.

    # How am I going to do this?
    # Definitely need to loop through unitlist.
    # For each unit need to check if there are any twin pairs and return
    # the values of the pair.
    Find all pairs in unit.
    So we have all the pairs in a unit. We want to check if any two
    of the pairs in this dictionary are the same
    Do set of all pairs.
    If one of the pairs is the same return the value of that pair.
    Eliminate that pair of values from all the other values in that unit.



        for box in elim_units:
            values[box] = str.replace(values[box], elim_values, '')

temp = [v for v in pairs.values()
                if set(v) in [set(s) for s in pairs.values() if s != v]]


pairs = [box for box in unit if len(values[box]) == 2]
pairs = [values[box] for box in unit if len(values[box]) == 2]
pairs = {k:set(v) for k,v in values.items() if k in unit and len(v) == 2}
pairs = {k:v for k,v in values.items() if k in unit and len(v) == 2}


list(itertools.product(temp, temp))

temp = pairs.keys()
cross(temp, temp)

        naked_twins = {k:v for k,v in pairs.items()
                       if set(v) in [set(s) for s in pairs.values() if s != v]}


set

        for i in range(len(pairs)-1):
            if set(pairs[i][1]) == set(pairs(i+1)[1]):
                print(pairs[i][1])



        set(pairs)

values['A1'] = '47'
values['A2'] = '74'
values['A3'] = '58'


before_naked_twins_1 = {'I6': '4', 'H9': '3', 'I2': '6', 'E8': '1', 'H3': '5', 'H7': '8', 'I7': '1', 'I4': '8',
                            'H5': '6', 'F9': '7', 'G7': '6', 'G6': '3', 'G5': '2', 'E1': '8', 'G3': '1', 'G2': '8',
                            'G1': '7', 'I1': '23', 'C8': '5', 'I3': '23', 'E5': '347', 'I5': '5', 'C9': '1', 'G9': '5',
                            'G8': '4', 'A1': '1', 'A3': '4', 'A2': '237', 'A5': '9', 'A4': '2357', 'A7': '27',
                            'A6': '257', 'C3': '8', 'C2': '237', 'C1': '23', 'E6': '579', 'C7': '9', 'C6': '6',
                            'C5': '37', 'C4': '4', 'I9': '9', 'D8': '8', 'I8': '7', 'E4': '6', 'D9': '6', 'H8': '2',
                            'F6': '125', 'A9': '8', 'G4': '9', 'A8': '6', 'E7': '345', 'E3': '379', 'F1': '6',
                            'F2': '4', 'F3': '23', 'F4': '1235', 'F5': '8', 'E2': '37', 'F7': '35', 'F8': '9',
                            'D2': '1', 'H1': '4', 'H6': '17', 'H2': '9', 'H4': '17', 'D3': '2379', 'B4': '27',
                            'B5': '1', 'B6': '8', 'B7': '27', 'E9': '2', 'B1': '9', 'B2': '5', 'B3': '6', 'D6': '279',
                            'D7': '34', 'D4': '237', 'D5': '347', 'B8': '3', 'B9': '4', 'D1': '5'}
   
