def collatz_length(n):
  size = 1
  while n > 1:
    if n % 2 == 0:
      n = n / 2
    else:
      n = 3 * n + 1
    size += 1
  return size

memoize = {1: 1}
def collatz_recursive(n):
  if n in memoize:
    return memoize[n]
  if n == 1:
    return 1
  if n % 2 == 0:
    memoize[n] = 1 + collatz_recursive(n / 2)
  else:
    memoize[n] = 2 + collatz_recursive((3 * n + 1) / 2)
  return memoize[n]


starting = -1
max_length = -1
for i in range(1, 1000000):
  l = collatz_recursive(i)
  if l > max_length:
    max_length = l
    starting = i


print(starting, max_length)
