# divmod returns quotient and reminder.
# use divmod to find quotient and reminder for 9 and 5.
quotient, reminder = divmod(10,3)
print(f"Quotient = {quotient} and reminder is {reminder}")


# chr functions the character whose value is value.
# chr value for example chr(mynum)
# ord value is ord(mychar) will return a number.
# In the range of  30 to 127. print the character to mynum and
# reverse it print the ordinal.

for myint in range(30, 127):
    mychar = chr(myint)
    myoridnal = ord(mychar)
    print( f"Character : {mychar} and ordinal is {myoridnal}")

# Convert a string to any base itneger and will return value to base 10
# Convert 100 to base 2 and then to base 16.
myintegerstr = "String 100 converted to base 2 is %d", int("100", 2)
print(myintegerstr)

base16str = "String 100 converted to base 16 is %d", int("100", 16)
print(base16str)

# int function will convert a string to number.

# Convert String 10 to base 16
base10str = "String 10 converted to base 16 is %d ", int("10",16)
print(base10str)

# Use range method to  display the integers from 10 to 16 in steps of 3.
for numebr in range(10,22,3):
    print(f"Number is {numebr}")


"""
Notes: 
1. range(start,end,step) generates range of numbers from start to end in increments of step. 
example: range(10,16,2) will print 10, 12, 14 ,16. 

2. int('10',16) will convert 10 to base 16. Result will be 16. int('10', 2) will convert 10 to base 2. 
Result will be 2.

3. chr method. Converts number to a character.

4.ord method. Converts character to a number.
"""

