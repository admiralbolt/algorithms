import bisect
import os
import sys

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from utils import math_utils

fib_numbers = math_utils.fib(100000)

print(bisect.bisect_right(fib_numbers, 10 ** 999))
