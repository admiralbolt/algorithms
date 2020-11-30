"""
What we effectively need is a fast way of bisecting and inserting, which sounds
suspciously like a tree to me. So we'll make a binary search tree and track
some extra stuff to figure out how many swaps are necessary. This should reduce
the complexity to O(nlog(n)) instead of n^2
"""

class Node:

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    # Total number of nodes in the right tree.
    self.total_right = 0
    # Number of duplicate values. I don't actually want to add duplicates to the
    # tree, it complicates things.
    self.duplicates = 0

  def __repr__(self):
    return f"{self.value}"

class SwapTree:

  def __init__(self):
    # Mapping from value -> node
    self.root = None
    self.nodes = {}
    self.count = 0

  def insert(self, value):
    if self.root is None:
      self.root = Node(value)
      self.nodes[value] = self.root
      return

    self.traverse_and_insert(value, self.root)

  def traverse_and_insert(self, value, node=None):
    """Traverse the tree and insert our new node.

    While inserting, updates dup and right hand side count values as necessary,
    and increases the total number of swaps required.
    """
    node = node or self.root
    if value > node.value:
      node.total_right += 1
      if node.right:
        return self.traverse_and_insert(value, node=node.right)


      node.right = Node(value)
      self.nodes[value] = node.right

    elif value < node.value:
      self.count += (node.total_right + node.duplicates + 1)
      if node.left:
        return self.traverse_and_insert(value, node=node.left)

      node.left = Node(value)
      self.nodes[value] = node.left

    elif value == node.value:
      # If we hit a duplicate value, the number of swaps necessary is the total
      # number in the right hand tree.
      node.duplicates += 1
      self.count += node.total_right
      return

def analyze_insertion_sort(l):
  tree = SwapTree()
  for item in l:
    tree.insert(item)
  return tree.count

if __name__ == "__main__":
  t = int(input())
  for t_itr in range(t):
    n = int(input())
    l = list(map(int, input().rstrip().split()))
    result = analyze_insertion_sort(l)
    print(result)
