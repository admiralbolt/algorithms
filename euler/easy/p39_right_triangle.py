import collections

triples = []
with open("pythagorean_triples.txt", "r") as rh:
  for line in rh.readlines():
    if not line:
      continue
    triple_numbers = line.split()
    if not triple_numbers:
      continue
    triples.append(tuple(map(int, triple_numbers[:3])))

triangles = collections.Counter()

for triple in triples:
  if sum(triple) > 1000:
    continue
  triangles[sum(triple)] += 1

print(triangles.most_common())
