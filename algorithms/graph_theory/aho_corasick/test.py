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

s = "aabcdaabc"

# a: 4
# aa: 2
# aab: 2
# ab: 2
# bc: 2
# c: 2
# abcd: 1

keywords = ["a", "b", "c", "aa", "d", "b"][0:5]
s = "xyz"

trie = Trie()
trie.parse_keywords(keywords)
trie.add_suffix_links()
trie.add_output_links()
print(trie.get_occurrences(s))
trie.render("test.gv")
