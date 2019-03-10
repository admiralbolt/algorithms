import collections
import os
import sys

from pprint import pprint

# This bit is ridiculous
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from utils import prime_utils

is_prime, primes = prime_utils.load_primes()

four_digit_primes = collections.defaultdict(list)
for i in range(1000, 10000):
  if is_prime[i]:
    four_digit_primes[frozenset(str(i))].append(i)


for key, primes in four_digit_primes.items():
  if len(primes) >= 3:
    for i in range(len(primes) - 2):
      for j in range(i + 1, len(primes) - 1):
        for k in range(j + 1, len(primes)):
          if primes[k] - primes[j] == primes[j] - primes[i]:
            print(primes[i], primes[j], primes[k])
