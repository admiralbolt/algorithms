import argparse
import math
import os
import sys

# This bit is ridiculous
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from utils import prime_utils

def get_consecutive_primes(is_prime, b, c):
  """Returns the number of consecutive primes generated for a quadratic:

  n^2 + bn + c
  """
  number_consecutive = 0
  # if n = c, n^2 + bn + c can't be prime.
  for n in range(c):
    if not is_prime[n * n + b * n + c]:
      break
    number_consecutive += 1
  return number_consecutive

def brute_force_quadratic_primes():
  _, primes_under_1k = prime_utils.load_primes(max_number=1000)
  is_prime, primes_under_10m = prime_utils.load_primes(max_number=10000000)
  max_consecutive = 0
  final_b = final_c = 0
  for b in range(-999, 1001, 2):
    for c in list(map(lambda p: -1 * p, primes_under_1k)) + primes_under_1k:
      consecutive = get_consecutive_primes(is_prime, b, c)
      if consecutive > max_consecutive:
        max_consecutive = consecutive
        final_b, final_c = b, c
  return max_consecutive, final_b, final_c

max_consecutive, final_b, final_c = brute_force_quadratic_primes()
print(max_consecutive, final_b, final_c)
print(final_b * final_c)
