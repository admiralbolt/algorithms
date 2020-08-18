from aho_corasick import *

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

trie = Trie()
trie.construct(keywords)
trie.render("sample.gv")
