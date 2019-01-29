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

def bisect(max_value):
  # Precompute fib_numbers
  fib_numbers = math_utils.fib(500)
  for i, val in enumerate(fib_numbers):
    if val > max_value:
      return i - 1
  return i

def sum_slow(max_value):
  # Precompute fib numbers
  fib_numbers = math_utils.fib(33)
  total_sum = 0
  for i in range(2, 33, 3):
    if fib_numbers[i] < max_value:
      total_sum += fib_numbers[i]
  return total_sum


def sum_discrete(max_iter):
  total_sum = 0
  for i in range(3, max_iter + 2, 3):
    total_sum += math_utils.fib_discrete(i)
  return total_sum





if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Sum some.")
  parser.add_argument("--max", default=4000000, type=int, help="maximum value")
  args = parser.parse_args()
  print("Bisect: %s." % bisect(args.max))
  print("Sum Slow: %s." % sum_slow(args.max))
  print("Sum Discrete: %s." % sum_discrete(32))
