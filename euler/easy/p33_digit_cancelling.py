import math

for a in range(10, 99):
  for b in range(11, 99):
    if a >= b:
      continue
    val = a / b
    sa, sb = str(a), str(b)
    for i in "123456789":
      if i in sa and i in sb:
        newa, newb = int(sa.replace(i, "", 1)), int(sb.replace(i, "", 1))
        if newb == 0:
          continue
        removed = newa / newb
        if math.isclose(val, removed):
          print("a: %s, b: %s" % (a, b))
