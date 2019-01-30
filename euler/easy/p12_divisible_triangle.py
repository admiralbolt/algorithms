# What is the value of the first triangle number to have over five hundred divisors?
#
# We prime factorize each triangle number and the generate the total number
# of divisors from that. We can simply take all possible combinations of
# powers to get our answer.

import argparse
import os
import sys

# This bit is ridiculous
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from utils import math_utils

def find_triangle_with_divisors(minimum_divisors, max_iter=100000):
  for i in range(2, max_iter):
    triangle = math_utils.gaussian_sum(i)
    primes, powers = math_utils.prime_factors_brute(triangle)
    divisors = 1
    for power in powers:
      divisors *= (power + 1)
    print("Triangle: %s. Num divisors: %s." % (triangle, divisors))
    if divisors > minimum_divisors:
      return triangle
  return -1

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Find the divisors of a triangle number.")
  parser.add_argument("--min", default=500, type=int, help="Min value of number of divisors.")
  parser.add_argument("--iter", default=10000, type=int, help="Max number of iterations.")
  args = parser.parse_args()
  print(find_triangle_with_divisors(args.min, args.iter))
