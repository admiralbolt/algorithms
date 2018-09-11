# Given a string, return the first non-repeating character in the string.
# Example: 'google' -> 'l'

import collections

# Basic way using character counts. Time complexity is 2n.
def non_repeating(string):
  if len(string) == 0:
    return None
  if len(string) == 1:
    return string[0]
  counts = collections.defaultdict(int)
  # Build our counts
  for char in string:
    counts[char] += 1
  # Re-run through our string
  for char in string:
    if counts[char] == 1:
      return char
  return None

# Slightly faster version that maps the first known location as well.
# Time complexity is n + m where m is the number of unique strings.
def non_repeating_loc(string):
  if len(string) == 0:
    return None
  if len(string) == 1:
    return string[0]
  counts = {}
  for i, char in enumerate(string):
    if char not in counts:
      counts[char] = {"count": 1, "loc": i}
    else:
      counts[char]["count"] += 1
  # Iterate over map stuff:
  final_char = None
  loc = len(string)
  for char, count_dict in counts.items():
    if count_dict["count"] == 1 and count_dict["loc"] < loc:
      loc = count_dict["loc"]
      final_char = char
  return final_char


print(non_repeating_loc("google"))
