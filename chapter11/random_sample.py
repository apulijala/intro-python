# Random has many methods
# import choice from random module.
# choice method can return one of the values.
import random
from random import  choice
# from the list of values of 23, 9, 46, 'Arvind', 0x123abc
# print choice of the values
print(choice([23, 9, 46, 'Arvind', 0x123abc]))


# Print the choice of values from tuple 'a', 'one', 'and-a', 'two'
print(choice(('a', 'one', 'two')))

# Choice can be applied to any sequence.
# print the choice from "alphabet"
print("Alphabet choice")
print(choice("alphabet"))

# Import sample from random module.
# sample list will return the values.
# sample(itreator, <number>)

from random import  sample
print(sample( [23,4,5, 'bacon'], 3 ))

# Choose random integer from random.
# randint method .
# Print random integer between 38 -- 74
#
print("Random integer")
print(random.randint(34,67))



# Simple random() function can return a float.
from random import  random
print("Random float number")
print(random())




