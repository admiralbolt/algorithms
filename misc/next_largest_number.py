def next_largest_number(l):
  """
  Returns an array containing the distance to the next largest number ex:
  Input: [3, 11, 8, 4, 13, 6]
  Output: [1, 3, 2, 1, -1, -1]
  """
  if not l:
    return []
  if len(l) == 1:
    return [-1]
  next_largest = [-1] * len(l)
  # Iterate through the list backwards, starting with the second to last element.
  for i in range(len(l) - 2, -1, -1):
    current_element = l[i]
    next_element = l[i + 1]
    if current_element < next_element:
      next_largest[i] = 1
    elif current_element == next_element:
      next_largest[i] = -1 if next_largest[i + 1] == -1 else next_largest[i + 1] + 1
    else:
      # We know there is no greater element if we are larger than an element
      # that has no greater element.
      if next_largest[i + 1] == -1:
        next_largest[i] = - 1
        continue
      total_distance = 1 + next_largest[i + 1]
      # Jump through next larger elements until we find one that is larger
      # or run through the list of elements.
      while i + total_distance < len(l):
        if current_element < l[i + total_distance]:
          next_largest[i] = total_distance
          break
        elif current_element == l[i + total_distance]:
          next_largest[i] = -1 if next_largest[i + total_distance] == -1 else next_largest[i + total_distance] + total_distance
          break
        elif next_largest[i + total_distance] == -1:
            next_largest[i] = -1
            break
        total_distance += next_largest[i + total_distance]
  return next_largest
