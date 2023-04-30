# Default dictionary can be used to set the default values for int.
from collections import  defaultdict

# Default dictionaries can be used to set the values.
# Assign default dictionary to periodic_table. Assing Hydrogen to 1.
# Print lead.
periodic_table = defaultdict(int)
periodic_table["Hydrogen"] = 101
print(periodic_table["Hydrogen"])
print(periodic_table["Helium"])

def no_idea():
    return "Huh ?"

# You can pass a function to default dictionary.
# Create a function called no_idea which return "Huh ? "
# Assingn Aboinable Snowman to A and
# Assign Basilisk to B. to bestiary to defaultdictionary
# Print the bestiary A , B and C .
bestiary = defaultdict(no_idea) # Should not have a () as it will inovke the function.
bestiary["A"] = "Aboinable Snowman"
bestiary["B"] = "Basilisk"

print(bestiary["B"])
print(bestiary["C"])

# Count Items with counter.

# Counter can take a list of items and display all the values .
# Import the Counter class from collections module
from collections import Counter

# Create a list called breakfast from "spam", "spam", "eggs", "spam"
breakfast = [ "spam", "spam", "eggs", "spam" ]
# Create a counter. From the above list, Create  a dictionary
# Which Summarises keys with values.
breakfast_coutner = Counter(breakfast)
print(breakfast_coutner)

# Most common can be used to get a tuple of the key and values.
print(breakfast_coutner.most_common())

# You can get the most Ocurrences after the 1.
print(breakfast_coutner.most_common(1))


# Two counters can be combined.
# Craete a lunch_counter from the list of lunch items, "eggs", "eggs", "bacon"
# Combine lunch counter with breakfast counter .
lunch_items = ["eggs", "eggs", "bacon"]
lunch_counter = Counter(lunch_items)

# Combine with breakfast coutner with lunch Counter.
combined_counter = breakfast_coutner + lunch_counter
print(combined_counter)

#  You can subtract both the above containers
# Subtract lunch counter from breakfast counter.
subtracted_dict = breakfast_coutner  - lunch_counter
print(subtracted_dict)

# Subtract breakfast coutner from lunch counter.
subtracted_dict = lunch_counter - breakfast_coutner
print(subtracted_dict)

# You can get common items from the intersection opreator.
# Get common items from breakfast counter and lunch Counter.
# USe the & operator.

print (breakfast_coutner & lunch_counter)

# Union Operator is | . Use this to combine breakfast_counter with lunch_counter
print(breakfast_coutner | lunch_counter)

# Ordered Dictionary automatically orders the keys of the dictionary.
from collections import OrderedDict

# Ordered dictionary can automatically sort the keys.
# Ordereed dictionary can take array of Tuples.
# Create a ordered dictionaary from "Moe" => "A wise guy, huh? ",
# Larry => Ow!
# Curly => Nyuk nyuk!
# Print the keys of the ordered dictionary

quotes = OrderedDict([
    ("Moe", "A Wise guy, huh?"),
    ("Larry", "Ow!"),
    ("Curly", "Nyuk nyuk!")
])

# Sor the keys
for stooge in quotes:
    print(stooge)


# Stack + Queue == deque .
# Import deque from Collections module.
# popleft and pop will handle remove from the beginning and from the end.
# Write a method called palindrome which takes a word as parameter.
# IMPort deque from collections module.
# popleft() will remove and give from left.

from collections import  deque

def palindrome(word):

    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

# Test if the palindrome
# is the key .

if palindrome("a"):
    print("a is a palindrome")


if palindrome("radar"):
    print("radar is a palindrome")

if palindrome("racecar"):
    print("racecar is a palindrome")

if palindrome("arvind"):
    print("arvind is a palindrome")
else:
    print("arvind is not a palindrome")
























