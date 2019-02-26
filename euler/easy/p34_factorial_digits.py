import math

fac_digits = {str(i): math.factorial(i) for i in range(10)}

def fac_sum(n):
  return sum([fac_digits[i] for i in str(n)])

total_sum = 0
for i in range(10, 1000000):
  if fac_sum(i) != i:
    continue
  print("%s is equal to factorial sum of digits." % i)
  total_sum += i

print(total_sum)
