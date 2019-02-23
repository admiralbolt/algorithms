import mpmath as mp

mp.dps = 100

def get_cycle_len(i):
  s = str(mp.fdiv(1, i, dps=100))
  print(s)
  for j in range(7, 12):
    if s[4:j+4] == s[j+4:j+j+4]:
      return j
  return 0


max_cycle = -1
n = -1

for i in range(3, 1001):
  cycle_len = get_cycle_len(i)
  if cycle_len > max_cycle:
    max_cycle = cycle_len
    n = i

print(n, max_cycle)
