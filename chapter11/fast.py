from random import choice

# Module is the name of the Python file without .py extension.
# This makes code and variables in the imported module available to your program.

# Declare a list of things.
# "McDonalds", "KFC", "Burger King" ,"Taco Bell", "Wendys", "Arbys", "Pizza Hut"
# Use choice function in randome module to pick a food item.

places = [ "McDonalds", "KFC", "Burger King" ,
           "Taco Bell", "Wendys", "Arbys", "Pizza Hut"
]
def pick():
    return choice(places)

place = pick()
print(f"Place is {place}")

# Number of ways to do import.
# import random
# from random import choice   .
# Import module as another name.
# import fast as f

# Another way to look at module is
# from sources import fast, advice.
# sources is a directory . fast and advice as modules.
