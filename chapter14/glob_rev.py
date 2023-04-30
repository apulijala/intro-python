import glob
import os.path
# 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
# print(glob.glob('*'))
# print(glob.glob('??'))

"""
1. Get an absolute path oops.txt
"""
print(os.path.abspath("oops.txt"))

# 2. Get the real path.Using the symbolic path.
os.path.relpath("jeepers.txt")

win_file = os.path.join("eek", "urk")
print(win_file)

from pathlib import Path
# YOu can use operator / for joining paths.
# file_path = Path("eek") / "urk" / "snort.txt"
# Create a path is
file_path = Path("eek") / "urk" / "snort.txt"
print(file_path)
print(file_path.name)
print(file_path.suffix)
print(file_path.stem)

"""
1. You can pass file_path directly to open() function
"""