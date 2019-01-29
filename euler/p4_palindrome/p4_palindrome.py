# Find the largest palindrome that's a multiple of 2 3 digit numbers.

import argparse
import math
import os
import sys

# This bit is ridiculous
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

def is_palindrome(num):
  s = str(num)
  return s == s[::-1]

def find_max_palindromes(start=100, end=999):
  num1 = start
  num2 = start
  palindromes = []
  for num1 in range(start, end + 1):
    for num2 in range(start, end + 1):
      mult = num1 * num2
      if is_palindrome(mult):
        palindromes.append(mult)
  return max(palindromes)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Sum some.")
  parser.add_argument("--start", default=100, type=int, help="Starting number.")
  parser.add_argument("--end", default=999, type=int, help="Ending number.")
  args = parser.parse_args()
  print(find_max_palindromes(args.start, args.end))
