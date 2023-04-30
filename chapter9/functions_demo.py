# 1. Simple function. Function should strt with def <name of function>(argument-1, argument_2)
# Example .
# def echo(anything):
#   return anything + " " + anything.

# Write a functoin called echo which takes parameters anythig and return anythig + " " + anything.

def echo(anything):
    return anything + " " + anything

result = echo (anything="Jaya Guru Datta!! ")
print(result)


# 2.  Write a funciton called commentry which takes parameter color .
# Function will return "It's a tomato." if color is red.
# It's a green pepper if color is green.
# If color is "bee purpl"
# Otherwise Never heard of Color

def comentry(color):
    if color.lower() == "red":
        return "It's a tomato"
    elif color.lower() == "green":
        return "It's green pepper"
    elif color.lower() == "bee purple":
        return "It's Bee Color"
    else:
        return "Never Heard of Color"

result = comentry("red")
print(result)


# Positional arguments.
# For example if function is like def menu(wine,entree, dessert)
# To Invoke, it has to be either in order or menu(entree="beef", wine="bordeux", dessert="ice cream")

# Specify default parameter values. You can specify default values here.
# menu(wine, entree, dessert="pudding")
# Invoke it like this menu()
# Create a function called emnu which defines menu with argumetns wine , entree and dessert ( default to pudding )
# Invoke menu function with chardonnay and chcike
# Invoke menu function again with dunkelfelder, duck and doughnut

def menu(wine, entree, dessert="pudding"):

    print("Menu for Dinner is ")
    print(f"Wine is {wine}")
    print(f"Dessert is {dessert}")
    print(f"Entree is {entree}")



menu(entree="Chicken", wine="Blue")


# Positional arguments with *
# def print_args(*args)
# The values are 3, 2, 1, 'wait!', 'uh...'
# Questoon 2: Create a function called print_more with requried1, required2 and *argxs
# If there are positional argumemnts, it shold be last.
# Invoke the function as 'cap', 'gloves', 'scarf', 'monocle', 'mustache wax'

def print_more(required1, required2, *args):
    print(f"Requried 1 is {required1}")
    print(f"Required 2 is {required2}")
    print("Rest are ")
    for arg in args:
        print(f"Rest is {arg}")

print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')



# You can pass variable number of key-value pairs with keyword arguments.
# Exmaple: def print_keywords(""kwargs): # kwargs is representd as hash.
#               print("Keyword Arguments" , kwargs)
# To invoke the function, use wine="Merlot", entree="Mutton", dessert="macaroon"
def print_keywords(**kwargs):
    print(kwargs)

print_keywords(wine="Merlot")

# Good practice not to modify the value. Instead return the new value.
# Write a functoin called mangle which takes argument called arg.
# The array is outside = ["one", "fine", "day"]
# arg[1] = 'terrible!!'


# doctring is used to document the function.
# '''
# Prints the first argument  if a second argument is true.
#   The operation is:
#       1. Check whether the *second* argument is true.
#       2.  If it is, print the *first* argument
# '''
# To print the doc string print using the help(echo) function.

def help(first, second):
    '''
    :param first:
    :param second:
    :return:
    The operation is :
    1. Check wheter the *second* argument is true.
    2. If it is, print the *first* argument.
    '''
    if second:
        print(first)


print(help.__name__)
print("Documentation ")
print(help.__doc__)


# Functions are first class citizens.
# Functions can be sent as parameters.
# Write a function called add_args whcih takes arg1 and arg2
# Write another function called run_something_with_args with takes func ( any function )
# arg1 and arg2 are other arguments.
#  Test it with add_args, write another functions subtract-args, multiply_args and divide-args and test it.

def add_args(first, second):
    return first +second

def subtract_args(first, second):
    return first - second

def run_something(func, *args):
    print( f"Running {func.__name__} with {args}")
    return func(*args)


result = run_something(add_args, 4, 2)
print(f"Result is {result}")

result = run_something(subtract_args, 4, 8)
print(f"Result is {result}")


# Functions can be returned from another function.
# Wrtie a function called sum_args(*args) which returns sum of all the aguments.
# Create another function called run_with_positional_args(), which takes a funciton and
# any number of positinsl arguments to pass it. run_with_positional_args shold return
# func(*args)



# Inner functions.
# A function can be defined within function and return inner function.
# Write a function called outer which takes arguments a and b
# Within the outer function, define a function called inner which takes c, d and returns c+d.
# Invoke the outer funciton as outer with arguments as 4 , 7, Function return an inner function.

def outer(a,b):
    def inner(c,d):
        return c + d
    return inner(a,b)

print(f"Result is {outer(10,9)}")


# Clousres.
# An Inner funciton can act as closure.
# This is a function that is dynamically generated by another function.
# Outer function captures the arguments from outer funciton
# def knigts2(saying):
#   def inner2():
#       return "We are the knights who say: '%s' ", saying # Saying is captured from outer function.
# generate two funcitons by calling knigts2 with Duck assign it to a, then invoke with Hasenpfeffer
# Assign it to b. Then invoke a and b . Point to note is . Hasenpfeffer and Duck are captured after the funciton
# is returned. This concept is called closure.


def knights2(saying):
    def inner():
        return "We are the knights who are saying %s" % saying
    return inner


a = knights2("Jaya Guru Datta !!")
b = knights2("Om Namo Hanumate Namaha !! ")
c = knights2("Om Aim Hreem Shreem Kleem Sree Mathre Namaha !!")
print(a())
b()
print(c())


# Anonymous function is called lambda .
# A Python lambda function is an anonymous function
# expressed as a single statement. You can use it instead of a normal tiny function.
#  Example:
#   def edit_story(words, func) :
#       for word in words:
#           print(func(word))


# First do with proper function, then with lambda function.

def edit_story(words, func):
    for word in words:
        print(func(word))

def enliven(word):
    return str(word).capitalize() + "!!"

stairs  = ["thud", "meow", "thud", "hiss"]
edit_story(stairs, enliven)


# This can be invoked as stairs = ["thud", "meow", "thud", "hiss"]
# def envliven(word):
#     return word.capitailze() + "!"
# Invocation edit_store(stairs envilen)
# Or you can invoke it as .
# edit_store(stairs, lambda word : word.captialize() = "!")

edit_story(stairs, lambda word : "!!" + word.lower() + "!!" )


# Question. Repeat the question above. write another function which takes two function, and pritns both values.
# Invoke it using lambda functions
# Inner functions, will capture outer arguments from the outer function.


# Generator function
# range(1,10) is an inbuilt range function . example sum(range(1,101))
# Every time you iterate using a generator, it keeps track of where it was the last time was called and
# Returns next value. This is different from a normal function which has no memory of previous class
# and always start at first line.
# for iterating a generator, it is for i in ranger:



#  For writing Custom generator, you need to use yield .
# Example. create a function called my_range which takes first, last and step defaulting to first = 0
# last = 10 and step = 1, for each iteration, you can do yield.
# Invoke the function as my_range with variables 2, 10 and iterate on the result.

def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step


for j in my_range(40, 45, 3):
    print(f"j is {j}")



# Generator comprehensions. For list comprehensiin it is [] , for
# dictionary it is {}, for set it is {}
# For generator use () .
# Example. for two arrays ['a', 'b'] and ['1', 2]. for zip
# (pair for pair in zip(['a', 'b'], ['1', '2']))
# Iterate over this and print the result.

for pair in (pair for pair in zip(['a', 'b'], ['c', 'd'] )):
    print(f"Pair is {pair}")



# Decorator.
# Can be illustrated with example.
# def document_it(func):
#     def new_function(*args, **kwargs)
#       print("Running fucntion ", func.__name__)
#       print("Positional arguments:", *args)
#       print("Keyword arguments:", **kwargs)
#       result = func(*args, **kwargs)
#       print("Result :"  , result)
#       return result
#   return new_function

def document_it(func):
    def new_function(*args, **kwargs):
        print("Running Function ", func.__name__)
        print("Position arguments", *args)
        print("Keyword arguments", **kwargs)
        result = func(*args, **kwargs)
        print(f"Result is {result}")
        return  result
    return new_function # Should not have () . It should be normal function.


#   def add_ints(a,b):
#       return a + b
#   To use it .
#   cooler_add_ints = document_it(add_ints)
#   Finally invoke it as
#   cooler_add_ints(3,5) # 3 and 5 will be passed as args. to inner_funciton new_function
# Instead of doing this you can do
#
#   @document_it
#   def add_ints(a,b)
# and then normal invocation add_ints(3,5)

@document_it
def add_ints(a,b):
    return a + b

result = add_ints(10, 21)
print(f"Result returned is {result}")




# Another demonstration of the decorator
# define a function called square_it which takes func as argument.
# returns inner fucniotn called new_function which returns new_funcion
# result = func(*args,**kwargs); resturn result *r esult.  and return enw_function from square_it
# Create a functionc called add_its which takes a and b as arguments
# Anootatte with @document_it followed by @quare_it
# Reverse the annotation order


# Locals and Globals.
# locals() reutrns a dicitonary of contents of local namespace . Usually function
# globals() will return a dictionary of cotnents of global namespace.
# test theam
# Write a fucntion which tests locals and in the same file print globals()



# The name of the function and it's documentation is stored in the variables.
# __name__ and __doc__
# Write a function called amazing which prints this variables.

# Handling exception.
# to handle exception use try except values.
# example:
# try:
#   short_list[position]
# except:
#   print("Node position between 0 and", len(short_lst) - 1, "but you got {position}")
# or by the type of exception. Go for special to general.
# try
# except IndexError as err:
# except Exception as other

short_list = ["hello", "world"]
position = 2
try:
    short_list[position]
except:
    pass




# You can catch multiple exceptions
# decleare a short_list with values 1,2 and 3 .
# In a look


# Make your own excpetions.
# class UpperCaseException(Exception) : # Inheriting from exception.
# psss
class UpperCaseException(Exception):
    pass

# For raising exceptions you call raise function.
# declare an array of words
# 'eenie', 'meenie', 'miny', 'MO'
# if any of the words is upper case thwro UpperCaseException

def upper_case(words):
    for word in words:
        if word.upper() == word:
            raise UpperCaseException()
        else:
            print(f"word is {word}")

words = ['eenie', 'meenie', 'miny', 'MO']
try:
    upper_case(words)
except UpperCaseException as e:
    print("Upper case exception")

# yield from is added in python3.3 which lets generator hand off wome work to another genrator.
# Write a recursive functionc called flatten.
# which will flatten an array [1,2, [3,4,5], [6,[7,8,9]] , [] ]
# This recursive function should use yield from and yield

def flatten(lol):
    for item in lol:
        if isinstance(item, list):
            yield  from flatten(item)
        else:
            yield item

my_list = [1,2, [3,4,5], [6,[7,8,9]] , [] ]
for item in flatten(my_list):
    print(item)

print("Flattened List ")
print(list(flatten(my_list)))

