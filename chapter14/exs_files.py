"""
14.1 List the files in your current directory.

14.2 List the files in your parent directory.

14.3 Assign the string 'This is a test of the emergency text system' to the variable test1,
and write test1 to a file called test.txt.

14.4 Open the file test.txt and read its contents into the string test2. Are test1 and test2 the same?
"""

import os
print(os.listdir("."))
print(os.listdir(".."))

test1  = "This is a test of the emergency text system"
fin = open("test.txt", "wt")
fin.write(test1)
fin.close()

# Open the file test.txt and read contents to string test2.
fin = open("test.txt", "rt")
test2 = fin.readline()
print(test2)
fin.close()
print (test1 == test2)

