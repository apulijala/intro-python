"""
With open you and do to the files.

1.Read an existing file.
2. Write to an existing file.
3. Append to an existing file.
4. Overwrite  an existing file.
"""

"""
Following are true for files. 
r = reading 
w = writing. 
x = write, by only if file does not exist. 
a = append 

Other modes. 
t = text mode. 
b = binary mode. 
"""

# You can use open to open a file.
# Open a file called oops.txt as writing and in text mode.
# Write Oops, I created a file to this file.
# Close the file descriptir.
# print can take a file fo;e

fin = open("oops.txt", "wt")
print(" Oops, I created a file.", file=fin)
fin.close()


# Declare a poem as follows.
peom = """There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.
"""

# You can use write to a file.
# open a file called relativity.txt in write and text mode.
# Write the poem . Close the file.
fin = open("relativity.txt", "wt")
fin.write(peom)
fin.close()

# For using print,  you can use separator and end . For each line.
# Open  the previous file for
# What does separator do. end will put the required characters at the end of the string.

fout = open("relativity.txt" , "wt")
print(peom, file=fout, sep=" *** ", end= " *** ")
fout.close()

"""
1. You can use the chunk to read 
2. Read the file relativity.txt  to read in text mode. 
3. While it is True, read the file and add it to poem. 
4. Print the poem. 
"""

print("Poem is ")
poem = ''
fin = open("relativity.txt", "rt")
chunk = 100

while True:
    fragment = fin.read(chunk)
    if not fragment:
        break
    poem += fragment

print(poem)

# Do the readline on the File Object and print the line.

print("Read lines using readline() method \n")
poem = ''
fopen = open("relativity.txt", "rt")
while True:
    line = fopen.readline()
    if not line:
        break
    poem += line

fopen.close()
print(f"Length of the poem is {len(poem)}" )


"""
1. Use for in to loop over fileobj
2. Use the for in to loop over the fileobj and print the line. 
"""
poem = ''
fin = open("relativity.txt", "rt")
for line in fin:
    poem += line
print("Poem using for in loop\n")
print(poem)


"""
1. Using readlines() will read all the lines. 
2. readlines() will put them in an arry
"""
poem = ''
fin = open("relativity.txt", "rt")
allines = fin.readlines()
print("Poem all lines\n")
print(allines)

