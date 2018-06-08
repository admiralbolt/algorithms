import math
import os

def cost(b):
  """
  We set up a 2 x n dp array. The values of dp[i][0] mean that we took the
  value of b[i]. The values of dp[i][1] mean that we took the minimum value
  aka 1.

  We then compare each value to the previous values of dp and take the max.
  """
  dp = [[0] * len(b), [0] * len(b)]
  # Since we consider pairs, skip the first value.
  for i in range(1, len(b)):
    dp[0][i] = max(
      math.fabs(b[i] - b[i - 1]) + dp[0][i - 1],
      b[i] - 1 + dp[1][i - 1]
    )
    dp[1][i] = max(
      b[i - 1] - 1 + dp[0][i - 1],
      dp[1][i - 1]
    )
  return int(max(dp[0][-1], dp[1][-1]))


if __name__ == "__main__":
  num_cases = int(input())
  results = []
  for _ in range(num_cases):
    _ = int(input())
    b = list(map(int, input().rstrip().split()))
    results.append(cost(b))
  if "OUTPUT_PATH" in os.environ:
    # Running on hackerrank.
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    for result in results:
      fptr.write(str(result) + "\n")
    fptr.close()
  else:
    for result in results:
      print(result)
