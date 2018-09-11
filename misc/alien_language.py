# Given a dictionary of words that are lexicographically sorted, find the
# alphabet in sorted order of the input language.
#
# Example: ["Art", "Rat", "Cat", "Car"]
# Returns: [a, t, r, c]

# Assuming we have a graph structure / topological sort implemented.
# Runtime will be cost of comparisons + time for top sort. Let A be the
# number of characters in the alphabet and N be the number of words, E be the
# number of edges. Should note that worst case E = A^2 + A / 2
# O(N + A) + O(A + E)
def get_alphabet(words):
  letter_orders = Graph()
  for i in range(len(words) - 1):
    word1 = words[i]
    word2 = words[i + 1]
    # Iterate through each char of both words. If one word is longer than
    # another only compare the present characters.
    for j in range(min(len(word1), len(word2))):
      if word1[j] != word2[j]:
        letter_orders.add_edge(word1[j], word2[j])
        break
  return top_sort(letter_orders)


# Assuming all of this is implemented for you.

class Graph:

  nodes = set()
  edges = set()

  def __init__(self):
    return

  def add_node(self, node):
    self.nodes.add(node)

  def add_edge(self, from_node, to_node):
    if from_node not in self.nodes:
      self.add_node(from_node)
    if to_node not in self.nodes:
      self.add_node(to_node)
    self.edges.add((from_node, to_node))


def top_sort(graph):
  return
