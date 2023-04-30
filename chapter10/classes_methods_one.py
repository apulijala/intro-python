# Declare a Cat class. 12:20 PM
# Note taking completed at 14;34 Pm, barring one concept.
# 3:05 PM  started taking.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
# password = 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


from dataclasses import dataclass

# class Cat():
#   Declare a clss called Cat

class Cat():
    pass

cat = Cat()
print(cat)

# With an initializer .
# class Cat()
# For a class to have initializer, you have to take self,
# First parameter should be self. This will have to be used in ohter methods.
#   def __init__(self,name):
#       self.name = name
# Declare a class with a constructor.


class Cat():
    def __init__(self,name):
        self.__name = name

    @property
    def name(self):
        print("In setting the name")
        return self.__name

    @name.setter
    # Should match the getter method name.
    def name(self,name):
        self.__name = name


tomcat = Cat("Tomcat !!")
print(tomcat.name)
tomcat.name = "Great Tomcat !!"
print(tomcat.name)


# Inherit from parent class.
# class Car(); class Yugo(Car) :
# issubclass(Yugo, Car)
# Declare a class using  inheritance

class Car():
    pass

# Yugo inherits from Car .
class Yugo(Car):
    pass

car = Car()
yugo = Yugo()

print( f"Car Is subclass of Yugo? : {issubclass(Car, Yugo)} " )
print( f"Yugo is subclass of Car ? : {issubclass(Yugo, Car)} " )



# Declare a class called Car, declare a subclass called Yugo
# Override method called exclaim.
# Car has a method I'm a Car!
# Yugo has a method I'm a Yugo! Much like a Car, bug more Yugo-like
# Declare objects and start it. Add another method called need_a_push
# Every method in class should have self as the first prameter.
# need_a_push => A little help here?

class Car():
    def exclaim(self):
        print("I'm a car")


class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, bug more Yugo-Like")

    def need_a_push(self):
        print("A little help here? ")


car = Car()
car.exclaim()

yugo = Yugo()
yugo.exclaim()
yugo.need_a_push()


# Superclass with subclass. You can use super(). super() can be used to invoke
# superclass method.
# Declare a class called Person with attributes as name.
# Declare a class called EmailPerson which takes attributes name, email.
# use super class to set name and then set email attribute.
# Create two objects and then print the attribtues of class.

class Person():
    def __init__(self,name):
        self.name = name



class EmailPerson(Person):
    def __init__(self,name, email):
        super().__init__(name)
        self.email = email


person = Person("Arvind")
print(person.name)

emailperson = EmailPerson("Arvind K. Puljala", "arvind.pulijaala@gmail.com")
print(f"Email Person Name: {emailperson.name}")
print(f"Email Person Address: {emailperson.email}")



# Multiple Inheritance.
# You can have mulitple inheritance.
# Declare a class called Animal which has a method called I speak!!
# Declare a class called Horse, which inherits from Animal and returns Neigh!
# Declare a class called Donkey, which returns Hee-Haw
# Create a class called Mule which inherits from Donkey, Horse
# Create a class called Hinny which inherits from Horse, Donkey.
# Invoke says method on Mule and Hinny

class Animal():
    def speak(self):
        print("I speak!!")


class Horse(Animal):
    def speak(self):
        print("Neigh !!")

class Donkey(Animal):
    def speak(self):
        print("Hee-Haw !!")


class Mule(Donkey, Horse):
    pass

class Hinny(Horse, Donkey):
    pass

mule = Mule()
mule.speak()


hinny = Hinny()
hinny.speak()


# Declare a class called PrettyMixin()
# declare a class called dump(self) . It does pprint.pprint(vars(self))
# Declare a class called Thing which inherits from PrettyMixin


# Setting Properties.
# You can declare property as follows.
# Example. property(get_name, set_name). This will invoke the methods when properties.
#  Declare a class called Duck, which has a constructor, which takes input_name as constructor.
# Write method called get_name which prints inside the getter and return the value.
# Write a method called set_name which Prints inside the Setter and sets the property input_name.
# Create a class called Duck, which has input_name as input to constructor.
# Write methods get_name and set_name and set those methods as properties.
# Create an object called don and declare a class and invoke get_name and set_name

class DuckGo():

    def __init__(self,input_name):
        self.hidden_name = input_name

    @property
    def name(self):
        print("Inside the Getter")
        return self.hidden_name

    @name.setter
    def name(self,hidden_name):
        print("Inside the Setter.")
        self.hidden_name = hidden_name



duckgo = DuckGo("Arvind K. Pulijala")
print(f"Name is {duckgo.name}")

# Using Property annotations.
# For the getter method, use @property annotation.
# For the setter method use @<propertyname>.setter . Example @name.setter
# Declare a class called Duck, which takes __init__(self,input_name) as constructor.
# PUt a property called on method name, on the another name method set @name.setter.
# Test it like fowl.name = "Donald" # fowl.name



# Property can have a radius sttribute and it can be computed property.
# Example Circle  can have a method called diameter and annotte is as property. test it.

class Circle():
    def __init__(self,radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2*self.radius


circle = Circle(10.8)
print(f"Diameter of circle : {circle.diameter}")



# Convention is to use __name for private.
# Declare a class called Duck and use @property and @name.setter to
# set the properties. Test it.


# Declare a class called A. which has a class level attribute called count.
# YOu can increment the class level method as A.count += 1
# Write a method called exclaim which prints I'm an A!
# Declare a class method called kids. This can be done with annotation
# as @classmethod. which will have def kids(cls). cls is getting class object.

class A():
    count = 0

    def __init__(self):
        A.count += 1

    def exclaim(self):
        print("I am in A!!")

    @classmethod
    def kids(cls):
        print("A class has ", cls.count, "Little objects.")


a1 = A()
A.kids()
a2 = A()
A.kids()


# Static method defines a method at the class or at the object level.
# It is annotated with @staticmethod
# Write a class called CayoteWeapon() which has a method called
# commerical which prints This CoyoteWeapon has been brought to you by Acme
# It is invoked on the class directly.

class CayoteWeapon():

    @staticmethod
    def commerical():
        print("This Cayote Weapon has been brought to you by Acme.")


CayoteWeapon.commerical()


# Duck typing. Did not understnd this. Need to work out before makeing notes.


# Magic method. To do Comparision, you can use __eq__ this will let us do
# Comparision between objects. example first == second.
# Create a class called Word which declares a constructor and has porpety called text.
# Override a method called __eq__ which does lower case string comparision and returns true or false.
# To determine if objects of two classes are equal.
# this does lower case comparision.
# Override __eq__ other methods are __ne__, __lt__, __gt__, __le__ and __ge__ methods.
# Similarly method are __add__, __sub__, __mul__, __truediv__, __mod__, __pow__

class Text():
    def __init__(self,text):
        self.text = text

    def __eq__(self, other):
        return self.text.lower() == other.text.lower()

    def __repr__(self):
        return "word (" + self.text + ")"

text1 = Text("Arvind")
text2 = Text("arvind")

if text1 == text2:
    print(f"{text1} and {text2} are equal")


# __str__ and __repr__ are represeting some more methods.
# Declare a class called Word. Override __eq__ method,
# __str__ method and __repr__ methods.
# Takes test s a poprerty.
# __eq__, should take word2 as additional parameter.
# __repr__ should say Word( self.txt). Test all the methods.




# Aggregation and Composistion.
# Perform composition to Inheritance.
# Declare  a class called Bill which takes description as the parameter.
# Declare a class called Tail which takes length as parameter.
# Declare a class called Duck() , which takes bill and tail as the parameters.
# Write a method called about(self) Which prints out.
# This duck has a wide orange bill and a long tail

class Tail():
    def __init__(self, length):
        self.length = length

class Bill():
    def __init__(self, description):
        self.description = description


class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail

    def about(self):
        print(f"This duck has a wide {self.bill.description} bill and {self.tail.length} tail.")


bill = Bill("Orange")
tail = Tail("Long")
duck = Duck(bill, tail)
duck.about()


# Named Tuple.
# from collections import namedtuple.
# Create a Named Tuple for Duck with bill and tail.
# Duck = namedtuple("Duck", "bill tail")
# duck = Duck("wide orange", "long")
# Print the named tuple.
# You can also do it with dictionary.
# Example. parts = {"bill" : "wide orange", "tail" : "long" }
# duck2 = Duck(**parts)

from collections import namedtuple
parts = {
    "bill" : "Wide Orange",
    "tail" : "Long"
}

duck2 = Duck(**parts)
print(duck2)

# Dataclasses.
# If a class is just using properties, you can use dataclass.
# Example.
# from dataclasses import dataclass.
# @dataclass
# class TeenyDataClass:
#       name: str
#       age : int
# Usage TeenyDataClass("bitsy", 24)
# teeny = TeenyDataClass("bitsy", 24)
# print(teeny.name) print(teeny.age)
# from dataclasses import dataclass
# Declare a class called AnimalClass:
# with name as str, habitat as str and teeth as integer .
# Declare an object called snowman with AnimalClass attribtues as Yeti, Himalayas, 46 ("Name", "habitat", "age" )
# Print the class.

@dataclass
class AnimalClass:
    name : str
    habitat : str
    teeth : int

snowman = AnimalClass("Yeti", "Himalayas", 46)
print(snowman)

duck = AnimalClass(name="duck", habitat="lake", teeth = 0)
print(duck)

# Take a look at third party package called attrs.





