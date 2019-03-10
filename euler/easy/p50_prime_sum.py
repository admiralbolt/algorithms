import os
import sys

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from utils import prime_utils

is_prime, primes = prime_utils.load_primes()

print(len(is_prime))

# We don't know where the consecutive primes start sadly, and I don't want
# to recompute everything, so we're gonna get clever.
# 1. Compute the sum of the primes from 2, 3, 5, ..., n.
# 2. Subtract the minimal prime from the sum then continue the process.

def get_max_prime(range_sum, max_prime, left, right):
  range_sum -= primes[left]
  temp_sum = range_sum
  for i in range(right + 1, 2000):
    temp_sum += primes[i]
    if temp_sum > 1000000:
      break
    if is_prime[temp_sum] and temp_sum > max_prime:
      max_prime = temp_sum
      range_sum = max_prime
      right = i
  return range_sum, max_prime, left + 1, right

left = 0
right = 0
max_prime = 0
s = 0
for i in range(10000):
  s += primes[i]
  if s > 1000000:
    break
  if is_prime[s] and s > max_prime:
    right = i
    max_prime = s

result = (max_prime, left, right)

range_sum = max_prime

while left < right:
  print(max_prime, left, right)
  range_sum, max_prime, left, right = get_max_prime(range_sum, max_prime, left, right)
  if right - left > result[2] - result[1]:
    result = (max_prime, left, right)

print(result)
print(sum([primes[i] for i in range(result[1], result[2] + 1)]))
