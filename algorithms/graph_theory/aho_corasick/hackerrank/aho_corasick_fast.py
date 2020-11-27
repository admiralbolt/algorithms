"""
An implementation of the aho corasick automaton
for string matching.

All of this, for 50 hacker rank points.
SMH

I want to point out that this code was very nice looking at some point.
And now it is garbage. Will probably try to cleanup the old version and do
some performance improvements at some point.

The amount of optimizations required for it to work on hackerrank are ridiculous.
"""
import collections
import time


class Trie:

  def __init__(self):
    self.nodes = {}
    self.root = ["", False, None, None]
    # self.root = {
    #   "name": "",
    #   "output": False,
    #   "output_node": None
    # }
    self.nodes[""] = self.root
    return

  def get_longest_strict_suffix(self, node, letter):
    target_node = node[2]
    target_name = f"{target_node[0]}{letter}"

    if target_name in self.nodes:
      return self.nodes[target_name]

    while target_node[0]:
      target_node = target_node[2]
      target_name = f"{target_node[0]}{letter}"
      if target_name in self.nodes:
        return self.nodes[target_name]

    return self.root

  def construct(self, keywords):
    sorted_keywords = sorted(keywords)
    word_length = []
    max_length = 0
    for word in sorted_keywords:
      l = len(word)
      word_length.append(l)
      if l > max_length:
        max_length = l
    for i in range(max_length):
      for j, word in enumerate(sorted_keywords):
        word_len = word_length[j]
        if i >= word_len:
          continue

        node_name = word[:i+1]
        if node_name in self.nodes:
          continue

        # Nodes are [name, output, suffix, output_node]
        node = [node_name, i == word_len - 1]

        # node = {
        #   "name": node_name,
        #   "output": (i == word_len - 1),
        #   "output_node": None
        # }

        parent_name = word[:i]
        if not parent_name:
          # node["suffix_node"] = self.root
          node.append(self.root)
          node.append(None)
        else:
          node.append(self.get_longest_strict_suffix(self.nodes[parent_name], word[i]))
          node.append(node[2] if node[2][1] else node[2][3])
          # node["suffix_node"] = self.get_longest_strict_suffix(self.nodes[parent_name], word[i])
          # node["output_node"] = node["suffix_node"] if node["suffix_node"]["output"] else node["suffix_node"]["output_node"]

        self.nodes[node_name] = node
    return

  def get_occurrences(self, search):
    """Walks through the string and gets all occurences."""
    current_node = self.root
    occurrences = collections.defaultdict(int)
    for letter in search:
      target_name = f"{current_node[0]}{letter}"
      # If the node exists we want to update occurences.
      # We need to follow all output links and update
      # the occurences for those as well.
      if target_name in self.nodes:
        current_node = self.nodes[target_name]
        self.count(occurrences, current_node)
        continue


      if not current_node[0]:
        continue

      current_node = self.get_longest_strict_suffix(current_node, letter)
      if current_node[0]:
        self.count(occurrences, current_node)
    return occurrences

  def count(self, occurrences, current_node):
    if current_node[1]:
      occurrences[current_node[0]] += 1
    if current_node[3]:
      tmp = current_node
      while tmp[3]:
        occurrences[tmp[3][0]] += 1
        tmp = tmp[3]
    return
