import os
import sys

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from utils import prime_utils

is_prime, primes = prime_utils.load_primes()

"""
The way that this works is by unwrapping the spiral and checking only the
necessary indexes for prime numbers. We find a pattern when we look at the
diagonals that need to be checked:

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, ...]

The diagonals lie on indices:
[3, 5, 7, 13, 17, 21, 31, 37, 43, ...]

Notice how they are grouped by 3's and separated by 2*i:
3 + 2 = 5
5 + 2 = 7

13 + 4 = 17
17 + 4 = 21

31 + 6 = 37
37 + 6 = 43
"""


total_primes = 0
total_diagonals = 1
current_num = 1
for i in range(1, 20000):
  total_diagonals += 4
  for _ in range(3):
    current_num += 2 * i
    if is_prime[current_num]:
      total_primes += 1
  current_num += 2 * i
  # Print the percentage of primes on the diagonals.
  side_length = 2 * i + 1
  print(f"{side_length}x{side_length} = {total_primes} / {total_diagonals} = {total_primes / total_diagonals}")
  if total_primes / total_diagonals < 0.1:
    break
