# 18:35
# Completed tasks at 20:02.

# Create a dictionary. use {}
# Create a dictionary called bierce with keys
# day, positive and misfortune.
# Values are A period of twenty-four hours, mostly misspent
# Mistaken at the top of one's voice
# The kind of fortune that never misses

bierece = {
    "day" : "A period of twenty-four hours, mostly misspent",
    "positive" : "Mistaken at the top of one's voice",
    "misfortune" : "The kind of fortune that never misses"
}

print(bierece)

# convert arrays to a dictionary using dict() using tuples or in array of arrays.
# Create the above dictionary  using the dict()
# Create another using pairs a, b  & c,d & e, f . First make the pairs in array, then with tuples.

list_pairs = [['a','b'], ['c','d'], ['e','f']]
list_dict = dict(list_pairs)
print(list_dict)

tuple_pairs = (('a','b'), ('c','d'), ('e','f'))
tuple_dict = dict(tuple_pairs)
print(tuple_dict)


# Accessing items by key.
# Create tuples a, b & c, d & e ,f
# Create a dictionary using dict() function.




# Get an item by [key] or with get()
# Creat a dictionary using {} as follows.
# 'Chapman' => Graham.
# Cleese => John.
# Idle => Eric
# Jones => Terry.
# Plain => Michael.
# Add another item with [] operator. Gillaim to Gerry

pythons = {
    "Chapman" : "Graham",
    "Cleese" : "John",
    "Idle" : "Eric",
    "Jones" : "Terry",
    "Plain" : "Michael"
}

print(pythons)
pythons["Gilliam"] = "Gerry"




# Get all keys with keys()
# Print the keys from above dictionary.

for last_name in pythons.keys():
    print(f"Last Name : {last_name}")

# Get all values with values()
# Prin the items with values function.

print("\n")
for first_name in pythons.values():
    print(f"First Name : {first_name}")

# Get all key value pairs with items()
# Display all the key value pairs with items() function.
print("\n")
for (first,last) in pythons.items():
    print(f"{first} and {last}")

# Combining Dictionaries with update()
# Declare the Chapman dictionary above and combine it what others
# others dictionary as follows Marx => Groucho Howard => Moe.
my_names = {
    "Chapman" : "Graham",
    "Cleese" : "John",
    "Idle" : "Eric",
    "Jones" : "Terry",
    "Plain" : "Michael"
}

other= {
    "Marx" : "Groucho",
    "Howard" : "Moe"
}
my_names.update(other)
print(my_names)

# Purely delete an item with del
# Form the above dicitionary deilete Marx entry with del.

del(my_names["Marx"])
print(my_names)


# Get an item by key and delete with pop()
# Delete and collect the value using pop()
last_name = my_names.pop("Jones")
print(f"lst name is {last_name}")

# Delete all items with clear()
# USe clear() to clear the entire dictionary
my_names.clear()
print(my_names)

# Test for key with in operator.
# Chapman => Graham, Cleese => John, Jones => Terry, Palin => Michael, Idle =< Eric.
# use in operator to test if Chapman is in pythong and if Palin is in Pythons

new_names = dict(chapman="Graham", Clease="John", Jones="Terry", Palin="Michael", Idle="Eric")
if "chapman" in new_names:
    print(f"chapman last name is  {new_names['chapman']}")

# Assing with =
# Declare signals as green => go, yellow => Go faster, red => Smile for the camera.
# Assign signals to save_signals.

# Shallow copy with copy .
# make a copy of the signals using copy. Change one of the value. and verify it
# is changed at both places.
new_names = dict(chapman="Graham", Clease="John", Jones="Terry", Palin="Michael", Idle="Eric")
# Copy is on dicitonary
copied_names = new_names.copy()
copied_names["chapman"] = "Arvind"

print(copied_names)
print(new_names)


# Deep copy with deepcopy()
# declare signals as follows.
# green => go, yellow => go Faster red => stop smile
# make a deep copy of the signals and change the one of the values.
# then print out.
import copy
new_names = dict(chapman="Graham", Clease="John", Jones="Terry", Palin="Michael", Idle="Eric")
deepcopied =copy.deepcopy(new_names)

deepcopied["chapman"] = "Arvind"

print(new_names)
print(deepcopied)

# Declare dictionary as follows.
# accusation as
# room => Ballroom, weapon => Lead Pipe, Person => Col. Mustard.
accusation = {
    "room" : "Ballroom",
    "weapon" : "Lead Pipe",
    "Person" : "Col. Mustard"
}


# Iterate on keys for above dictionary

for type in accusation.keys():
    print(f"Type is {type}")

# Iterate on values for above dictionary
for value in accusation.values():
    print(f" {value}")




# Iterate on items for above dictionary. items() returns key, value pairs.
for type, value in accusation.items():
    print(f"{type} of {value}")

# Create a dictionary using Dictionary Comprehensions .
# declare a string word as "letters".
# Get the letters_count hash key is each letter and number of ocurences of the letter in word.
# This is great.


word = "letters"
letter_count = { letter : word.count(letter) for letter in word  }
print(letter_count)


# Do the same above by converting to set. This will prevent iterating twice.

letter_count = { letter : word.count(letter) for letter in set(word)  }
print(letter_count)

#  Declare vowels as aeiou
# Declare word as onomatopoeia
# Create a set called vowel_counts. Find a count of character which are vowels in the word.

vowels = "aeiou"
word = "onomatopoeia"

vowel_dict = {
    letter : word.count(letter) for letter in set(word)  if letter in vowels
}

print(vowel_dict)



# Delete an item with remove()

# Create with set()

# Convert with set()
# created word called letters and use set and print it.
# COnvert the list 'Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'
# to a set.

word_list = ['Dancer', 'Dancer', 'Prancer', 'Mason-Dixon']
print(set(word_list))



# Get length with len() function
# Create a list called 'Dancer', 'Dancer', 'Prancer', 'Mason-Dixon'
# Convert the list to a set and  find the length

my_list = ['Dancer', 'Dancer', 'Prancer', 'Mason-Dixon']
print(len(set(my_list)))

# Add an item with add() function.
# Declare a set as 1, 2 , 3
# Add 4 to the above set.

my_set = {1,2,3}
my_set.add(4)
print(my_set)


# Delete an item with remove() function.
# remove 3 from the above set.
my_set.remove(3)
print(my_set)

# Test for a value with in
# Declare the set as sofa, ottoman and table. use for in to print the above set.

furniture_set = {
    "sofa",
    "ottoman",
    "table"
}

for item in furniture_set:
    print(f"{item}")


# Complex sets.
# declare drinks as foloows.
# martini => vodka and vermounth
# black russian => vodka and kahlua.
# white russian => cream, kahula and vodka
# ' manhattan' => rye, vermounth and bitters
# secreweddriver as orange juice and vodka

# Iterate with name (key) and contents (values )
# on the above dictionary. if vodka is in the contents, print the values/

drinks = {
    "martini" : ["vodka", "vodka"],
    "black russian" : ["vodka", "kahlua"],
    "white russian" : ["cream", "kahula", "vodka"],
    "Manhattan" : ["rye", "vermounth" , "bitters"],
    "secreweddriver" : ["orange juice", "vodka"]
}

for drink, contents in drinks.items():
    if "vodka" in contents:
        print(contents)

# Combinations and Operators.
# For the above find intersection of contents with {"vermouth", "orange juice"}
# if there is itnersection print th anem.

for drink, contents in drinks.items():
    if {"vermouth", "orange juice"} & set(contents):
        print( "Interseced", contents)

# NEx tiem if there not intersection with {"vermouth", "orange juice"} print the name.
for drink, content in drinks.items():
    if  not {"vermouth", "orange juice"} & set(contents):
        print("Not Intersected", contents)


# Set intersection with & . Example a = {1,2} and b = {2,3}
# a & b will lead 2. or a.intersection(b)


# a = {1,2} and b = {2,3} a union b or a | b is {1,2,3}

a = {1,2}
b = {2,3}
print(a  | b)

# difference() function. a - b or a.difference(b)

# a is subset of b. a.issubset(b)
print(a.issubset(b))

# a is superset of b. a.issupserst(b)
print(a.issuperset(b))

# Set Comprehensions.
# { expression for expression in iterable }
# { expression for expression in iterable if condition }
# Using set comprehension find all multiples of 3 from 1 to 100.

even_nums = { num for num in range(1,100) if num % 2 == 0 }
print(even_nums)

odd_nums = { a_num for a_num in range(50,100) if a_num % 2 == 1 }
print("odd numbers ", odd_nums)

three_set = {number for number in range(1,100) if number % 3 == 0}

print(three_set)
a_set = {number for number in range(1,6) if number % 3 == 1}
print(a_set)


# Immutable sets.

# Big sets
# Declare marxes as 'Groucho', 'Chico', 'Harpo'
# Declare pythons as 'Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin'
# Declare stooges as 'Moe', 'Curly', 'Larry'

# Gernerate the tuple form the above listsa and pritn them.

# From the above lists create list of lists.

# Delcare a dictionary as follows.
# Marxes => marxes, Pythons => pythons and Stooges as stooges

