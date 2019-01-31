import functools
import math

@functools.lru_cache(maxsize=1000000)
def perms(i, j):
  if i == 0 or j == 0:
    return 1
  if i > 0 and j > 0:
    return perms(i - 1, j) + perms(i, j - 1)

def binomial(i):
  # 2i choose i
  product = 1
  for k in range(1, i + 1):
    product *= (i + k) / k
  return round(product)



for i in range(2, 21):
  print(i, perms(i, i), binomial(i))
