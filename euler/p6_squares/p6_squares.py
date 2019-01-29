# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import argparse
import os
import sys

# This bit is ridiculous
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from utils import math_utils

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Diff sum of squares and square of sums.")
  parser.add_argument("--num", default=100, type=int, help="Number to diff.")
  args = parser.parse_args()
  print(math_utils.gaussian_sum(args.num) ** 2 - math_utils.sum_of_squares(args.num))
