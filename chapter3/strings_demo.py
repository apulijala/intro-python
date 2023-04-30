# Coments can be in Triple quotes.

'''
Comments are in Triple quotes.
I do not like thee, Doctor Fell.
The Reason why, I connot tell.
But
'''


# Convert Integers and Floats to Strings. Convert 98.6 to string.
print(str(98.6))

# Escape with \. Declare a string called palindrome, A man, followed by newline,
# Followed by A Plan, followed by new line
# print A man, A Plan, A Canal and A Panama all on new lines.

# Raw Strings. With raw string, \'s are not escaped

newline_str = "A Plan\nA Canal\nA Panama"
print(newline_str)




# Combining Strings using + sign.
# Strings can be combined using + operator.
# Concatenate the strings Release the Kraken! with No wait!

mystr = "Realease the Karken! " + "No Wait!"
print(mystr)

# String Multiplication.
# Assign 'Na ' multipleid by 4 and assign to start. middle to be assigned to string 'hey' 3 times.
# Assign 'Goodybye. ' to end . Concatenate the Strings start, middle and end and
# print it.

start = "No " * 4
middle = " hey" * 3
end = " Goodbye. "
print(start + middle + end)



# Letters. You can acess it with index . Negative Index from the reverse.
name = "Sakshi"
print(name[1] + name[-1])

# Declare "Henry" to variable called name.
# Replace "H" with P
name = "Henry"
print(name.replace("H", "P"))

# You can get a substring with slice operation.
# declare letters variable as 'abcdefghijklmnopqrstuvwxyz'
# Use slice operator to print letters from 12 to 15
# use slice opeartor from 20 to end.
# use slice oepartor to print letters from -3 to end.
# USe slice operator to get string from start to end in steps of 7 .
# USe slice operator from 4 to 20 in steps of 3.

letters = 'abcdefghijklmnopqrstuvwxyz'
print("Letters from 12 to 15 ", letters[12:15])
print("Letters from 20 to end", letters[20:])
print("Letters from -3 to end", letters[-3:])
# Not specifying any start end will default to start and with
print("letters froms tart to end in steps of 7 ", letters[::7] )
print("letters from 4 to 20 in steps of 3", letters[4:20:3])


# len function to print length of string.
# use len to print the length of string letters

letters = "abcedijfjkjkqzno"
print(f"Length of the letters is {len(letters)}")

# You can use split function to split on the string by the character.
# Declare a string called get gloves,get mask,give cat vitamins,call ambulance
# Use split operator to split using the , operator.
mystr = "gloves,get mask,give cat vitamins,call ambulance"
myarray = mystr.split(",")
print(myarray[3])



# Declae an array called "Yeti", "Bigfoot", "Loch Ness Monster"
# use : or , to joiin the array.

my_array = ["yeti", "Bigfoot", "Loch Ness monster"]
print(",".join(my_array))

# Replace the function.
# Declare a string called a duck goes into a bar....
# USe replace function to replace duck with marmoset.
mystr = "a duck goes into a bar..."
print(mystr.replace("bar", "marmoset"))



# USe strip to remove the spaces in strings. You can also specify character, set of characters for removal.
# Delcare a string called "  earth   "
# use strip to remove white spaces  .
# use lstrip to remove the wihite space from left side.
# use rstriop to remve the white space from right side.

earth_str ="  earth   "
print("-" + earth_str.strip() + "-")
print("-" + earth_str.lstrip() + "-")
print("-" + earth_str.rstrip() + "-")

# Strip function can take parametes.
# Declare a string called What the...!!?
# Remove ".?!" using the strip funciton.
mystr = "What the...!!?"
print(mystr.replace("!?", ""))


# Use string module to get all possible whitespace and punctuation characters.
import string
# Print all whitespaces.

# Print the punctuation.

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
# use rfind and rindex to find the word "the"
# use count  to find number of occurences of string "the"

print(poem.startswith("All"))
word  = "the"
print(poem.index(word))
print(poem.find(word))
print(poem.rfind(word))
print(poem.rindex(word))
print(f"Count of word {word} is {poem.count('the')}")

# Will print the position of the string.

# Find the position of the string from the right.

# Count the number of occurences.

# Converting to lower, upper and using title.
# Declare a string called setup a duck goes into the bar
# Print the title of the above string, uppercase string, use swapcase()
duckstr = "setup a duck goes into the bar"
print(f"Title is {duckstr.title()}")
print(f"Uppercased is {duckstr.upper()}")
print(f"Lowercased is {duckstr.lower()}")


# COnvert to upper.

# Change case from one to another.

# String formatting.
# Use old style formatting to
# print the string .
# Our cat <Name of Cat > weighs < weight > pounds
actor = 'Richard Gere'
cat  = 'Chester'
weight = 28

catstr = "Our cat %s weighs %d pounds" % (cat, weight)
print(catstr)

# Left and Right Formatting.

# Left and Right Formatting. woodstuck ( 8 characters ) . %12s will add 4 characters %12s will
# Add 4 characrters to the left.
# %-12s will add 4 characters to the right.
# declare a thing as woodstock use woodstock to left format and then right format.
# Use {} and format .

thing = "woodchuck"
place = "lake"
formatstr = "The {}  is in the {}".format(thing, place)
print(formatstr)


# It can be same with d ( for decimal ). Format 9876 to 12 left
# and 12 to right.



# New Formatters are with :10s and use {} braces.

# declare two variables as thing = wraith and place as window.
# use {} and format to do the following.
# 1. {} to format m {:10s} to format,
# 2. {} with >10s right alighent,
# 3. {} with :<10s to do the left alignment.
# 4. ^10s to do middle formatting.
# 5. use ! to format with the string with ! instead of spaces.
 # String should be  The wraith is at the window.

thing = "wraith"
place = "window"
mystr = "The {:10s} is at the {:10s}".format(thing, place)
print(mystr)
mystr = "The {:<10s} is at the {:>10s}".format(thing, place)
mystr = "The {:^10s} is at the {:^10s}".format(thing, place)
print(mystr)
mystr = "The {:!^10s} is at the {:!^10s}".format(thing, place)
print(mystr)


# Doing the same with f strings.
mystr = f"The {thing:>20} is in the {place:.^20}"
print(mystr)

# Left Alignment.
mystr = f"The {thing:<20} is in the {place:.^20}"
print(mystr)

# Center Alignment.
mystr = f"The {thing:!^20} is in the {place:.^20}"
print(mystr)


# Surround with ! on the string


# Newest Strings are f strings.
# declare a varable thing as wereduck
# declare a variable place as werepond
# use f string to print The wreduci in the wrerepond.


# Alignment in space. :> for right alignmetn, :< for left alignment.
# :^ is for center alignment. To surround with a character :.^

# lower, upper, swapcase, title()
# center(), ljust(), rjust()