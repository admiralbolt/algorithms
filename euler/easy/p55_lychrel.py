def is_palindrome(i):
  s = str(i)
  for i in range(len(s) // 2):
    if s[i] != s[-1 - i]:
      return False
  return True

def reverse(i):
  return int(str(i)[::-1])

def is_lychrel(i, max_iter=50):
  tmp = i
  for _ in range(max_iter):
    tmp += int(str(tmp)[::-1])
    if is_palindrome(tmp):
      return False
  return True

total_lychrel = 0
for i in range(1, 10000):
  if is_lychrel(i):
    total_lychrel += 1

print(total_lychrel)
