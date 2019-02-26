import os
import sys

# This bit is ridiculous
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from utils import prime_utils

def gen_truncate(i):
  s = str(i)
  for j in range(len(s)):
    yield int(s[j:])
    yield int(s[:j+1])

def check_truncations(is_prime, i):
  for truncation in gen_truncate(i):
    if not is_prime[truncation]:
      return False
  return True



is_prime, primes = prime_utils.load_primes()
truncatable_primes = []
for i in range(11, 1000000):
  if not check_truncations(is_prime, i):
    continue
  truncatable_primes.append(i)

print(truncatable_primes)
print(sum(truncatable_primes))
