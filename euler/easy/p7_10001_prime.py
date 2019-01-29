# Find the sum of all even fibonnaci numbers <= 4,000,000

import argparse
import math
import os
import sys

# This bit is ridiculous
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from utils import math_utils

def find_nth_prime(n):
  primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
  curr_prime = primes[-1]
  if n <= 10:
    return primes[n - 1]
  while len(primes) < n:
    curr_prime += 2
    if math_utils.is_prime_slow(curr_prime, primes):
      primes.append(curr_prime)
  return curr_prime

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Diff sum of squares and square of sums.")
  parser.add_argument("--num", default=10001, type=int, help="Number to diff.")
  args = parser.parse_args()
  print(find_nth_prime(args.num))
