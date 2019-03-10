# I think the point of this problem is to come up with a clever way of only
# calculating what you need. BUT, python's only limitation is your computers
# memory for integers, so I'm just gonna fucking calculate it.

s = 0
for i in range(1, 1001):
  s += i ** i

print(s)
