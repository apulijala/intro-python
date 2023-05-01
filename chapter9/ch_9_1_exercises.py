"""
9.1 Define a function called good() that returns the following list: ['Harry', 'Ron', 'Hermione'].
"""
def good():
    return ["Harry", "Ron", "Hermione"]

result = good()
print(result)

"""
9.2 Define a generator function called get_odds() that 
returns the odd numbers from range(10). Use a for loop to find and print the third value returned.
"""

def get_odds():
    for num in range(1,10):
        if num % 2 == 1:
            yield num

# print(list(get_odds()))
odd_range = list(get_odds())

for i in range(0,3):
    if i == 2:
        print(odd_range[2])

"""
9.3 Define a decorator called test that prints 'start' 
when a function is called, and 'end' when it finishes.
"""

def test(func):
    def my_decorator(*args):
        print("Start !!")
        result = func(*args)
        print(f"Result is {result}")
        print("End it !!")
    return my_decorator

@test
def sum_numbers(a,b):
    return a + b

sum_numbers(7,19)

"""
9.4 Define an exception called OopsException. 
Raise this exception to see what happens. 
Then, write the code to catch this exception and print 'Caught an oops'.
"""

class OopsException(Exception):
    pass

def raise_new_exception():
    raise OopsException

try:
    raise_new_exception()
except OopsException as oex:
    print(oex)

