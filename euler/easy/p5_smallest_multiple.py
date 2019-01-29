# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# This question is trying to be sneaky. We need to multiply only the necessary
# prime factors together. We prime factorize each number and then take the maximum
# power of each individual prime factor. Then, we multiply all the factors together.

import argparse
import collections
import math
import os
import sys

# This bit is ridiculous
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from p3_largest_prime_factor import p3_largest_prime_factor

final_factors = collections.defaultdict(int)
for i in range(2, 21):
  primes, powers = p3_largest_prime_factor.prime_factors_brute(i)
  print("Primes: %s, Powers: %s" % (primes, powers))
  for prime, power in zip(primes, powers):
    final_factors[prime] = max(power, final_factors[prime])

result = 1
for factor, power in final_factors.items():
  result *= factor ** power

print("Result: %s" % result)
