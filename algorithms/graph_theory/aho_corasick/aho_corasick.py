"""
An implementation of the aho corasick automaton
for string matching.

All of this, for 50 hacker rank points.
SMH
"""
import collections
import functools
import hashlib
import queue

from graphviz import Digraph

class Trie:

  def __init__(self):
    self.nodes = {}
    self.nodes[""] = TrieNode(value="", name="")
    self.root = self.nodes[""]
    return

  def add_node(self, parent=None, node=None):
    """Adds a node to the trie."""
    if node.name in self.nodes:
      # We can potential process out of order, and need to update
      # the output value accordinly.
      if node.output:
        self.nodes[node.name].output = True
      return
    if parent not in self.nodes:
      parent = ""
    self.nodes[node.name] = node
    self.nodes[parent].add_child(node)
    return

  @functools.lru_cache(maxsize=None)
  def get_longest_strict_suffix(self, node, letter):
    """
    yield node.suffix_node
    if node.suffix_node != self.nodes[""] and node.suffix_node is not None:
      yield from self.follow_suffixes(node.suffix_node)
    """
    target_node = node
    while target_node != self.root:
      target_name = f"{target_node.name}{letter}"
      if target_name in self.nodes:
        return self.nodes[target_name]
      target_node = target_node.suffix_node
    return self.root

  def add_suffix_links(self):
    """Constructs suffix links."""
    for child in self.bfs(self.root):
      if child.parent == self.root:
        child.suffix_node = self.root
        continue

      # Check the suffix link of the parent...
      for suffix_node in self.follow_suffixes(child.parent):
        target = f"{suffix_node.name}{child.value}"
        if target in self.nodes:
          child.suffix_node = self.nodes[target]
          break
      if not child.suffix_node:
        child.suffix_node = self.root
    return

  def add_output_links(self):
    """Construct output links."""
    for node in self.nodes.values():
      if node == self.root:
        continue

      for suffix_node in self.follow_suffixes(node):
        if suffix_node.output:
          node.output_node = suffix_node
          break
    return

  def bfs(self, node):
    """Do a breadth-first search starting from a node."""
    q = queue.Queue()
    q.put(node)

    while q.qsize() > 0:
      current_node = q.get()
      if current_node != self.root:
        yield current_node

      for child in current_node.children:
        q.put(child)

  def follow_suffixes(self, node):
    yield node.suffix_node
    if node.suffix_node != self.nodes[""] and node.suffix_node is not None:
      yield from self.follow_suffixes(node.suffix_node)

  def parse_keywords(self, keywords):
    """Convert keywords into a trie."""
    for word in keywords:
      last_index = len(word) - 1
      parent = ""
      for i, letter in enumerate(word):
        self.add_node(
          parent=parent,
          node=TrieNode(
            value=letter,
            name=parent + letter,
            parent=self.nodes.get(parent, self.nodes[""]),
            output=(i == last_index)
          )
        )
        parent += letter
    return

  def render(self, fname):
    """Renders the trie to a graphviz diagram."""
    d = Digraph()
    for name, node in self.nodes.items():
      if node.output:
        d.node(name, node.value, {"color": "lightblue2", "style": "filled"})
      else:
        d.node(name, node.value)

      # Render child edges
      for child in node.children:
        d.edge(name, child.name)

      # Render output & suffix links
      if node.suffix_node:
        d.edge(name, node.suffix_node.name, None, {"color": "blue", "constraint": "false"})
      if node.output_node:
        d.edge(name, node.output_node.name, None, {"color": "orange", "constraint": "false"})

    d.render(fname)
    return

  def get_occurrences(self, search):
    """Walks through the string and gets all occurences."""
    current_node = self.root
    occurrences = collections.defaultdict(int)
    for letter in search:
      target_name = f"{current_node.name}{letter}"
      # If the node exists we want to update occurences.
      # We need to follow all output links and update
      # the occurences for those as well.
      if target_name in self.nodes:
        current_node = self.nodes[target_name]
        self.count(occurrences, current_node)
        continue


      if current_node == self.root:
        continue

      found = False
      # Follow suffix nodes attempting to save as much context as we can.
      for suffix_node in self.follow_suffixes(current_node):
        target_name = f"{suffix_node.name}{letter}"
        # Same as before, if we find a node update the current node and count.
        if target_name in self.nodes:
          found = True
          current_node = self.nodes[target_name]
          self.count(occurrences, current_node)
          break

      # If we didn't find any useful suffixes, reset our node back to the root.
      if not found:
        current_node = self.root
    return occurrences

  def count(self, occurrences, current_node):
    if current_node.output:
      occurrences[current_node.name] += 1
    if current_node.output_node:
      tmp = current_node
      while tmp.output_node:
        occurrences[tmp.output_node.name] += 1
        tmp = tmp.output_node
    return




class TrieNode:

  def __init__(self, value=None, name=None, parent=None, output=False):
    self.name = name
    self.value = value
    # Determines if this is an output keyword.
    self.output = output
    self.parent = parent
    self.children = set()
    # Edges for outputs & longest strict suffixes.
    self.output_node = None
    self.suffix_node = None
    return

  def __repr__(self):
    return self.name

  def __eq__(self, obj):
    return self.name == obj.name

  def __hash__(self):
    return int(hashlib.sha1(self.name.encode("utf-8")).hexdigest(), 16) % (10 ** 8)

  def add_child(self, node):
    """Add the passed in node as a child to the current node."""
    self.children.add(node)
