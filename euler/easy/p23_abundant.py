import os
import sys

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from utils import math_utils

abundant_numbers = []

for i in range(1, 28124):
  primes, powers = math_utils.prime_factors_brute(i)
  if math_utils.get_sum_proper_divisors(primes, powers) > i:
    abundant_numbers.append(i)

print(abundant_numbers)

sums = set()
for i in range(len(abundant_numbers)):
  for j in range(i, len(abundant_numbers)):
    sums.add(abundant_numbers[i] + abundant_numbers[j])

total_sum = 0
for i in range(1, 28124):
  if i not in sums:
    total_sum += i
print(total_sum)
