# Moar brute force.
import itertools
import collections

def is_pandigital(a, b, c):
  all_str = "".join(a) + "".join(b) + str(c)
  return set(all_str) == set("123456789") and collections.Counter(all_str).most_common()[0][1] == 1

def multiply(a, b):
  return int("".join(a)) * int("".join(b))

digits = set("123456789")
pandigitals = set()

for r in range(1, 5):
  for a in itertools.permutations(digits, r):
    for z in range(1, 5):
      for b in itertools.permutations(digits - set(a), z):
        c = multiply(a, b)
        if not is_pandigital(a, b, c):
          continue
        pandigitals.add(c)



print(sum(pandigitals))
