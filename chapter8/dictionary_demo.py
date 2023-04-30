"""
8.1 Make an English-to-French dictionary called e2f and print it.
Here are your starter words: dog is chien, cat is chat, and walrus is morse.
"""
import pprint

e2f = {
    "dog" : "chien",
    "cat" : "chat",
    "walrus" : "morse"
}

"""
8.2 Using your three-word dictionary e2f, print the French word for walrus.
"""
print(e2f["walrus"])

"""
8.3 Make a French-to-English dictionary called f2e from e2f. Use the items method.
"""

f2e = {}
for key, value in e2f.items():
    f2e[value] = key

import pprint
pprint.pprint(f2e)

"""
8.4 Print the English equivalent of the French word chien.
"""
print(f2e["chien"])

"""
8.5 Print the set of English words from e2f.
"""
print(set(e2f.keys()))

"""
8.6 Make a multilevel dictionary called life. Use these strings for the topmost keys: 
'animals', 'plants', and 'other'. Make the 'animals' key refer to another dictionary with
 the keys 'cats', 'octopi', and 'emus'. 
 Make the 'cats' key refer to a list of strings with the values 'Henri', 'Grumpy', and 'Lucy'. 
 Make all the other keys refer to empty dictionaries.
"""

life = {
    "animals" : {
        "cats" : ["Henri", "Grumpy", "Lucy"],
        "octopi" : {

        },
        "emus" : {

        }
    },
    "plants" : {

    },
    "other" : {

    }
}


"""
8.7 Print the top-level keys of life.
"""
print(life.keys())

"""
8.8 Print the keys for life['animals'].
"""
print(life["animals"].keys())

"""
8.9 Print the values for life['animals']['cats'].
"""
print(life["animals"]["cats"])

"""
8.10 Use a dictionary comprehension to create the dictionary squares. 
Use range(10) to return the keys, and use the square of each key as its value.
"""
dict_comp = {
    num : num**2 for num in range(1,10)
}
pprint.pprint(dict_comp)

"""
8.11 Use a set comprehension to create the set odd from the odd numbers in range(10).
"""
oddset = {
    num for num in range(1,10) if num % 2 == 1
}
print(oddset)

"""
8.12 Use a generator comprehension to return the string 'Got ' and a number
 for the numbers in range(10). Iterate through this by using a for loop.
"""

"""
8.13 Use zip() to make a dictionary from the key tuple ('optimist', 'pessimist', 'troll')
 and the values tuple ('The glass is half full', 'The glass is half empty', 'How did you get a glass?').
"""
for my_tuple in zip(('optimist', 'pessimist', 'troll'),
                    ('The glass is half full', 'The glass is half empty', 'How did you get a glass?')):
    print(my_tuple)

"""
8.14 Use zip() to make a dictionary called movies that pairs 
these lists: titles = ['Creature of Habit', 'Crewel Fate', 'Sharks On a Plane'] 
and plots = [ 'A nun turns into a monster', 'A haunted yarn shop', 'Check your exits']
"""
titles = ['Creature of Habit', 'Crewel Fate', 'Sharks On a Plane']
plots = [ 'A nun turns into a monster', 'A haunted yarn shop', 'Check your exits' ]

print("\n")
for pair in zip(titles, plots):
    print(pair)