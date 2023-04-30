"""
1. Check for file existence os.path.exists
2. Check for if a path is a file os.path.isfile
3. Check for if a path is a directory os.path.isdir
4. Check for if it is a absolute path. os.path.isabs
Password :
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
"""

"""
1. Check for existance of oops.txt. 
2. Check for existance of ./oops.txt
3. Check for existance of waffles
4. Check for existance of current directory. 
5. Check for existance of parent directory. 
"""

import os
print(f"Check for oops.txt {os.path.exists('oops.txt')}")
print(f"Check of ./oops.txt {os.path.exists('./oops.txt')}")
print(f"Check for existance of waffles {os.path.exists('waffles')}")
print(f"Check for current directory {os.path.exists('.')}")
print(f"Check for the parent directory {os.path.exists('..')}")


"""
1. Check if oops.txt is a file. 
2. check if directory ( hello ) in current directory exists. 
3. 
"""

import os
print (f"Check if oops.txt is a file : {os.path.isfile('oops.txt')}")
print(f"Check if hello is a directory: {os.path.isfile('hello')}")

"""
1. Check for absolute path. (name = oops.txt ) 
2. Check if /big/fake/name is an absolute path. 
3. Check if big/fake/name/without/a/leading/path is an absolute path. 
"""

name = "oops.txt"
"""
1. Check if it is absolute path. 
"""
print(f"Check if name exists : {os.path.isabs(name)}")
abspath = "/big/fake/name"
print(f"Check for abs path : {os.path.isabs(abspath)}")

relpath = "big/fake/name/without/a/leading/path"
print(f"Is {relpath} absolute : {os.path.exists(relpath)}")






