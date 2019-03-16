# This is another problem that I should probably come up with a clever way
# to solve, but I mean, I really can just plug in 99^99 and it'll fucking
# compute that shit so...

max_digit_sum = 0
for a in range(1, 100):
  for b in range(1, 100):
    n = a ** b
    digit_sum = sum([int(i) for i in str(n)])
    if digit_sum > max_digit_sum:
      max_digit_sum = digit_sum

print(max_digit_sum)
