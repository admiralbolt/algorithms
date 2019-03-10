pset = set()
plist = []

for i in range(1, 50000):
  p = (i * (3 * i - 1)) // 2
  pset.add(p)
  plist.append(p)

# for i in range(9999):
#   for j in range(i + 1, 10000):
#     if plist[j] - plist[i] in pset and plist[j] + plist[i] in pset:
#       print("i: %s, j: %s" % (i, j))

min_diff = 100000
ps = ()
for i in range(19999):
  pi = plist[i]
  for j in range(i + 1, 20000):
    pj = plist[j]
    # print("i: %s, p[i]: %s, j: %s, p[j]: %s. diff: %s, sum: %s" % (i, pi, j, pj, pj - pi, pj + pi))
    if (pj - pi) not in pset or (pj + pi) not in pset:
      continue
    if (j - i) < min_diff:
      min_diff = pj - pi
      ps = (pi, pj)

print(ps)
print(ps[1] - ps[0])
