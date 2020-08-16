import math
import os
import random
import re
import sys
import time

from aho_corasick import *

start_time = time.time()
def time_it(title):
  global start_time
  print(f"{title} time: {time.time() - start_time}")
  start_time = time.time()

def get_health(genes, health, first, last, d):
    keywords = set()
    health_dict = collections.defaultdict(int)
    for i in range(first, last + 1):
        gene = genes[i]
        keywords.add(gene)
        health_dict[gene] += health[i]

    start_time = time.time()
    sorted_words = sorted(keywords, key=lambda word: (len(word), word))
    time_it("sort keywords")
    trie = Trie()
    time_it("trie init")
    trie.parse_keywords(sorted_words)
    time_it("parse words")

    # Manual parse keywords
    parent_edges = {}
    child_edges = collections.defaultdict(set)
    nodes = set()
    for keyword in sorted_words:
      nodes.add(keyword)
      parent_edges[keyword] = keyword[:-1]
      child_edges[keyword[:-1]].add(keyword)
    time_it("manual parse")



    trie.add_suffix_links()
    time_it("suffix links")
    trie.add_output_links()
    time_it("output links")
    start_time = time.time()
    occurrences = trie.get_occurrences(d)
    print(f"get_occurrences: {time.time() - start_time}")
    # Score occurrences
    total_score = 0
    for gene, number in occurrences.items():
        total_score += health_dict[gene] * number
    return total_score




if __name__ == '__main__':
    n = int(input())

    genes = input().rstrip().split()

    health = list(map(int, input().rstrip().split()))

    s = int(input())

    health_values = []

    for s_itr in range(s):
        firstLastd = input().split()

        first = int(firstLastd[0])

        last = int(firstLastd[1])

        d = firstLastd[2]

        health_values.append(get_health(genes, health, first, last, d))

    print(min(health_values), max(health_values))
