# Consider placing a knight on a phone dialer. Write a function that counts
# the distinct phone numbers dialable by the knight starting with the digit
# 0 and having length l.

import functools

key_map = {
  0: [4, 6],
  1: [6, 8],
  2: [7, 9],
  3: [4, 8],
  4: [0, 3, 9],
  5: [],
  6: [0, 1, 7],
  7: [2, 6],
  8: [1, 3],
  9: [2, 4]
}

# An iterative solution that expands each previous phone number.
# Time complexity ~ O(2.5^N), space complexity is also ~ O(2.5^N)
def get_unique_phone_numbers(length, digit = 0):
  if length == 0:
    return 0
  if length == 1:
    return 1
  rows = [[0]]
  for i in range(1, length):
    new_row = []
    for digit in rows[i - 1]:
      for child in key_map[digit]:
        new_row.append(child)
    rows.append(new_row)
  return len(rows[-1])

# A recursive solution that does the same as the above. Memoized for speed
# gains. Memoization makes it much faster than the iterative approach.
# Time complexity ~ O(N) *I think*, Space complexity depends on stack / cache.
@functools.lru_cache(maxsize=8192)
def get_numbers_recursive(length, digit = 0):
  if length == 0:
    return 0
  if length == 1:
    return 1
  return sum([get_numbers_recursive(length -1, digit = d) for d in key_map[digit]])



# Here's a crazy complicated way of solving the same problem except only using
# a few recurisve series. (Definitely not viable in an interview).

# see: http://oeis.org/A001519
a1 = [1, 1]
def series_a1(n):
  if n >= len(a1):
    for i in range(len(a1), n + 1):
      a1.append(3 * a1[i - 1] - a1[i - 2])
  return a1[n]

# see: http://oeis.org/A154626
a2 = [1, 2]
def series_a2(n):
  if n>= len(a2):
    for i in range(len(a2), n + 1):
      a2.append(2**i * series_a1(i))
  return a2[n]

# Equivalent to (1 + (-1)^n) / 2
def even_odd(n):
  if n % 2 == 0:
    return 1
  return 0

# Solves the chess knight problem using only math and a recursive series.
# Time complexity is O(n). Space complexity is O(n)
a3 = [1]
def get_numbers_maths(n):
  if n>= len(a3):
    for i in range(len(a3), n):
      a3.append(2 * a3[i - 1] + even_odd(i) * series_a2(int(i / 2)))
  return a3[n - 1]

print(f"Iterative: {get_unique_phone_numbers(10)}")
print(f"Recursive: {get_numbers_recursive(10)}")
print(f"Maths: {get_numbers_maths(10)}")
