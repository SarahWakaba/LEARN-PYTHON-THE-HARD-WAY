>>> things = ['a', 'b', 'c', 'd']
>>> print things[1]
b
>>> things[1] = 'z'
>>> print things[1]
z
print things
['a', 'z', 'c', 'd']
>>>

>>> stuff = {'name': 'zed', 'age': 36, 'height': 6*12+2}
>>> print stuff['name']
zed
>>> print stuff['age']

>>> print stuff['height']

>>> stuff['city'] = "San Fransisco"
>>> print stuff['city']
San Fransisco


>>> stuff[1] = "wow"
>>> stuff[2] = "Neato"
>>> print stuff[1]
wow
>>> print stuff[2]
Neato

>>> print stuff
{'city': 'San Fransisco', 2: 'Neato', 'name': 'zed', 1: 'wow',
'age': 36, 'height': 74 }


#EXERCISE
cities = {'CA': 'San Fransisco', 'MI': 'detroit', 'FL': 'Jacksonville'}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state):
    if state in themap:
        return themap[state]
    else:
        return "Not found."

#ok pay attention
cities['_find' = find_city]

while True:
    print "State? (Enter to quit)",
    state = raw_input("> ")

    if not state: break

    # this line is the most important ever! study!
city_found = cities['_find'](cities, state)
print city_found
