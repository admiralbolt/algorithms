"""
Classes are slow, so instead we try to use arrays for everything. Wooo...

Our nodes have 5 values:
[value, left_node_index, right_node_index, total_right, duplicates]

Our "tree" is just an array of nodes
"""
import cProfile
import random

def insert(tree, value):
  if not tree:
    tree.append([value, -1, -1, 0, 0])
    return 0

  swaps = 0
  inserted = False
  node = tree[0]
  # I really hate the way this is written, but I'm trying to avoid using
  # recursion to avoid hitting max depth. I think this is technically faster
  # since it avoids the call stack but :shrug:
  while not inserted:
    if value > node[0]:
      node[3] += 1
      if node[2] != -1:
        node = tree[node[2]]
        continue

      node[2] = len(tree)
      tree.append([value, -1, -1, 0, 0])
      inserted = True

    elif value < node[0]:
      swaps += (node[4] + node[3] + 1)
      if node[1] != -1:
        node = tree[node[1]]
        continue

      node[1] = len(tree)
      tree.append([value, -1, -1, 0, 0])
      inserted = True

    elif value == node[0]:
      # Increment duplicates. swaps increase based on total right hand.
      node[4] += 1
      swaps += node[3]
      inserted = True

  return swaps

def only(l):
  only_decreasing = True
  only_increasing = True
  for i in range(len(l) - 1):
    if l[i + 1] < l[i]:
      only_increasing = False
    elif l[i + 1] > l[i]:
      only_decreasing = False
  return only_decreasing, only_increasing


def analyze_insertion_sort(l):
  only_decreasing, only_increasing = only(l)
  if only_increasing:
    return 0
  elif only_decreasing:
    n = len(l) - 1
    return n * (n + 1) // 2

  tree = []
  total_swaps = 0
  for item in l:
    total_swaps += insert(tree, item)
  return total_swaps

l = [random.randint(1, 100) for _ in range(20)]
print(l)
print(analyze_insertion_sort(l))

from naive import analyze_insertion_sort_slow
print(analyze_insertion_sort_slow(l))

if __name__ == "__main__":
  t = int(input())
  for t_itr in range(t):
    n = int(input())
    l = list(map(int, input().rstrip().split()))
    cProfile.run("analyze_insertion_sort(l)")
    # result = analyze_insertion_sort(l)
    # print(result)
