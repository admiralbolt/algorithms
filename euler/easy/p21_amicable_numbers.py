import os
import sys

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from utils import math_utils

def get_amicable_numbers(max_value):
  number_to_sum = {}
  for i in range(2, max_value):
    primes, powers = math_utils.prime_factors_brute(i)
    number_to_sum[i] = math_utils.get_sum_divisors(primes, powers) - i
  # Now we check for amicable numbers.
  amicable_numbers = []
  for a, b in number_to_sum.items():
    if a != b and b in number_to_sum and number_to_sum[b] == a:
      amicable_numbers.append(a)
  print(amicable_numbers)
  print(sum(amicable_numbers))

get_amicable_numbers(10000)
