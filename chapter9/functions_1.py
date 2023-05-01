# 1. Simple function. Function should strt with def <name of function>(argument-1, argument_2)
# Example .
# def echo(anything):
#   return anything + " " + anything.



def echo(anything):
    return anything + " " + anything

print(echo("Jaya Guru Datta!!"))



# Write a function called echo which takes parameters
# anythig and return anythig + " " + anything.


# 2.  Write a funciton called commentry which takes parameter color .
# Function will return "It's a tomato." if color is red.
# It's a green pepper if color is green.
# If color is "bee purpl"
# Otherwise Never heard of Color

def commentry(color):
    if color.lower() == "red":
        print(f"It is {color} tomoato.")
    elif color.lower() == "green":
        print(f"This is {color} pepper")
    elif color.lower() == "bee purple":
        print(f"Only bees recoginze {color} pepper")
    else:
        print(f"Never heard of color : {color}")

commentry("red")
commentry("Green")
commentry("Bee Purple")
commentry("Yellow")


# Positional arguments.
# For example if function is like def menu(wine,entree, dessert)
# To Invoke, it has to be either in order or menu(entree="beef", wine="bordeux", dessert="ice cream")

def menu_positional(wine,entree,dessert):
    print(f"Drinking {wine} with Entree {entree} and eating {dessert}")

menu_positional(entree="beef", dessert="Gulab Juman", wine="Bordeaux")



# Specify default parameter values. You can specify default values here.
# menu(wine, entree, dessert="pudding")
# Invoke it like this menu()
# Create a function called emnu which defines menu with argumetns wine , entree and dessert ( default to pudding )
# Invoke menu function with chardonnay and chcike
# Invoke menu function again with dunkelfelder, duck and doughnut

def menu_default(wine, entree, dessert="pudding"):
    print(f"Entree = {entree}, drinking wine {wine} and eating dessert {dessert}")

menu_default("chardonnay", "Chicken")
menu_default("dunkelfelder", "duck", "doughnut")

# Positional arguments with *
# def print_args(*args)
# The values are 3, 2, 1, 'wait!', 'uh...'

def print_args(*args):
    print("Positiona argumetns " , args)

print_args("Hello", "World", "Jaya Guru Datta !!")


# Questoon 2: Create a function called print_more with requried1, required2 and *argxs
# If there are positional argumemnts, it shold be last.
# Invoke the function as 'cap', 'gloves', 'scarf', 'monocle', 'mustache wax'
# Need this one, Need this one too and print the rest of the argumetns.


def print_more(required1, requrired2, *args):
    print(f"Need this One: {required1}")
    print(f"Need this one too: {requrired2}")
    print(f"All the Rest: {args}")


print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')

# You can pass variable number of key-value pairs with keyword arguments.
# Exmaple: def print_keywords(""kwargs): # kwargs is representd as hash.
#               print("Keyword Arguments" , kwargs)
# To invoke the function, use wine="Merlot", entree="Mutton", dessert="macaroon"


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

def echo(first, second):
    """
    :param first:
    :param second:
    :return:
    Prints the first acurment if second argument is ture.
    The operation is:
         1. Check wheter the *second* argument is true.
         2. If it is print the *first* agument.
    """
    if second:
        print(f"This is {first} arument")


# print(help(echo))

# Functions are first class citizens.
# Functions can be sent as parameters.
# Write a function called add_args whcih takes arg1 and arg2
# Write another function called run_something_with_args with takes func ( any function )
# arg1 and arg2 are other arguments.
#  Test it with add_args, write another functions subtract-args, multiply_args and divide-args and test it.

def add_args(a,b):
    return a +b

def subtract_args(a,b):
    return a - b

def multiply_args(a,b):
    return a*b

def run_something_with_args(func, a,b):
    return func(a,b)

x=10
y=5

add_result = run_something_with_args(add_args,x,y)
print(f"Add Result: {add_result}")

diff_result = run_something_with_args(subtract_args,10,5)
print(f"Subtract result : {diff_result}")

mult_result = run_something_with_args(multiply_args,10,5)
print(f"Multiply result : {mult_result}")

# Functions can be returned from another function.
# Wrtie a function called sum_args(*args) which returns sum of all the aguments.
# Create another function called run_with_positional_args(), which takes a funciton and
# any number of positinsl arguments to pass it. run_with_positional_args shold return
# func(*args)



# Inner functions.
# A function can be defined within function and return inner function.
# Write a function called outer which takes arguments a and b
# Within the outer function, define a function called inner which takes c, d and returns c+d.
# Invoke the outer funciton as outer with arguments as 4 , 7

def outer(a,b):
    def inner(c,d):
        return c +d
    return inner(a,b)


result = outer(10,9)
print(f"Result is {result}")


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

def knitghts2(saying):
    def inner2():
        return "We are the Knights who say %s" % saying
    return inner2 # Should return function, and not with (). Don't understand this


a = knitghts2("Hasenpfeffer")
b = knitghts2("Jaya Guru Datta !!")

# Invoke the functions.
print(a())
print(b())


def my_operation(a,b):
    def add_nums(c,d):
        return c +d
    return add_nums(a,b)

result = my_operation(4,8)
print(f"Result is {result}")


# Anonymous function is called lambda .
# A Python lambda function is an anonymous function
# expressed as a single statement. You can use it instead of a normal tiny function.
#  Example:
#   def edit_story(words, func) :
#       for word in words:
#           print(func(word))
# This can be invoked as stairs = ["thud", "meow", "thud", "hiss"]
# def envliven(word):
#     return word.capitailze() + "!"
# Invocation edit_store(stairs envilen)
# Or you can invoke it as .
# edit_store(stairs, lambda word : word.captialize() = "!")

def edit_store(func, words):
    for word in words:
        print(func(word))

stairs = ["thud", "meow", "thud", "hiss"]
edit_store(lambda word : str(word).upper() + "!", stairs)
edit_store(lambda word : word.lower() + " " + word.upper()  , stairs)

# Question. Repeat the question above. write another function which takes two functoin, and pritns both values.
# Invoke it using lambda functions
# Inner functions, will capture outer arguments from the outer function.


# Generator function
# range(1,10) is an inbuilt range function . example sum(range(1,101))
# Every time you iterate using a generator, it keeps track of where it was the last time was called and
# Returns next value. This is different from a normal functoin which has no memory of privous calss and always start at
# first line.
# for iterating a generator, it is for i in ranger:

#  For writing custom generator, you need to use yield .
# Example. create a function called my_range which takes first, last and step defaulting to first = 0
# last = 10 and step = 1, for each iteration, you can do yield.
# Invoke the function as my_range with variables 2, 10 and iterate.

def my_range(first=0, last=11, step=2):
    number = first
    while number < last:
        yield number
        number = number + step


print(list(my_range(10,100,5)))
for num in my_range(11,27,2):
    print(f"Number is {num}")



# Generator comprehensions. For list comprehensiin it is [] , for
# dictionary it is {}, for set it is {}
# For generator use () .
# Example. for two arrays ['a', 'b'] and ['1', 2]. for zip
# (pair for pair in zip(['a', 'b'], ['1', '2']))
# Iterate over this and print the result.

gen_comprehension = (pair for pair in zip(['a', 'b'], ['1', '2']  )  )
for pair in gen_comprehension:
    print(pair)


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
#
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


def document_it(func):
    def new_function(*args, **kwargs):
        print(f"Running Function : {func.__name__}")
        print("Positional Arguments ", *args)
        print("Keyword Arguments ", **kwargs)
        result = func(*args)
        print("Result: " , result)
        return result
    return new_function

# Instead let's do it this way.
# It is the responsibility of the decorator to
# Invoke the function that it is trying to decorate.

def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function





@document_it
@square_it
def add_ints(a,b):
    return a + b

result = add_ints(10,19)
print(f"Final Result is {result}")


# cooler_add_ints = document_it(add_ints)
# cooler_add_ints(3,5)





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

def hello(a,b):
    print("Locals are : ")
    print(locals())

# print(globals())


# The name of the function and it's documentation is stored in the variables.
# __name__ and __doc__
# Write a function called amazing which prints this variables.

def amazing():
    """
    Just used to test the inbuilt variables __name__ and __doc__
    :return:
    """
    print(f"Name of the funciton {amazing.__name__}")
    print(f"Doc string of the function {amazing.__doc__}")


amazing()

# Handling exception.
# to handle exception use try except values.
# example:
# try:
#   short_list[position]
# except:
#   print("Noded position between 0 and", len(short_lst) - 1, "but you got {position}")
# or by the type of exceiption. Go for special to general.
# try
# except IndexError as err:
# except Exception as other

def get_number(position):
    short_list = [4, 5, 9]
    try:
        short_list[position]
    except:
        print("Need a position between 0 and ", len(short_list) -1, " but got ", position)

get_number((7))


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
# if any of the words is upper case throw UpperCaseException

def find_upper_case(*args):
    for mystr in args:
        if str(mystr).isupper():
            raise UpperCaseException()

try:
    find_upper_case('eenie', 'meenie', 'miny', 'MO')
except UpperCaseException as uce:
    print("Upper Case Exception: ", uce)
except Exception as ex:
    print("Normal Exception: ", ex)



# yield from is added in python3.3 which lets generator hand off wome work to another genrator.
# Write a recursive functionc called flatten.
# which will flatten an array [1,2, [3,4,5], [6,[7,8,9]] , [] ]
# This recursive function should use yield from and yield


def flatten(lol):
    for item in lol:
        if isinstance(item,list):
            yield from flatten(item)
        else:
            yield item

for item in flatten([1,2, [3,4,[10,12],5], [6,[7,8,9]] , [] ]):
    print(item)

new_list = list(flatten([1,2, [3,4,5], [6,[7,8,9, [34,99, 101] ]] , [] ]))
print(new_list)