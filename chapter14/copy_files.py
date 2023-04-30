import os
import shutil

"""
1. Copy using oops.txt to ohno.txt
"""
import shutil
shutil.copy("oops.txt", "ohno.txt")

"""
os.rename
2. Rename the files ohno.txt to ohwell.txt
"""
os.rename("ohno.txt", "ohwell.txt")

"""
Use os.link  - This will create a hard link. 
Link oops.txt to yikes.txt. 
Check if yikes.txt is a file.  
Check if yikes.txt is a link . 
"""
try :
    os.link("oops.txt", "yikes.txt")
except FileExistsError as fe:
    pass

print(f"oops.txt is a file ? {os.path.isfile('oops.txt')}")

"""
symlink is a symbolic link. 
Create a symlink from oops.txt to jeepers.txt
Check if jeepers.txt is a symbolic link. 
"""
try :
    os.symlink("oops.txt", "jeepers.txt")
except FileExistsError:
    pass
print( "Check if jeepers.txt is a link ", os.path.islink("jeepers.txt"))
