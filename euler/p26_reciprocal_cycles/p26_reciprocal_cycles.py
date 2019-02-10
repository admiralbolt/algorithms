import argparse
import decimal


def get_cycle_len(n, max_so_far = 7):
  # Longest repeating sequence for a number is n - 1 so we'll need a lot of
  # precision for large numbers.
  decimal.getcontext().prec = 2 * n
  # This is just a really complicated way of stripping the leading 0's
  s = str(decimal.Decimal(str(decimal.Decimal(1) / decimal.Decimal(n))[2:]))
  # This is *almost* like longest repeated substring, but we can make it
  # faster because we know the repeated part of the sequence is adjacent.
  # Additional, we *only* care if the repeated part is longer than what
  # we've found so far.
  cycle_len = max_so_far + 1
  for cycle_len in range(max_so_far + 1, n):
    for i in range(len(s) - cycle_len * 2):
      if s[i:i+cycle_len] == s[i+cycle_len:i+2*cycle_len]:
        # Double check that this can't be broken apart into a smaller sequence.
        for j in range(1, (cycle_len // 2) + 1):
          if s[i:i+j] == s[i+j:i+2*j]:
            return 0
        return cycle_len
  return 0



def get_max_cycle_brute(n):
  # Brute force that cycle baby.
  num = 0
  max_cycle = 1
  # Skip the boring numbers.
  for i in range(7, n):
    cycle_len = get_cycle_len(i, max_so_far=max_cycle)
    if cycle_len > max_cycle:
      max_cycle = cycle_len
      num = i
  return num, max_cycle

def get_max_cycle_fast(n):
  num = 0
  max_cycle = 1
  # Skip the boring numbers.
  for i in range(7, n):
    # If a number n is divisble by 2 or 5, it's repeating decimal portion has
    # an equivalent length of n / 2 OR n / 5. So, since we're going from bottom
    # to top, we've already calculated it, and we can skip it entirely.
    if i % 2 == 0 or i % 5 == 0:
      continue
    for j in range(1, i):
      if int("9" * j) % i == 0:
        if j > max_cycle:
          max_cycle = j
          num = i
        break
  return num, max_cycle


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Reciprocal cycles.")
  parser.add_argument("--num", default=1000, type=int, help="Number to calculate 1/d up to.")
  args = parser.parse_args()
  print(get_max_cycle_brute(args.num))
  print(get_max_cycle_fast(args.num))
