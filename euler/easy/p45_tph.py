tset = set()
pset = set()
hset = set()
hlist = []

for i in range(100000):
  t = i * (i + 1) / 2
  p = i * (3 * i - 1) / 2
  h = i * (2 * i - 1)
  tset.add(t)
  pset.add(p)
  hset.add(h)
  hlist.append(h)

for i in range(144, len(hlist)):
  h = hlist[i]
  if h in tset and h in pset:
    print(h)
    break
