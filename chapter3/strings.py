# Coments can be in Triple quotes.

'''
Comments are in Triple quotes.
I do not like thee, Doctor Fell.
The Reason why, I connot tell.
But
'''


# Convert Integers and Floats to Strings. Convert 98.6 to string.
my_num = str(98.6)
print(f"Number is {my_num}")

# Escape with \. Declare a string called palindrome, A man, followed by newline,
# Followed by A Plan, followed by new line
# print A man, A Plan, A Canal and A Panama all on new lines.
palindrome = "A man,\nA Plan,\nAcanal:\nPanama"
print(palindrome)

# Raw Strings. With raw string, \'s are not escaped
info = r"Type a \n to get a new line in a normal string"
print(info)


# Combining Strings using + sign.
# Strings can be combined using + operator.
# Concatenate the strings Release the Kraken! with No wait!
kraken = 'Release the Kraken! ' + 'No wait!'
print(kraken)

# String Multiplication.
# Assign 'Na ' multipleid by 4 and assign to start. middle to be assigned to string 'hey' 3 times.
# Assign 'Goodybye. ' to end . Concatenate the Strings start, middle and end and
# print it.
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

# Declare "Henry" to variable called name.
# Replace "H" with P
name = "Henny"
print(name.replace("H", "P"))

# You can get a substring with slice operation.
# declare letters variable as 'abcdefghijklmnopqrstuvwxyz'
# Use slice operator to print letters from 12 to 15
# use slice opeartor from 20 to end.
# use slice oepartor to print letters from -3 to end.
# USe slice operator to get string from start to end in steps of 7 .
# USe slice operator from 4 to 20 in steps of 3.

print("letters from 12 to 15")
print(letters[12:15])
print("letters from 20 character to end")
print(letters[20:])
print(letters[-3:])

print("Start to end in steps of 7 characters")
print(letters[::7])
print("4 to 19 in incements of 3")
print(letters[4:20:3])

# len function to print length of string.
# use len to print the length of string letters
print(len(letters))

# You can use split function to split on the string by the character.
# Declare a string called get gloves,get mask,give cat vitamins,call ambulance
# Use split operator to split using the , operator.

tasks = "get gloves,get mask,give cat vitamins,call ambulance"
print(tasks.split(","))

# Declae an array called "Yeti", "Bigfoot", "Loch Ness Monster"
# use : or , to joiin the array.
crypto_list = ["Yeti", "Bigfoot", "Loch Ness Monster"]
print(",".join(crypto_list))

# Replace the function.
# Declare a string called a duck goes into a bar....
# USe replace function to replace duck with marmoset.
setup = "a duck goes into a bar...."
print(setup.replace("duck", "marmoset"))

# USe strip to remove the spaces in strings. You can also specify character, set of characters for removal.
# Delcare a string called "  earth   "
# use strip to remove white spaces  .
# use lstrip to remove the wihite space from left side.
# use rstriop to remve the white space from right side.

world = "    earth    "
print(world.strip())
print(world.lstrip())
print(world.rstrip())

# Strip function can take parametes.
# Declare a string called What the...!!?
# Remove ".?!" using the strip funciton.

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

# startswith, find, index, rfind, rleft, count
# For the above string check if it starts with All.
# delcare a word called "the"
# use find and index to find the word "the"
# use rfind and rindex to fidn the word "the"
# use count  to find number of occurences of string "the"


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
print(poem.count(word))\

# Converting to lower, upper and using title.
# Declare a string called setup a duck goes into the bar
# Print the title of the above string, uppercase string, use swapcase()
setup = "a duck goes into the bar"
print(setup.title())

# COnvert to upper.
print(setup.upper())

# Change case from one to another.
print(setup.upper().swapcase())

# String formatting.
# Use old style formatting to
# print the string .
# Our cat <Name of Cat > weighs < weight > pounds

actor = 'Richard Gere'
cat  = 'Chester'
weight = 28
print("Our cat %s weighs %s pounds "%( cat, weight))

# Left and Right Formatting.
thing = 'woodstuck'

# Left and Right Formatting. woodstuck ( 8 characters ) . %12s will add 4 characters %12s will
# Add 4 characrters to the left.
# %-12s will add 4 characters to the right.
# declare a thing as woodstock use woodstock to left format and then right format.

print('%12s'% thing)
print('%-12s'% thing)

# It can be same with d ( for decimal ). Format 9876 to 12 left
# and 12 to right.

thing = 9876
print('%d' % thing)
print('%12d' % thing)
print('%-12d' % thing)


# New Formatters are with :10s and use {} braces.
thing = 'wraith'
place = 'window'
# declare two variables as thing = wraith and place as window.
# use {} and format to do the following.
# 1. {} to format m {:10s} to format,
# 2. {} with >10s right alighent,
# 3. {} with :<10s to do the left alignment.
# 4. ^10s to do middle formatting.
# 5. use ! to format with the string with ! instead of spaces.

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
# declare a varable thing as wereduck
# declare a variable place as werepond
# use f string to print The wreduci in the wrerepond.

thing = 'wereduck'
place = 'werepond'
print(f"The {thing} is in the {place}")

# Alignment in space. :> for right alignmetn, :< for left alignment.
# :^ is for center alignment. To surround with a character :.^
print(f"The {thing:>20s} is in the {place:.^20s}")

# lower, upper, swapcase, title()
# center(), ljust(), rjust()