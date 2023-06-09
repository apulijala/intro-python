"""
10.1 Make a class called Thing with no contents and print it.
Then, create an object called example from this class and also print it. Are the printed values the same or different?
"""

class Thing():
    pass

print(Thing)

thing = Thing()
print(thing)

"""
10.2 Make a new class called Thing2 and assign the value 'abc' 
to a class attribute called letters. Print letters.
"""

"""
10.3 Make yet another class called, of course, Thing3. 
This time, assign the value 'xyz' to an instance (object) attribute called letters. 
Print letters. Do you need to make an object from the class to do this?
"""

"""
10.4 Make a class called Element, with instance attributes name, symbol, and number. Create an object of this class with the values 'Hydrogen', 'H', and 1.
"""

"""
10.5 Make a dictionary with these keys and values: 'name': 'Hydrogen', 'symbol': 'H', 'number': 1. Then, create an object called hydrogen from class Element using this dictionary.
"""

"""
10.6 For the Element class, define a method called dump() 
that prints the values of the object’s attributes (name, symbol, and number).
 Create the hydrogen object from this new definition and use dump() to print its attributes.
"""

"""
10.7 Call print(hydrogen). In the definition of Element, change the name of the method dump to __str__, create a new hydrogen object, and call print(hydrogen) again.
"""

"""
10.8 Modify Element to make the attributes name, symbol, and number private. Define a getter property for each to return its value.
"""

"""
10.9 Define three classes: Bear, Rabbit, and Octothorpe. For each, define only one method: eats(). This should return 'berries' (Bear), 'clover' (Rabbit), or 'campers' (Octothorpe). Create one object from each and print what it eats.
"""

"""
10.10 Define these classes: Laser, Claw, and SmartPhone. 
Each has only one method: does(). 
This returns 'disintegrate' (Laser), 'crush' (Claw), or 'ring' (SmartPhone). 
Then, define the class Robot that has one instance (object) of each of these.
 Define a does() method for the Robot that prints what its component objects do.
"""