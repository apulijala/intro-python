"""
6.1 Use a for loop to print the values of the list [3, 2, 1, 0].
"""
mynums = [3, 2, 1, 0]
for mynum in mynums:
    print(mynum)

"""
6.2 Assign the value 7 to the variable guess_me, and the value 1 to the variable number. 
Write a while loop that compares number with guess_me. Print 'too low' if number is less than guess me. 
If number equals guess_me, print 'found it!' and then exit the loop. 
If number is greater than guess_me, print 'oops' and then exit the loop. 
Increment number at the end of the loop.
"""
guess_me = 7
number = input("Enter Number ? ")

while True:
    number = int(number)
    if number < guess_me:
        print("Too Low")
    elif number == guess_me:
        print("Found it !")
        break
    else:
        print("Oops !!")
        break
    number = input("Enter Number ? ")
else:
    number = number + 1

print(f"Number is {number}")



"""
6.3 Assign the value 5 to the variable guess_me. Use a for loop to iterate a variable 
called number over range(10). If number is less than guess_me, print 'too low'. 
If it equals guess_me, print found it! and then break out of the for loop. 
If number is greater than guess_me, print 'oops' and then exit the loop.
"""

guess_me = 11
for number in range(10):
    if number < guess_me:
        print("Too Low")
    elif number > 10:
        print("Oops !!")
        break
    else:
        print("Found It!")
        break
else:
    number = number + 1


print(f"Number is {number}")