# divmod returns quotient and reminder.
result = divmod(9,5)
print(f"result = {result}")

# chr functions the character whose value is value.
"""
for mynum in range(30,127):
    mychar = chr(mynum)
    myordinal = ord(mychar)
    print(f"character is {mychar} and ordinal is {myordinal}")
"""

# Convert a string to any base itneger and will return value to base 10
print(f"101 in base 3 is int('10',2)")
result = int('101',2)
print(f"base 2 result is {result}")

result = int('10',22)
print(f"base 2 result is {result}")
result = int('10',16)
print(f"Converting 10 to base 16 {result}")


result = int('100',16)
print(f"Converting 100 to base 16 {result}")

"""
Notes: 
1. range(start,end,step) generates range of numbers from start to end in increments of step. 
example: range(10,16,2) will print 10, 12, 14 ,16. 

2. int('10',16) will convert 10 to base 16. Result will be 16. int('10', 2) will convert 10 to base 2. 
Result will be 2.

3. chr method. Converts number to a character.

4.ord method. Converts character to a number.
"""