import collections

def is_pandigital(s):
  return set(s) == set("123456789") and collections.Counter(s).most_common()[0][1] == 1

def pandigitalize(num, max_mult):
  s = ""
  for i in range(1, max_mult + 1):
    s += str(num * i)
  return s


pandigitals = []

for i in range(2, 5):
  for n in range(11, 10 ** (7 - i)):
    s = pandigitalize(n, i)
    if is_pandigital(s):
      print("i: %s, n: %s, s: %s" % (i, n, s))
      pandigitals.append(int(s))

print(sorted(pandigitals, reverse=True))
