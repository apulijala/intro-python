import random

sum = 1 + \
      2 + \
      3 + \
     10
print(f"Sum of numbers is {sum}")

color = "mauve"
if color == "red":
    print("It's a Tomato")
elif color == "green":
    print("It's a green pepper")
elif color == "bee pruple":
    print("Only bees can see the color.")
else:
    print("I've never heard of the color.")

# Empty list results in true / false.
some_list = []
if some_list:
    print("There's something in here.")
else:
    print("Hey It's empty!!")

# In Operator is best.
vowels = "aeiou"
letter = 'l'
if letter in vowels:
    print(f"{letter}", " is a Vowel.")
else:
    print(f"{letter} is a consonent")

# Declare a set
vowel_set = {'a', 'e','i', 'o','u' }
letter = "a"
if letter in vowel_set:
    print(f"{letter} is in {vowel_set}")

vowel_list = ['a', 'e','i', 'o','u']
letter = 'l'
if letter not in vowel_list:
    print(f"{letter} is not a vowel.")

# Walrus Operator . Comare and assing. the oeprator.
# Instead of diff = tweet_limit - len(tweet_string)
# then if diff >= 0
# you can do.
# if diff  := tweet_limit - len(tweet_string) >= 0:

tweet_limit = 250
tweet_string= "Blah" *400
diff = tweet_limit - len(tweet_string)
print("Actual diff is ", diff)
print("Absolute diff is ", abs(diff))
# Walrus operator is not working correctly. It always sets to 0 in above
# example.

if diff :=  tweet_limit - len(tweet_string) >= 0:
    print("A Flitting Tweet")
else:
    print(" Diff is ", diff)
    print("Went Over by ", abs(diff))


# Exercises.
secret = random.randint(1,10)
guess = random.randint(1,10)

if guess < secret:
    print(f"guess {guess} is less than secret {guess}")
elif guess < secret:
    print(f"guess {guess} is equal to secret {secret}")
else :
    print(f"guess {guess} is equal to secret {secret}")
