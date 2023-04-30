from random import  choice

places = [
    "McDonald's",
    "KFC",
    "Burger King",
    "Taco Bell",
    "Wendys",
    "Arbys",
    "Pizza Hut"
]

def pick():
    import random
    return random.choice(places)