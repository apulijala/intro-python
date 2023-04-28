
# Write a while loop which prints count less than 10. Initialize count to 1.
count =1
while count <= 10:
    print(f"count is {count}")
    count = count + 1

# Write a while loop which capitalizes string,based on input. if the user enters q, quit it.
while True:
    stuff = input("Enter the word to be capitalized: ")
    if stuff == "q":
        break
    print(f"Input capitalized : {stuff.capitalize():^20s} world")

# In a while loop, enter Integer. if value is q, break out of the loop.
# Get a number, if it is even continue the lopp, otherwise print the squared number.

while True:
    value = input("Integer, please [q to quit] : ")
    if value == "q":
        break
    number = int(value)
    if number % 2 == 0:
        continue
    print(f"Number squared is {number**2}")

# Else block can be used with while block. if while block does not exit
# with break block else block will be executed.

position = 0
numbers = list(range(1,1000,2))
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        break
    position = position +1
else:
    print("No Even Number Found")


word = "thud"
offset = 0
while offset < len(word):
    print(word[offset])
    offset = offset +1

# For loop.
print("\n")
word = "thud"
for letter in word:
    if letter == "u":
        break
    print(letter)
else:
    print("Not found u")

# Fro loop with else.
word = "thud"
for letter in word:
    if letter == "x":
        print("Eek | An x ! ")
        break
else:
        print("No 'x' is there.")

# Converting range to list.
print(list(range(1,5)))