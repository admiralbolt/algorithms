"""
Given a list of integers A find all possible indices i < j < k such that
A[i] + A[j] + A[k] = 0

Example:
A = [-1, 0, 1, 2, -1, -4]

Result = [
  [0, 1, 2],
  [0, 3, 4],
  [1, 2, 4]
]
"""

import collections
import itertools

# Slow solution first: O(n^3)
def three_sum_slow(numbers):
  solutions = set()
  for i in range(0, len(numbers) - 2):
    for j in range(i + 1, len(numbers) - 1):
      for k in range(j + 1, len(numbers)):
        if numbers[i] + numbers[j] + numbers[k] == 0:
          solutions.add((i, j, k))
  return solutions


# Time to get clever. We map each value to its index, and then we apply a
# transform to this map:
# 1. Generate a key based on the inverted sum of two elements.
# 2. Generate a value containing all sets of valid indices to obtain this sum.
# With these two maps, we just check for intersection of keys, and then generate
# all possible final indicies.
def three_sum(numbers):
  index_map = collections.defaultdict(list)
  for i, number in enumerate(numbers):
    index_map[number].append(i)
  # Next, we make a map of pairwise sum values.
  pairwise_map = collections.defaultdict(list)
  # Python3 Ugh.
  unique_keys = list(index_map.keys())
  for i in range(0, len(unique_keys) - 1):
    for j in range(i + 1, len(unique_keys)):
      a, b = unique_keys[i], unique_keys[j]
      pairwise_map[-1 * a - b].extend(
        list(itertools.product(index_map[a], index_map[b]))
      )
  # Finally, check for intersection, and add the product to the final solutions.
  solutions = []
  for key in unique_keys:
    if key not in index_map or key not in pairwise_map:
      continue
    for index1 in index_map[key]:
      for index2, index3 in pairwise_map[key]:
        if index1 == index2 or index1 == index3 or index2 == index3:
          continue
        solutions.append(tuple(sorted([index1, index2, index3])))

  print(numbers)
  print(index_map)
  print(pairwise_map)
  return list(set(solutions))

print(three_sum([-1, 0, 1, 2, -1, -4]))
