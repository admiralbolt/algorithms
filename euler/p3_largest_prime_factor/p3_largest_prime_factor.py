# Find the largest prime factor of some number.

import argparse
import math
import os
import sys

# This bit is ridiculous
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)


def prime_factors_brute(n, max_iter=1000000):
  primes = []
  powers = []
  remainder = n
  number = 2
  while remainder != 1:
    if number > max_iter:
      break
    if remainder % number == 0:
      primes.append(number)
      power = 1
      remainder = remainder / number
      # Keep trying the same number until it stops dividing.
      while remainder % number == 0:
        power += 1
        remainder = remainder / number
      powers.append(power)
    number += 1
  return primes, powers

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Sum some.")
  parser.add_argument("--num", default=600851475143, type=int, help="Number to factor.")
  parser.add_argument("--iter", default=1000000, type=int, help="Max iterations.")
  args = parser.parse_args()
  primes, powers = prime_factors_brute(args.num, args.iter)
  print("Primes: %s \nPowers: %s" % (primes, powers))
