# Given a list of synonym pairs, write a function to determine if some pairs
# of queries are synonyms. Two pairs of queries are synonyms if you can
# match them word by word in order including synonyms.
#
# Example:
# Synonyms = [("rate", "ratings"), ("approval", "popularity")]
# Queries = [("obama approval rate", "obama popularity ratings"), ("obama approval rates", "obama popularity ratings")]
# Output = [True, False]

# {
#   rate: set(ratings),
#   ratings: set(rate),
# }

import collections

def synonyms(queries, synonyms):
  synonym_set = construct_synonym_set(synonyms)
  results = []
  for query1, query2 in queries:
    results.append(are_queries_synonymous(synonym_set, query1, query2))
  return results


def are_queries_synonymous(synonym_set, query1, query2):
  for word1, word2 in zip(query1.split(), query2.split()):
    if word2 not in synonym_set[word1] and word1 != word2:
      return False
  return True

# Constructs our synonym set with words mapping to sets of their synonyms.
def construct_synonym_set(synonyms):
  s = collections.defaultdict(set)
  for word1, word2 in synonyms:
    s[word1].add(word2)
    s[word2].add(word1)
  return s
