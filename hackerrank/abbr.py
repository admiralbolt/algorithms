import functools
import os
import sys
# Hack to get it to work for large numbers.
sys.setrecursionlimit(10000)

@functools.lru_cache(maxsize=4096)
def abbr(a, b):
  """
  Return True if we can convert a -> b using only two operations:
  1. Capitalize any of a's lowercase letters.
  2. Delete all of the remaining lowercase letters in a.
  Example:
  Input: a=AbcDE, b=ABDE
  Output: True
  """
  if len(a) < len(b):
    return False
  elif len(b) == 0:
    return len(a) == 0 or all([c.islower() for c in a])
  if a[0] == b[0]:
    return abbr(a[1:], b[1:])
  elif a[0] == b[0].lower():
    return abbr(a[1:], b[1:]) or abbr(a[1:], b)
  elif a[0].islower():
    return abbr(a[1:], b)
  else:
    return False

def abbreviation(a, b):
  # Quick preprocess to remove all invalid chars in a.
  valid_a = "".join([
    letter for letter in a if letter.isupper() or letter.upper() in b
  ])
  return "YES" if abbr(valid_a, b) else "NO"


if __name__ == "__main__":
  try:
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    q = int(input())
    for q_itr in range(q):
      a = input()
      b = input()
      result = abbreviation(a, b)
      fptr.write(reuslt + "\n")
  except Exception as e:
    print(e)
