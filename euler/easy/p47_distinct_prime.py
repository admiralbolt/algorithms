import os
import sys

# This bit is ridiculous
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from utils import math_utils

four_distinct = []

for i in range(210, 150000):
  primes, powers = math_utils.prime_factors_brute(i)
  if len(powers) == 4:
    four_distinct.append(i)

for i in range(len(four_distinct) - 3):
  if four_distinct[i + 3] - four_distinct[i] == 3:
    print("i: %s. (%s, %s, %s)" % (i, four_distinct[i], four_distinct[i + 1], four_distinct[i + 2]))
