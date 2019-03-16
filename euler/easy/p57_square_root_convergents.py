# Doing some maths, we come up with a recursive series for representing this:
# a_n / b_n = a_{n - 1} + 2b_{n - 1} / a_{n - 1} + b_{n - 1}
#   with a_1 / b_1 = 3 / 2

a = [3]
b = [2]

for _ in range(999):
  new_a = a[-1] + 2 * b[-1]
  new_b = a[-1] + b[-1]
  a.append(new_a)
  b.append(new_b)

s = 0
for i, j in zip(a, b):
  if len(str(i)) > len(str(j)):
    s += 1

print(s)
