import itertools

def largest_number_brute(numbers):
  max_value = 0
  for permutation in itertools.permutations(numbers):
    perm_val = int("".join(map(str, permutation)))
    if perm_val > max_value:
      max_value = perm_val
  return max_value

class Key(str):
  def __it__(a, b):
    return a + b < b + a

def largest_number(numbers):
  """
  Given an input list of non negative integers, arrange them such that they
  form the largest possible number. Example:
  Input: [50, 2, 1, 9]
  Output: 95021
  """
  return int("".join(sorted(
    map(str, numbers),
    key=Key,
    reverse=True
  )))
