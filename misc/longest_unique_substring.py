def longest_unique_substring(s, debug=False):
  """
  Computes the longest substring that only has unique characters, some examples:
  aabcdd -> abcd -> 4
  abcadef -> bcadef -> 6
  aa -> 1
  """
  if len(s) == 0:
    return 0
  elif len(s) == 1:
    return 1
  char_map = {}
  max_length = 0
  # Keep track of a left pointer and a right pointer. The right pointer is
  # always the index of the element we are currently considering.
  left = 0
  for i, l in enumerate(s):
    if l not in char_map:
      char_map[l] = i
    else:
      max_length = max(max_length, i - left)
      # Only update the left value if it's to the right of the current one.
      left = max(char_map[l] + 1, left)
      char_map[l] = i
    if debug:
      print("left: %s, i: %s, char_map: %s" % (left, i, char_map))
  # Recalculate the max one last time in case the last value wasn't a duplicate.
  max_length = max(max_length, i - left + 1)
  return max_length
