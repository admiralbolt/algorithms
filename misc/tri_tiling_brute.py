# How many ways can you tile a 3xn grid with 2x1 dominoes.
import argparse
from pprint import pprint

def print_matrix(matrix):
  for l in matrix:
    print(l)


def find_first_open(matrix):
  for i in range(len(matrix)):
    for j in range(3):
      if not matrix[i][j]:
        return i, j
  return None, None

def all_true(matrix):
  return all([all(l) for l in matrix])

def can_place_vertical(matrix, i, j):
  return i != len(matrix) - 1 and not matrix[i][j] and not matrix[i + 1][j]

def can_place_horizontal(matrix, i, j):
  return j != 2 and not matrix[i][j] and not matrix[i][j + 1]

def place_vertical(matrix, i, j):
  matrix[i][j] = True
  matrix[i + 1][j] = True

def pop_vertical(matrix, i, j):
  matrix[i][j] = False
  matrix[i + 1][j] = False

def place_horizontal(matrix, i, j):
  matrix[i][j] = True
  matrix[i][j + 1] = True

def pop_horizontal(matrix, i, j):
  matrix[i][j] = False
  matrix[i][j + 1] = False

total_count = 0

# Brute force solution to spot check.
def brute(matrix):
  print_matrix(matrix)
  i, j = find_first_open(matrix)
  print(i, j)
  if i is None and j is None and all_true(matrix):
    global total_count
    total_count += 1
    print("found a state: %s" % total_count)
    return
  # Attempt to place a vertical tile:
  if can_place_vertical(matrix, i, j):
    print("placing vertical at: (%s, %s)" % (i, j))
    place_vertical(matrix, i, j)
    brute(matrix)
    print("popping vertical at: (%s, %s)" % (i, j))
    pop_vertical(matrix, i, j)
  # Attempt to place a horizontal tile:
  if can_place_horizontal(matrix, i, j):
    print("placing horizontal at: (%s, %s)" % (i, j))
    place_horizontal(matrix, i, j)
    brute(matrix)
    print("popping horizontal at: (%s, %s)" % (i, j))
    pop_horizontal(matrix, i, j)
  return


# Tiling going downards
"""
0 0 0
0 0 0
0 0 0
0 0 0
"""
def tri_tiling(n):
  global total_count
  matrix = []
  for i in range(n):
    matrix.append([False, False, False])
  brute(matrix)
  return total_count

def tri_tiling_fast(n):
  if n % 2 == 1:
    return 0
  f = [1, 0, 3, 0]
  for i in range(4, n + 1):
    if i % 2 == 1:
      f.append(0)
      continue
    f.append(4 * f[i - 2] - f[i - 4])
  print(f)
  return f[-1]



if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Brute force tri tilling.")
  parser.add_argument("--n", default=4, type=int, help="size of grid")
  args = parser.parse_args()
  print("Total combinations: %s." % tri_tiling_fast(args.n))
