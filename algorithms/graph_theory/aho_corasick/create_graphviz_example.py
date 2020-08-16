"""
Example visualization for an Aho-Corasick automaton.
"""
import collections
from graphviz import Digraph

keywords = [
  "a",
  "ab",
  "aab",
  "aaba",
  "bc",
  "bca",
  "baa",
  "aa",
  "abcd",
  "c",
  "cb",
  "cbd"
]

d = Digraph(strict=False)
d.node("root", "")

edges = collections.defaultdict(set)
for word in keywords:
  for i, letter in enumerate(word):
    # If it's the last letter in the word make it an output node.
    if i == len(word) - 1:
      d.node(word[:i+1], letter, {
        "color": "lightblue2",
        "style": "filled"
      })
    else:
      d.node(word[:i+1], letter)

    # Make edges
    if i == 0 and letter not in edges["root"]:
      d.edge("root", letter)
      edges["root"].add(letter)
    elif word[:i+1] not in edges[word[:i]]:
      d.edge(word[:i], word[:i+1])
      edges[word[:i]].add(word[:i+1])

d.render("automaton_trie.gv")

# Construct our suffixes manually
d.edge("aa", "a", None, {"color": "blue", "constraint": "false"})
d.edge("aab", "ab", None, {"color": "blue", "constraint": "false"})
d.edge("ab", "b", None, {"color": "blue", "constraint": "false"})
d.edge("abc", "bc", None, {"color": "blue", "constraint": "false"})
d.edge("bc", "c", None, {"color": "blue", "constraint": "false"})
d.edge("ba", "a", None, {"color": "blue", "constraint": "false"})
d.edge("baa", "aa", None, {"color": "blue", "constraint": "false"})
d.edge("bca", "a", None, {"color": "blue", "constraint": "false"})
d.edge("cb", "b", None, {"color": "blue", "constraint": "false"})
d.edge("aaba", "ba", None, {"color": "blue", "constraint": "false"})

d.render("automaton_suffix.gv")

# Construct our output links manually
d.edge("aa", "a", None, {"color": "orange", "constraint": "false"})
d.edge("aab", "ab", None, {"color": "orange", "constraint": "false"})
d.edge("abc", "bc", None, {"color": "orange", "constraint": "false"})
d.edge("baa", "aa", None, {"color": "orange", "constraint": "false"})
d.edge("bc", "c", None, {"color": "orange", "constraint": "false"})
d.edge("bca", "a", None, {"color": "orange", "constraint": "false"})
d.edge("ba", "a", None, {"color": "orange", "constraint": "false"})
d.edge("aaba", "a", None, {"color": "orange", "constraint": "false"})

d.render("automaton_output.gv")
