# Import pick method from fast file (module)
from fast import pick
import sys

"""
for place in sys.path:
    print(place)
"""


place = pick()
print(f"Let's Go: {place}")

import fast
place = fast.pick()
print(f"Place is {place}")