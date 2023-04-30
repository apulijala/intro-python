# Write a while loop which prints count less than 10. Initialize count to 1.

counter = 1
while counter <= 10:
    print(f"Counter is {counter}")
    counter += 1

# Write a while loop which capitalizes string,based on input. if the user enters q, quit it.
# use while true statement. Otherwise, print the string.

quitstr = input("enter q to quit: ")
while True:
    if quitstr.lower() == "q":
        print("Quitting ")
        break
    else:
        print(quitstr)
    quitstr = input("enter q to quit:")


# In a while loop, enter Integer. if value is q, break out of the loop.
# Get a number, if it is even continue the lopp, otherwise print the squared number.
while True:
    number = input("Enter Number: ")
    if number.lower() == "q":
        break
    number = int(number)
    if number %2 == 0:
        continue
    else:
        print(f"Number squared is {number**2}")


# Else block can be used with while block. if while block does not exit
# with break block else block will be executed.
# Write a while loop as follows.
# Initialize the position to 0.
# Generate a list from 1 to 1000 within steps of 2. break when number is not even .
# Use else to print "No Even Number Found".

position = 0
numlist = list(range(1,1000,2))

while position < len(numlist):
    number = numlist[position]
    if number % 2 == 0:
        break
    position += 1
else:
    print("No Even number found.")


# For loop.
# print new line.
# declare a wrd as thud.
# iterate over a letter . and if letter is u break.
# else print not found u.
# Declare another word as "fierce"

word = input("Enter word ")
for letter in word:
    if letter.lower() == "u":
        print(f"Breaking {letter}" )
        break
else:
    print("Not Found u !!")


# for loop with else. Do the same with x.



# Converting range to list.
# Convert numbers from 1 to 5 and list.
print(list(range(1,5)))