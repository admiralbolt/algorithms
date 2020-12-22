"""
We can sort it in a different way and count inversions.

Wow.

[2, 3, 2, 8, 7, 4, 5, 3]

We do merge sort and look at all the spots where we move a right hand side
item while there are still left hand side items. And that counts as a swap.

This guarantees O(nlog(n)) processing time.
"""
def merge_sort(l):
  if len(l) <= 1:
    return l, 0
  n = len(l) // 2
  left, right = l[:n], l[n:]
  # sort each side
  sleft, left_count = merge_sort(left)
  sright, right_count = merge_sort(right)
  # combine
  sorted, final_merge_count = combine(sleft, sright)
  return sorted, final_merge_count + left_count + right_count

def combine(l, r):
  left_index = 0
  right_index = 0
  swap_count = 0
  sorted = []
  length_left = len(l)
  length_right = len(r)
  for i in range(length_left + length_right):
    if left_index == length_left or (right_index < length_right and r[right_index] < l[left_index]):
      sorted.append(r[right_index])
      right_index += 1
      # Increment swap count based on numbers in left hand array.
      swap_count += length_left - left_index
    else:
      sorted.append(l[left_index])
      left_index += 1
  return sorted, swap_count
