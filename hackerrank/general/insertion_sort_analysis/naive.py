"""
https://www.hackerrank.com/challenges/insertion-sort/problem

Insertion Sort is a simple sorting technique which was covered in previous
challenges. Sometimes, arrays may be too large for us to wait around for
insertion sort to finish. Is there some other way we can calculate the number
of shifts an insertion sort performs when sorting an array?

The *fastest* way I can think of is just running insertion sort and counting
the number of swaps that we do...

By fastest I meant without having to think about it.
"""

import random

def partial_sort(l, i):
  swaps = 0
  while i > 0 and l[i] < l[i - 1]:
    l[i - 1], l[i] = l[i], l[i - 1]
    swaps += 1
    i -= 1
  return swaps

def analyze_insertion_sort_slow(l, debug=False):
  swaps = 0
  for i in range(1, len(l)):
    swaps += partial_sort(l, i)
    if debug:
      print(f"i: {i}, {l}, total_swaps: {swaps}")
  return l, swaps
