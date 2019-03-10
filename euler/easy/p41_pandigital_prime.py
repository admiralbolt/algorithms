# Why the fuck are there so many pandigital questions?
import collections
import os
import sys

# This bit is ridiculous
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from utils import prime_utils

is_prime, primes = prime_utils.load_primes()

def is_pandigital(n):
  return set(str(n)) == set(map(str, range(1, len(str(n)) + 1))) and collections.Counter(str(n)).most_common()[0][1] == 1


for prime in primes:
  if is_pandigital(prime):
    print(prime)
