import os
import sys

# This bit is ridiculous
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from utils import prime_utils

is_prime, primes = prime_utils.load_primes()

def generate_rotations(i):
  s = str(i) + str(i)
  l = len(str(i))
  return [int(s[i:i+l]) for i in range(l)]


circular_primes = []
for i in range(2, 1000000):
  if all([is_prime[n] for n in generate_rotations(i)]):
    circular_primes.append(i)
    print("%s is a circular prime." % i)

print(circular_primes)
print(len(circular_primes))
