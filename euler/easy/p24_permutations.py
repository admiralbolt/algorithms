digits = "0123456789"

def permutations(digits, depth = 0, perms = []):
  if depth == len(digits) - 1:
    starting_perms = []
    for digit in digits:
      starting_perms.append(digit)
    return starting_perms
  perms = []
  for perm in permutations(digits, depth + 1, perms):
    for digit in digits:
      if digit in perm:
        continue
      perms.append(perm + digit)
  return perms

print(sorted(permutations(digits))[1000000 - 1])
