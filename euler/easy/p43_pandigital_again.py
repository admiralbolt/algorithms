# Still on with this pandigital stuff huh?
import collections
import itertools

def is_pandigital(s):
  return set(s) == set("0123456789") and collections.Counter(s).most_common()[0][1] == 1

primes = [2, 3, 5, 7, 11, 13, 17]

def is_divisible(s):
  for i in range(7):
    if int(s[1 + i:4 + i]) % primes[i] != 0:
      return False
  return True

pandigitals = []
for perm in itertools.permutations("0123456789"):
  if not is_pandigital(perm):
    continue
  """
  d2d3d4=406 is divisible by 2
  d3d4d5=063 is divisible by 3
  d4d5d6=635 is divisible by 5
  d5d6d7=357 is divisible by 7
  d6d7d8=572 is divisible by 11
  d7d8d9=728 is divisible by 13
  d8d9d10=289 is divisible by 17
  """
  s = "".join(perm)
  if not is_divisible(s):
    continue
  pandigitals.append(int(s))


print(sum(pandigitals))
