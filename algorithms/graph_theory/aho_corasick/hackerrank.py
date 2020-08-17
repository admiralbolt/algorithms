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


def get_health(genes, health, first, last, d, trie):
    keywords = set()
    health_dict = collections.defaultdict(int)
    for i in range(first, last + 1):
        gene = genes[i]
        keywords.add(gene)
        health_dict[gene] += health[i]

    occurrences = trie.get_occurrences(d)
    # Score occurrences
    total_score = 0
    for gene, number in occurrences.items():
        total_score += health_dict[gene] * number
    return total_score


if __name__ == '__main__':
    true_start = time.time()
    n = int(input())

    genes = input().rstrip().split()

    health = list(map(int, input().rstrip().split()))

    s = int(input())

    health_values = []

    g = list(set(genes))

    start_time = time.time()

    trie = Trie()
    time_it("trie2 init")
    trie.construct(g)
    time_it("total construction")

    for s_itr in range(s):
        firstLastd = input().split()

        first = int(firstLastd[0])

        last = int(firstLastd[1])

        d = firstLastd[2]

        health_values.append(get_health(genes, health, first, last, d, trie))

    print(min(health_values), max(health_values))
    print(f"GRAND TOTAL: {time.time() - true_start}")
