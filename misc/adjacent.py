# Rearrange an array of characters such that no two identical characters are
# adjacent.

# First I want to establish if an input is valid or not, which I think we can
# do with a count of characters. Then we'll reconstruct an array arbitrarily
# that has no duplicate characters adjacent.

# A:3, B:2
# A:3, B:1
# A:3, B:3, C:3 ABCABCABC
# A:5, B:3, C:3 ABACABACABC
# A:7, B:3, C:3 ABACABACABACA
# A:8, B:3, C:3
# A:9, B:7, C:1

# 1. Sort hist by order desc.
# 2. If the largest is greater than the sum of the rest by 2, not a valid input.
# A > Sum(All) - A + 1

import collections

def seperate_identical_chars(s):
  char_map = collections.Counter(s)
  print(f"char_map: {char_map}")
  print(f"can_seperate: {can_separate(char_map)}")
  if not can_separate(char_map):
    return []
  return []

def can_separate(char_map):
  # Can't directly access values... dammit python 3.
  max_val = None
  sum_other = 0
  for val in char_map.values():
    if not max_val:
      max_val = val
    else:
      sum_other += val
  print(f"max_val: {max_val}, sum_other: {sum_other}")
  return max_val - 1 <= sum_other

seperate_identical_chars("ABCABACAAABAAA")
