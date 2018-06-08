# https://www.hackerrank.com/challenges/equal/problem

import os

def get_diff_ops(start, target):
  """
  Returns the number of operations it takes to get from start to target,
  where the valid operations are subtracting 1, 3, or 5.
  """
  diff = start - target
  sub_5 = diff // 5
  sub_3 = (diff % 5) // 2
  sub_1 = diff % 5 % 2
  return sub_5 + sub_3 + sub_1

def equal(chocolate_counts):
  """
  This algorithm works in the following way:
  Adding to every number is the same as subtracting from a single number until
  all are equal. All we need is to correctly identify the target value.
  It is not guaranteed that the target value is the minimum chocolate count,
  consider the example [2 6 6 6]
  If we use 2 as the target value it takes 6 operations to reduce the list:
  [2 6 6 6] -> [2 4 6 6] -> [2 2 6 6] -> [2 2 4 6] -> [2 2 2 6] -> [2 2 2 4] -> [2 2 2 2]
  However, if we use 1 as the target value it instead takes 4 operations:
  [2 6 6 6] -> [1 6 6 6] -> [1 1 6 6] -> [1 1 1 6] -> [1 1 1 1]
  We reduced the number of total operations because we can shift each of the 6's
  with 1 op instead of 2.

  The target value must be within some x of the minimum. X < 3 otherwise we
  are adding steps without the potential to reduce multiple steps into single
  steps.
  """
  min_count = min(chocolate_counts)
  return min(
    sum([get_diff_ops(count, min_count - diff) for count in chocolate_counts])
    for diff in range(3)
  )


if __name__ == "__main__":
  num_test_cases = int(input())
  results = []
  for _ in range(num_test_cases):
    _ = input()
    chocolate_counts = list(map(int, input().rstrip().split()))
    results.append(equal(chocolate_counts))
  if "OUTPUT_PATH" in os.environ:
    # Running on hackerrank.
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    for result in results:
      fptr.write(str(result) + "\n")
    fptr.close()
  else:
    # Running locally.
    for result in results:
      print(result)
