# paaswrod = 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
import itertools

# Iterate over codee structures with itertools.
# itertools have lot of nice tools.

# You can use itertools to chain [1, 2] and ['a', 'b']

for item in itertools.chain([1, 2], ['a', 'b']):
    print(item)


# Use to cycle [  2, 4, 6] infinitely

"""
for item in itertools.cycle([1,2]):
    print(item)
"""
print(f"\nAccumulate\n\n")
# Accumulate can be used to accumulate the values.
for item in itertools.accumulate([1,2, 3, 4, 7]):
    print(item)


def multiply(a, b):
    return a * b

myitems = [1,2,3,4,5]

# Create a function called multiply return product of two numbers.
# Accumulate using myitems and multiply as a function.
print(f"\nAccumulate Using Multiply\n\n")
for item in itertools.accumulate(myitems, multiply):
    print(item)

