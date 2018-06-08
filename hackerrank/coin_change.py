# https://www.hackerrank.com/challenges/coin-change/problem

def change_count(coins, value):
  """
  Counts the number of ways to make change for a target value based on the
  values in coins. Example:
  Input:
    coins = [2, 3, 4]
    target = 6
  Output: 3
  """
  # Initalize our counts, with the 0th row = 1.
  counts = [
    [1 if i == 0 else 0 for i in range(value + 1)] for _ in range(len(coins))
  ]
  for i in range(len(coins)):
    for j in range(1, value + 1):
      # Count the number of ways the previous set of coins could be used to
      # make the current target value j.
      prev_coin = counts[i - 1][j] if i - 1 >= 0 else 0
      # Count the number of ways the current coin set can be used.
      current_coin = counts[i][j - coins[i]] if j - coins[i] >= 0 else 0
      counts[i][j] = prev_coin + current_coin
  return counts[i][j]

if __name__ == "__main__":
  value = int(input().split()[0])
  coins = list(map(int, input().rstrip().split()))
  print(change_count(coins, value))
