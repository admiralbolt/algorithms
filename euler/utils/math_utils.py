import math
from mpmath import mp

mp.dps = 500
# Golden ratio stuff.
phi = (1 + mp.sqrt(5)) / 2
phi_prime = (1 - mp.sqrt(5)) / 2

def gaussian_sum(x):
  """Returns the gaussian sum of x."""
  return x * (x + 1) / 2

def sum_of_squares(x):
  """Returns the sum of squares up to x inclusive."""
  return round((1 / 3) * mp.power(x, 3) + (1 / 2) * mp.power(x, 2) + (1 / 6) * x)

def fib(x):
  """Returns the list of fibonnaci numbers with x iterations."""
  if x == 0:
    return []
  if x == 1:
    return [1]
  if x == 2:
    return [1, 1]
  fib_numbers = [1, 1]
  for i in range(2, x):
    fib_numbers.append(fib_numbers[i - 2] + fib_numbers[i - 1])
  return fib_numbers

def fib_discrete(n):
  return round((mp.power(phi, n) - mp.power(phi_prime, n)) / mp.sqrt(5))
