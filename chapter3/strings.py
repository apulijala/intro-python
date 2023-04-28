# Coments can be in Triple quotes.

'''
Comments are in Triple quotes.
I do not like thee, Doctor Fell.
The Reason why, I connot tell.
But
'''


# Convert Integers and Floats to Strings.
my_num = str(98.6)
print(f"Number is {my_num}")

# Escape with \
palindrome = "A man,\nA Plan,\nAcanal:\nPanama"
print(palindrome)

# Raw Strings. With raw string, \'s are not escaped
info = r"Type a \n to get a new line in a normal string"
print(info)


# Combining Strings using + sign.
kraken = 'Release the Kraken! ' + 'No wait!'
print(kraken)

#
start = 'Na ' * 4 + '\n'
middle = "hey " * 3 + '\n'
end = 'Goodbye.'
print(start + middle + end)

# Letters. You can acess it with index . Negative Index from the reverse.
letters = 'abcdefghijklmnopqrstuvwxyz'

print(letters[0])
print(letters[8])
print(letters[-1]) # From the last.
print(letters[25])

name = "Henny"
# You can replace the string with replace function.
print(name.replace("H", "P"))

# You can get a substring with slice operation.
print("letters from 12 to 15")
print(letters[12:15])
print("letters from 20 character to end")
print(letters[20:])
print(letters[-3:])

print("Start to end in steps of 7 characters")
print(letters[::7])
print("4 to 19 in incements of 3")
print(letters[4:20:3])

# Length o fhte sting len function.
print(len(letters))

# You can use split function to split on the string by the character.
tasks = "get gloves,get mask,give cat vitamins,call ambulance"
print(tasks.split(","))

# Combine using the join function.
crypto_list = ["Yeti", "Bigfoot", "Loch Ness Monster"]
print(",".join(crypto_list))

# Replace the function.
setup = "a duck goes into a bar...."
print(setup.replace("duck", "marmoset"))

# USe strip to remove the spaces in strings. You can also specify character, set of characters for removal.
world = "    earth    "
print(world.strip())
print(world.lstrip())
print(world.rstrip())


blurt = "What the...!!?"
print(blurt.strip('.?!'))

# Use string module to get all possible whitespace and punctuation characters.
import string
# Print all whitespaces.
print("Whitespaces")
print(string.whitespace)

# Print the punctuation.
print("Punctuation")
print(string.punctuation)

poem = '''All that doth flow we cannot liquid name
     Or else would fire and water be the same;
    But that is liquid which is moist and wet
    Fire that property can never get.
    Then 'tis not cold that doth the fire put out
    But 'tis the wet that makes it die, no doubt.'''

print(poem.startswith("All"))
word = "the"
# Will print the position of the string.
print(poem.find(word))
print(poem.index(word))

# Find the position of the string from the right.
print(poem.rfind(word))
print(poem.rindex(word))

# Count the number of occurences.
print(f"Number of occurences")
print(poem.count(word))

# Converting to lower, upper and using title.
setup = "a duck goes into the bar"
print(setup.title())

# COnvert to upper.
print(setup.upper())

# Change case from one to another.
print(setup.upper().swapcase())

# String formatting.
actor = 'Richard Gere'
cat  = 'Chester'
weight = 28
print("Our cat %s weighs %s pounds "%( cat, weight))

# Left and Right Formatting.
thing = 'woodstuck'

# Left and Right Formatting. woodstuck ( 8 characters ) . %12s will add 4 characters %12s will
# Add 4 characrters to the left.
# %-12s will add 4 characters to the right.

print('%12s'% thing)
print('%-12s'% thing)

# It can be same with d ( for decimal )
thing = 9876
print('%d' % thing)
print('%12d' % thing)
print('%-12d' % thing)


# New Formatters are with :10s and use {} braces.
thing = 'wraith'
place = 'window'
print("The {} is at the {}".format(thing, place))
print("The {:10s} is at the {}".format(thing, place))
# Right alignment.
print("The {:>10s} is at the {}".format(thing, place))
# Left Alignment.
print("The {:<10s} is at the {}".format(thing, place))
# Center Alignment.
print("The {:^10s} is at the {:>10s}".format(thing, place))
# Surround with ! on the string
print("The {:!^10s} is at the {:!>10s}".format(thing, place))


# Newest Strings are f strings.
thing = 'wereduck'
place = 'werepond'
print(f"The {thing} is in the {place}")

# Alignment in space. :> for right alignmetn, :< for left alignment.
# :^ is for center alignment. To surround with a character :.^
print(f"The {thing:>20s} is in the {place:.^20s}")