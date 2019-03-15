
def is_permuted_multiple(x, max_multiple=6):
  s = set(str(x))
  for i in range(2, max_multiple + 1):
    if s != set(str(x * i)):
      return False
  return True

for i in range(1, 1000000):
  if is_permuted_multiple(i):
    print(i)
