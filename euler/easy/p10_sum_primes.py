# Get the sum of all primes less than 2 million.

import argparse
import math
import os
import sys
import pickle

# This bit is ridiculous
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from utils import math_utils

def sum_primes(max_value):
  primes = [2, 3, 5, 7, 11, 13, 17, 19]
  for i in range(23, max_value):
    if math_utils.is_prime_slow(i, primes):
      primes.append(i)
  with open("primes.pickle", "wb") as wh:
    pickle.dump(primes, wh)
  return sum(primes)

def sum_primes_sieve(max_value):
  primes = [False, False] + [True] * (max_value - 1)
  prime = 2
  while prime * prime < max_value:
    if primes[prime]:
      for i in range(prime * 2, max_value + 1, prime):
        primes[i] = False
    prime += 1
  total = 0
  for p in range(2, max_value + 1):
    if primes[p]:
      total += p
  return total


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Sum some primes.")
  parser.add_argument("--num", default=2000000, type=int, help="Max value of primes to sum.")
  args = parser.parse_args()
  print(sum_primes_sieve(args.num))
