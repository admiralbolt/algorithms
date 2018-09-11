# Given two strings, find the length of the longest common subsequence between
# the two strings. The sequence must be contiguous but not necessarily in order.
#
# Example: lcs("ABCDGH", "AEDFHR") is "ADH" of length 3.

# Recurisve solution. Works backwards through each string to find where
# values are equal.
# Run time is O(2^N) without memoization.
def lcs_recursive(string1, string2, s1_index, s2_index):
  if s1_index == 0 or s2_index == 0:
    return 0
  elif string1[s1_index] == string2[s2_index]:
    return 1 + lcs_recursive(s1_index - 1, s2_index - 2)
  else:
    return max(
      lcs_recursive(string1, string2, s1_index - 1, s2_index),
      lcs_recursive(string1, string2, s1_index, s2_index - 1)
    )

# The better, dynamic programming approach.
# Time complexity: O(mn), Space complexity: O(mn)
def lcs(string1, string2):
  m = len(string1)
  n = len(string2)
  # Initialize our m + 1 x n + 1 dp array. Just makes the init part waaaaaay
  # easier.
  # Interesting note, we can't do [[0] * n] * m, as the inner lists are created
  # as duplicates of each other.
  max_substring = []
  for i in range(m + 1):
    max_substring.append([0] * (n + 1))
  # Fill in the rest of the table:
  for i in range(0, m + 1):
    for j in range(0, n + 1):
      # Initialize our first row.
      if i == 0 or j == 0:
        max_substring[i][j] = 0
      # If the chars are equal add 1 to the diagonally previous value.
      elif string1[i - 1] == string2[j - 1]:
        max_substring[i][j] = 1 + max_substring[i - 1][j - 1]
      # Otherwise carry over the maximum of the previous col / row.
      else:
        max_substring[i][j] = max(max_substring[i - 1][j], max_substring[i][j - 1])
  return max_substring[m][n]
