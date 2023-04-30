"""
1. Directory and Glob operations.
"""
import os

"""
1. Create a directory called poems. 
2. Check if the directory poems exists. 
3. Delete the directory with rmdir()
4. List the contents with listdir()

a. Create a directory called poems and check if poems exist. 
b. Remove the poems directory. 
c. List the poems directory
d. Make a directory called poems/mcintyre
e. list the directory poems. 
f. Create the poem below 
Cheerful and happy was his mood,
He to the poor was kind and good,
And he oft' times did find them food,
Also supplies of coal and wood,
He never spake a word was rude,
And cheer'd those did o'er sorrows brood,
He passed away not understood,
Because no poet in his lays
Had penned a sonnet in his praise,
'Tis sad, but such is world's ways.
"""
try:
    os.mkdir("poems")
except FileExistsError as fe:
    pass

# Create a directory called poems/mcintyre
try:
    os.mkdir("poems/mcintyre")
except FileExistsError as fe:
    print(os.listdir("poems"))

poem = """
Cheerful and happy was his mood,
He to the poor was kind and good,
And he oft' times did find them food,
Also supplies of coal and wood,
He never spake a word was rude,
And cheer'd those did o'er sorrows brood,
He passed away not understood,
Because no poet in his lays
Had penned a sonnet in his praise,
'Tis sad, but such is world's ways.
"""
fout = open("poems/mcintyre/poem.txt", "wt")
fout.write(poem)
print(os.listdir("poems"))

# Change the directory using os.
os.chdir("poems/mcintyre")
print(os.listdir("."))