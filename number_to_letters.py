import string

def number_to_letters(n):
  """
  Given the infinite sequence:
  a -> 1
  b -> 2
  ...
  z -> 26
  aa -> 27
  ...
  zz -> 702
  aaa -> 703

  Given an input number n, return the corresponding letter code representing it.
  """
  return base26(n - 1)

letters = string.ascii_lowercase
def base26(n):
  if n < 0:
    return ""
  else:
    # n // 26 -> Means the number of 26's that can fit into n.
    # n % 26  -> Means the remained after we've fit all the 26's we can.
    return base26((n // 26) - 1) + letters[n % 26]
