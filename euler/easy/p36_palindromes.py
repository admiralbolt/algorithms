

def is_palindrome(s):
  for i in range(len(s) // 2):
    if s[i] != s[-1 - i]:
      return False
  return True

double_palindrome = []
for i in range(1000000):
  if is_palindrome(str(i)) and is_palindrome(bin(i)[2:]):
    double_palindrome.append(i)

print(sum(double_palindrome))
