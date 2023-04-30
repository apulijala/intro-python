"""
1. Changing permissions on the file.
a. They must be specified as 0o400 Which is Octal notation for 0o
2. Changing ownership with chown
"""
import os
os.chmod("oops.txt", 0o400 )
os.chmod("oops.txt", 0o600 )


"""
1. Change ownership of the files with chown. 
2. Use uid of 5 and gid of 22 on oops.txt file. 
"""
uid = 1100
gid = 1100
try:
    os.chown("oops.txt", uid, gid)
except PermissionError:
    pass

# Delete the file with remove method.
"""
1. Delete the file hello.txt
"""
os.remove("hello.txt")