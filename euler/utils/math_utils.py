import decimal
import math

# Golden ratio stuff.
# phi = (1 + mp.sqrt(5)) / 2
# phi_prime = (1 - mp.sqrt(5)) / 2

def gaussian_sum(x):
  """Returns the gaussian sum of x."""
  return x * (x + 1) / 2

# def sum_of_squares(x):
#   """Returns the sum of squares up to x inclusive."""
#   return round((1 / 3) * mp.power(x, 3) + (1 / 2) * mp.power(x, 2) + (1 / 6) * x)

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

# def fib_discrete(n):
#   return round((mp.power(phi, n) - mp.power(phi_prime, n)) / mp.sqrt(5))

def is_prime_slow(n, primes):
  for prime in primes:
    if prime > math.floor(math.sqrt(n) + 1):
      break
    if n % prime == 0:
      return False
  return True

def prime_factors_brute(n, max_iter=1000000):
  primes = []
  powers = []
  remainder = n
  number = 2
  while remainder != 1:
    if number > max_iter:
      break
    if remainder % number == 0:
      primes.append(number)
      power = 1
      remainder = remainder / number
      # Keep trying the same number until it stops dividing.
      while remainder % number == 0:
        power += 1
        remainder = remainder / number
      powers.append(power)
    number += 1
  return primes, powers

def eval_prime_factorized(primes, powers):
  result = 1
  for prime, power in zip(primes, powers):
    result *= prime ** power
  return result

def get_sum_divisors(primes, powers):
  individual_sums = []
  for prime, power in zip(primes, powers):
    isum = 1
    for i in range(1, power + 1):
      isum += prime ** i
    individual_sums.append(isum)
  # Finally, multiply together all the results.
  result = 1
  for isum in individual_sums:
    result *= isum
  return result

def get_sum_proper_divisors(primes, powers):
  return get_sum_divisors(primes, powers) - eval_prime_factorized(primes, powers)

def concat(a, b):
  return int(str(a) + str(b))
