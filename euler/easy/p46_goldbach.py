import os
import sys

# This bit is ridiculous
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from utils import prime_utils

is_prime, primes = prime_utils.load_primes()

squares = []
for i in range(1, 100000):
  squares.append(i * i)

# It was proposed by Christian Goldbach that every odd composite number can be
# written as the sum of a prime and twice a square. We iterate through each
# odd composite number, and subtract squares from it. We check to see if the
# result is prime.
def can_be_written(i):
  for square in squares:
    if square > i:
      break
    diff = i - 2 * square
    if is_prime[diff]:
      # print("%s = %s + 2 * %s" % (i, diff, square))
      return True
  return False

for i in range(9, 10000, 2):
  if not is_prime[i] and not can_be_written(i):
    print("Cannot write %s." % (i))
    exit()
