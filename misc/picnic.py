# You are having a company picnic on the hottest day of the year. Thankfully,
# you will have umbrellas to provide you with shade. The tables and umbrellas
# are bolted to the ground (can't be stealing company property) so you can
# only choose to raise or lower umbrellas. Two umbrellas cannot both be raised
# if they overlap with each other at any point. What is the maximum amount
# of shade you can provide?
#
# The input will be an array of tuples (x, y, r) where (x, y) are the
# coordinates of the center of the table, and r is the radius of the umbrella.

import math

# Brute force solution.
# Time complexity is O(2^n * n^2)
def max_shade(umbrellas):
  total_shade = 0
  for mask in mask_gen(len(umbrellas)):
    if not is_valid_mask(umbrellas, mask):
      continue
    total_shade = max(total_shade, sum([
      umbrellas[i][2] * umbrellas[i][2]
      for i, umbrella_up in enumerate(mask) if umbrella_up
    ]))
  return total_shade


# Generates a mask for iterating through all possible combinations of umbrellas
# up/down. A 0/False corresponds to down, and a 1/True corresponds to up.
def mask_gen(size):
  format_str = "{:0%sb}" % size
  for i in range(0, int(math.pow(2, size))):
    bit_string = format_str.format(i)
    yield [char == '1' for char in bit_string]


# Returns whether or not the given configuration of umbrellas is valid.
def is_valid_mask(umbrellas, mask):
  raised_indices = [i for i, umbrella_up in enumerate(mask) if umbrella_up]
  for i in range(0, len(raised_indices) - 1):
    for j in range(i + 1, len(raised_indices)):
      if intersect(umbrellas[raised_indices[i]], umbrellas[raised_indices[j]]):
        return False
  return True


# Returns whether or not two individual umbrellas intersect
def intersect(umbrella1, umbrella2):
  x1, y1, r1 = umbrella1
  x2, y2, r2 = umbrella2
  dist = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) + (y2 - y1))
  return dist < (umbrella1[2] + umbrella2[2])
