
rows = 'ABCDEFGHI'
cols = '123456789'


def cross(a, b):
    return[s + t for s in a for t in b]

boxes = cross(rows, cols)

# This creates a list of 9 lists, where each of the 9 lists is
# a unit. So for each character in the rows string we cross that
# with all of the characters in the cols string. We then return
# this as a list. We then move onto the next character in the rows
# string and return another list.
row_units = [cross(r, cols) for r in rows]

column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]
unitlist = row_units + column_units + square_units

# This creates a dictionary that which associates to each box the
# units that contain the box.
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)

# This creates a dictionary where each element of the dictionary
# is a set containing all of the boxes that are peers to the box
# in question.
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

test = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'

# Takes a string and returns a grid value.
def grid_values(grid):
    char_list = [s for s in grid]
    char_list = [s.replace('.', '123456789') for s in grid]
    tuple_list = list(zip(boxes, char_list))
    return(dict(tuple_list))

values = grid_values(test)

values['A1']
len(values['A1'])

list(values.keys())
sorted(values.keys())

# A dictionary is a set of unordered key:value pairs.

peers['A1']

# The set data structure does not support indexing. So the below returns an error.
peers['A1'][1]
list(peers['A1'])[1]
values[list(peers['A1'])[1]]
values['A6'] = str.replace(values['A6'], '3', '')

# Want to return all of the keys that are associated
# with a single values in the values dictionary.
solved_boxes = [s for s in boxes if len(values[s]) == 1]

def eliminate(values):
    solved_boxes = [s for s in boxes if len(values[s]) == 1]
    for s in solved_boxes:
        elim_value = values[s]
        for r in list(peers[s]):
            values[r] = str.replace(values[r], elim_value, '')

unitlist[0]
unitlist[0][0]
values[unitlist[0][0]]

values[boxes]

temp = [values[box] for box in unitlist[0]]

temp0a = [s for s in temp if len(s) > 1]


temp2 = ''.join(temp)
temp2.count('a')

temp3 = [temp2.count(num) for num in '123456789']
temp4 = [i+1 for i,x in enumerate(temp3) if x == 1]
temp5 = ''.join(map(str, temp4))

for (i, item) in enumerate(temp):
    for j in temp5:
        if j in item:
            temp[i] = j

for num in '123456789':
    print(temp2.count(num))

# Do any numbers only appear once in temp?
# Find numbers that appear once.
# Assign units containing those numbers to be that number.
set(temp)


values_unit = {k:v for k,v in values.items() if k in unitlist[0]}

values['A1'] = 30


for unit in unitlist:
    for box in unit:
        print(values[box])

values[list('A1', 'A2')]

def only_choice(values):
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
                    new_values[key] = j

        return(new_values)



# What do I want to do? I want to create a dictionary with just
# keys A1-A9.

p3 = dict.fromkeys(unitlist[0])
p3 = set(unitlist[0])


p1 = {key:value for key, value in values.items() if key in unitlist[0]}

p1 = {key:value for key, value in values.items() if 'A' in key}

{k:v for}

################################################
# Experiments
################################################

# A set is another type of data structure. A set is an unordered collection
# with no duplicate elements.
# ex.
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# Printing basket automatically removes duplicates.
print(basket)

# This is some good old imperative programming.
myList = []
for s in rows:
    for t in cols:
        myList.append(s + t)

# This is equivalent to the cross(a, b) function using traditional for loops
# instead of list comprehensions.
def cross_test(a, b):
    temp_list = []
    for s in a:
        for t in b:
            temp_list.append(s + t)
    return temp_list

# aList and bList are equivalent
aList = [i for i in range(10)]
for i in range(10):
    myList.append(i)


for i in cols:
    print(i)
d = dict((i,True) for i in [1,2,3])

a = dict((s, cols) for s in rows)

a = [s for s in rows]
b = [s for s in cols]
list = list(zip(a,b))


char_list = [s for s in test]

# This is a way of writing replace(s, '.', 123456789) where s is an
# element of char_list
char_list = [s.replace('.', '123456789') for s in char_list]

for i in len(char_list)

for s in char_list:
    if s == '.':
        s.replace('.', '123456789')

tuple_list = list(zip(boxes, char_list))
temp = dict(tuple_list)

def grid_values(grid):
    char_list = [s for s in grid]
    tuple_list = list(zip(boxes, char_list))
    grid_dict = dict(tuple_list)
    return(grid_dict)
ict((s, t) for s in boxes)
temp = [u for u in unitlist if s in u]
temp_dict = dict([['hash', 'bang'], ['slash', 'dot']])

# This is clearly the syntax being used when defining units.
d = dict((key, value) for (key, value) in iterable)

def display(values):
    """
    Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return


# Possible problem with this is that if we eliminate enough
# some boxes that weren't originally solved already may become
# solved and we may use that now solved box to eliminate other
# values.
def eliminate(values):
    for s in boxes:
        if len(values[s]) == 1:
            elim_value = values[s]
            for r in list(peers[s]):
                values[r] = str.replace(values[r], elim_value, '')


def eliminate(values):
    for s in sorted(values.keys()):
        if len(values[s]) = 1:
            for r in peers[s]:
                replace(values[r], '3', '')





