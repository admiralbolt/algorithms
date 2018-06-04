# https://www.hackerrank.com/challenges/matrix-rotation-algo/problem

class Loop:
  """
  A class representing a loop in the matrix. Given bounds it will calaculate
  all possible indices that fall in a particular loop, as well as providing
  a way to get the next index from a current position.
  """

  def __init__(self, matrix, m_lower, m_upper, n_lower, n_upper):
    self.point_indexes = []
    self.point_values = []
    # Load all possible loop indices by fixing one bound, then iterating
    # through the other. We stop 1 before the end to avoid duplicates.
    # Fix n = n_lower
    for m in range(m_lower, m_upper):
      self.__add_point(matrix, m, n_lower)
    # Fix m = m_upper
    for n in range(n_lower, n_upper):
      self.__add_point(matrix, m_upper, n)
    # Fix n = n_upper
    for m in range(m_upper, m_lower, -1):
      self.__add_point(matrix, m, n_upper)
    # Fix m = m_lower
    for n in range(n_upper, n_lower, -1):
      self.__add_point(matrix, m_lower, n)

    self.num_points = len(self.point_indexes)
    return

  def __add_point(self, matrix, m, n):
    self.point_indexes.append((m, n))
    self.point_values.append(matrix[m][n])

  def rotate_loop(self, num_rotations):
     """Returns a dictionary of (x, y) -> val pairs."""
     pivot = num_rotations % self.num_points
     return dict(zip(self.point_indexes, self.point_values[-pivot:] + self.point_values[:-pivot]))

def generate_all_loops(matrix):
  """Gets all Loops in a given matrix."""
  rows = len(matrix)
  cols = len(matrix[0])
  m_lower = 0
  m_upper = len(matrix) - 1
  n_lower = 0
  n_upper = len(matrix[0]) - 1
  lower = 0
  upper = min(m_upper, n_upper)
  all_loops = []
  while upper >= lower:
    # upper/lower represent columns not rows.
    if rows > cols:
      all_loops.append(Loop(matrix, m_lower, m_upper, lower, upper))
      m_lower += 1
      m_upper -= 1
    else:
      all_loops.append(Loop(matrix, lower, upper, n_lower, n_upper))
      n_lower += 1
      n_upper -= 1
    upper -= 1
    lower += 1
  return all_loops


def matrix_rotation(matrix, num_rotations):
  all_loops = generate_all_loops(matrix)
  point_dict = {}
  for loop in all_loops:
    point_dict.update(loop.rotate_loop(num_rotations))
  num_rows = len(matrix)
  num_cols = len(matrix[0])
  for m in range(num_rows):
    for n in range(num_cols):
      print(point_dict[(m, n)], end="")
      if n == num_cols - 1:
        print()
      else:
        print(" ", end="")



if __name__ == "__main__":
  mnr = input().split()
  rows, cols, num_rotations = map(int, mnr)
  matrix = []
  for _ in range(rows):
    matrix.append(list(map(int, input().rstrip().split())))
  matrix_rotation(matrix, num_rotations)
