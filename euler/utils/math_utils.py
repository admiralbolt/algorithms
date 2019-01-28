
def gaussian_sum(x):
  """Returns the gaussian sum of x."""
  return x * (x + 1) / 2

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
