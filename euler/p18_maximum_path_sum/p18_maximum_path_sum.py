# Maximum path sum.

pyramid = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""


def parse_pyramid(pyramid):
  """Parse a pyramid string into a list of lists.

  We parse it in reverse order to make the DP easier.
  """
  matrix = []
  for line in pyramid.strip().split("\n")[::-1]:
    matrix.append(list(map(int, line.split())))
  return matrix

def maximum_path_sum(pyramid):
  """Find the maximum path using dynamic programming.

  We construct a matrix that keeps track of the maximal sum possible including
  the current point. We initialize our state to the bottom row of the pyramid:
  s[0] = matrix[0]
  Then, each subsequent entry can be calculated as:
  s[i][j] = max(s[i - 1][j], s[i - 1][j + 1]) + matrix[i][j]
  There's no need to save the entire matrix, so we save some memory by using
  a single list.
  """
  matrix = parse_pyramid(pyramid)
  max_path = []
  max_path.append(matrix[0])
  for i in range(1, len(matrix)):
    new_row = []
    for j in range(len(matrix[i])):
      new_row.append(max(max_path[i - 1][j], max_path[i - 1][j + 1]) + matrix[i][j])
    max_path.append(new_row)
  return max_path[-1][0]



print(maximum_path_sum(pyramid))
