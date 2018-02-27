# This is a list in python
things = ['a', 'b', 'c', 'd']

things[1] = 'z'

# This is a dict. It's basically the equivalent of a
# named list in R.f
stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' * 10)
print("New York's abbreviation is: ", states['New York'])

# We have the following mapping
# state_names -> abbreviations -> cities


print('-' * 10)
states['Michigan']
print "Michigan has: ", cities[states['Michigan']]


# The below printing method is not going to work in Python 3.5
# for state, abbrev in states.items():
#     print "%s is abbreviated %s" % (state, abbrev)


# A list is for an ordered list of items. A dictionary is for matching some items
# called 'keys' to other items called 'values'. Dictionaries are essentially look-up
# tables. In other languages this dictionary data structure is called an associative
# array.
