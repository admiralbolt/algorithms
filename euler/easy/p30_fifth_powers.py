

sums_of_powers = []

for a in range(2, 10000000):
  digits = map(int, str(a))
  if sum([digit ** 5 for digit in digits]) == a:
    sums_of_powers.append(a)

print(sum(sums_of_powers))
