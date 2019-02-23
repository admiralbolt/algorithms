def change_count(coins, value):
  """
  Counts the number of ways to make change for a target value based on the
  values in coins. Example:
  Input:
    coins = [2, 3, 4]
    target = 6
  Output: 3
  """
  # Initalize our counts, with the 0th row = 1 and the 0th column = 1.
  counts = [
    [1 if i == 0 or j == 0 else 0 for j in range(len(coins))] for i in range(value + 1)
  ]
  for j in range(len(coins)):
    for i in range(1, value + 1):
      # Count the number of ways the previous set of coins could be used to
      # make the current target value j.
      prev_coin = counts[i][j - 1] if j - 1 >= 0 else 0
      # Count the number of ways we can make the target value minus the value
      # of the currently considered coin.
      current_coin = counts[i - coins[j]][j] if i - coins[j] >= 0 else 0
      counts[i][j] = prev_coin + current_coin
  return counts
