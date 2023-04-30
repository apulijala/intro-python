import random

# Extend the line here.
# You can spread it across multiple lines.
# Write sum as 1 + \ and then 2 , then 3 and then 10.
sum = 1 + \
      2 + \
      3 + \
      10

print(f"Sum of 1, 2, 3 and 10 is {sum}")


# write if statatemnt to do the following.
# If color is red, print "It's a tomato", if color is green
# It's a green pepper. If it is bee-purple, it will be Only bees can see the color.
# else I've never heard of the color.

input_color = input("Enter the Color ? ")
if input_color.lower() == "red":
    print("It's a tomato.")
elif input_color.lower() == "green":
    print("It's a Green Pepper.")
elif input_color.lower() == "bee-purple":
    print("You better ask bees. Strang purple color")
else:
    print("I've never heard of the color.")


# Empty list results in true / false. declare an empty list
# and check if is empty list.

empty_list = []
if not empty_list:
    print("is an empty list")

# In Operator. use in operator to check if a variable called letter is in word
# called "aeiou", Get letter from input function.
# if letter is in world, print letter is a vowel.
# else print letter is a consonent.
# For Murray.

vowels = "aeiou"
letter = input("Enter the letter: ")
if letter in vowels:
    print(f"{letter} is in vowels")
else:
    print(f"{letter} is not in vowels")


# Declare a set . Set declared with {}. use input function for a letter.
# if letter in vowel_set, print letter is in the vowel set.

vowel_set = { 'a', 'e', 'i', 'o', 'u'}
letter = input("Enter the letter: ")
if letter in vowel_set:
    print(f"{letter} is in vowel_set")
else:
    print(f"{letter} is not if vowel_set")


# Do the same for not in .

# Walrus Operator . Compare and assign. the oeprator.
# Instead of diff = tweet_limit - len(tweet_string)
# then if diff >= 0
# you can do.
# if diff  := tweet_limit - len(tweet_string) >= 0:

# Walrus operator is not working correctly. It always sets to 0 in above
# example.

tweet_limit = input("Enter Tweet limit: ")
tweet_string = input("Enter tweet string: ")
if diff := int(tweet_limit) - len(tweet_string) >= 0:
    print(f"{tweet_limit} is greater than {len(tweet_string)}")
else:
    print(f"{tweet_limit} is less than {len(tweet_string)}")



# Declare two variables called secret and guess .
# for secret assign use randint from random between 1 and 10
# for guess use randint from random between 1 and 10.
# use if /elif  / else guess is less than secret, guess is equal to secret.
# guess is greater tha secret.

# This is for Richard and Murrie and My House.

import random

secret = random.randint(1,100)
guess = random.randint(1,100)

if guess < secret:
    print(f"{guess} is less than {secret}")
elif guess > secret:
    print(f"{guess} is greater than {secret}")
else:
    print(f"{guess} is equal to {secret}")