
def generate_champernowne(n):
  s = ""
  for i in range(1, n + 1):
    s += str(i)
  return s

lots_of_digits = generate_champernowne(2000000)
indices = [0, 9, 99, 999, 9999, 99999, 999999]
q = 1
for i in indices:
  q *= int(lots_of_digits[i])
print(q)
