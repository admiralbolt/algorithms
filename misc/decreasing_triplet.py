def decreasing_triplet_chain(l):
  """
  Given an integer array A, is there a triple i,j,k s.t. i < j < k AND
  l[i] > l[j] > l[k]. Example:
  Input: [5, 6, 3, 8, 1]
  Output: True

  Input: [5, 6, 4, 9]
  Output: False
  """
  if len(l) < 3:
    return False
  # Chains will be a list of lists representing descending chains.
  chains = []
  for value in l:
    create_new_chain = True
    for chain in chains:
      if value > chain[-1]:
        if len(chain) >= 2 and value < chain[-2]:
          chain[-1] = value
          create_new_chain = False
      elif value < chain[-1]:
        chain.append(value)
        create_new_chain = False
    if create_new_chain:
      chains.append([value])
  for chain in chains:
    if len(chain) >= 3:
      return True
  return False

def decreasing_triplet(l):
  if len(l) < 3:
    return False
  has_smaller = [False] * len(l)
  has_greater = [False] * len(l)
  current_min = l[0]
  current_max = l[-1]
  for i in range(len(l) -2, -1, -1):
    if l[i] < current_min:
      current_min = l[i]
    else:
      has_smaller[i] = True
  for i in range(1, len(l)):
    if l[i] > current_max:
      current_max = l[i]
    else:
      has_greater[i] = True
  for i in range(0, len(l)):
    if has_smaller[i] and has_greater[i]:
      return True
  return False


print(decreasing_triplet([5, 8, 3, 6, 4]))
