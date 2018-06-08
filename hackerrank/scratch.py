import math
from scipy.special import comb

s = [0]
f = [0]

def compute_f(n):
  sub = 0
  for k in range(1, n):
    val = comb(n - 1, k - 1) * f[k] * math.pow(2, (n - k) * (n - k - 1) / 2)
    if k == n - 1:
      print("k == n -1 == %s => %s" % (k, val))
    sub += val
  s.append(sub)
  f.append(math.pow(2, n * (n - 1) / 2) - sub)

for i in range(1, 10):
  compute_f(i)

print(s)
print(f)
