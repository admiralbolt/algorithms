# https://www.hackerrank.com/challenges/robot/problem

import copy
import os


class PathGraph:

  def __init__(self, energies):
    self.all_paths = []
    self.graph = []
    self.number_of_nodes = len(energies)
    self.visited = [False] * self.number_of_nodes
    for i, energy in enumerate(energies):
      self.graph.append(list(range(i + 1, min(i + 1 + energy, len(energies)))))

  def load_all_paths(self, source, target, path):
    self.visited[source] = True
    path.append(source)
    if source == target:
      self.all_paths.append(copy.deepcopy(path))
    else:
      for i in self.graph[source]:
        if not self.visited[i]:
          self.load_all_paths(i, target, path)
    path.pop()
    self.visited[source] = False

  def get_all_paths(self):
    if not self.all_paths:
      self.load_all_paths(0, self.number_of_nodes -1, [])
    return self.all_paths


def robot(scores, energies):
  pg = PathGraph(energies)
  max_score = 0
  max_path = []
  for path in pg.get_all_paths():
    path_score = sum([scores[i] for i in range(0, len(scores)) if i not in path]) + scores[-1]
    if path_score > max_score:
      max_score = path_score
      max_path = path
  print(max_path)
  return max_score


if __name__ == "__main__":
  try:
    n = int(input())
    scores = []
    energies = []
    for _ in range(n):
      score, energy = tuple(map(int, input().strip().split()))
      scores.append(score)
      energies.append(energy)
    result = robot(scores, energies)
    if "OUTPUT_PATH" in os.environ:
      # Running on hackerrank.
      fptr = open(os.environ["OUTPUT_PATH"], "w")
      fptr.write(str(result) + "\n")
      fptr.close()
    else:
      # Running locally.
      print(result)
  except Exception as e:
    print(e)
