import collections
import copy
import functools
import math
from scipy.special import comb

s = [0]
f = [0]

# https://www.hackerrank.com/challenges/counting-road-networks/problem
# https://oeis.org/A001187
def compute_f(n):
  sub = 0
  for k in range(1, n):
    val = comb(n - 1, k - 1) * f[k] * math.pow(2, (n - k) * (n - k - 1) / 2)
    if k == n - 1:
      print("k == n -1 == %s => %s" % (k, val))
    sub += val
  s.append(sub)
  f.append(math.pow(2, n * (n - 1) / 2) - sub)

def convert_to_list(n):
  return [int(char) for char in str(n)[::-1]]

def convert_to_int(n):
  return int(convert_to_str(n))

def convert_to_str(n):
  return "".join([str(i) for i in n])[::-1]

def shift(n, i):
  l = copy.deepcopy(n)
  l[i] -= 2
  if i == len(l) - 1:
    l.append(1)
  else:
    l[i + 1] += 1
    j = 1
    while l[i + j] >= 10:
      l[i + j] -= 2
      if i + j == len(l) - 1:
        l.append(1)
        break
      l[i + j + 1] += 1
      j += 1
  return l


x = 3

def convert_to_largest(n):
  if n < 10:
    return [n]
  curr = n
  l = []
  while curr >= 10:
    target = 8 if curr % 2 == 0 else 9
    l.append(target)
    curr = int((curr - target) / 2)
  l.append(curr)
  return l


# @functools.lru_cache(maxsize=2048)
def recurse_print(n, decimal, db_numbers = set()):
  global x
  n_repr = convert_to_str(n)
  if n_repr in db_numbers:
    return db_numbers
  db_numbers.add(n_repr)
  print(f"x: {x}, decibinary: {''.join(map(str, n))[::-1]}, decimal: {decimal}")
  # Iterate through our list backwards
  recurse = False
  for i, val in enumerate(n):
    if n[i] >= 2:
      x += 1
      db_numbers = recurse_print(shift(n, i), decimal, db_numbers=db_numbers)
  return db_numbers

# https://oeis.org/A007728

def decibinary(n):
  print("x: 1, decibinary: 0, decimal: 0")
  print("x: 2, decbinary: 1, decimal: 1")
  d = {}
  x = 3
  for i in range(2, n):
    d[i] = recurse_print(convert_to_largest(i), i, db_numbers=set())
  for i in range(2, n):
    print(f"{i} -> {d[i]}")
  print("reps...")
  reps = 0
  val = 0
  for i in range(2, n):
    if len(d[i]) != val:
      print(f"val: {val}, reps: {reps}")
      val = len(d[i])
      reps = 1
    else:
      reps += 1



decibinary(40)
