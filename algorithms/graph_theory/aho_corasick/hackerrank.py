import math
import os
import random
import re
import sys
import time

import cProfile

from aho_corasick import *

start_time = time.time()
def time_it(title):
  global start_time
  print(f"{title} time: {time.time() - start_time}")
  start_time = time.time()

def get_gene_value(health_values, gene, first, last):
  if gene not in health_values:
    return 0

  value = 0
  for index, worth in health_values[gene]:
    if index >= first and index <= last:
      value += worth
  return value



def get_health(health_values, first, last, d, trie):
    occurrences = trie.get_occurrences(d)
    # Score occurrences
    total_score = 0
    for gene, number in occurrences.items():
        total_score += get_gene_value(health_values, gene, first, last) * number
    return total_score


if __name__ == '__main__':
    true_start = time.time()
    n = int(input())

    genes = input().rstrip().split()

    health = list(map(int, input().rstrip().split()))

    health_values = collections.defaultdict(list)
    for i, gene in enumerate(genes):
      health_values[gene].append((i, health[i]))


    s = int(input())

    start_time = time.time()
    print(f"warmup: {start_time - true_start}")

    trie = Trie()
    time_it("trie2 init")
    # cProfile.run('trie.construct(genes)')
    # sys.exit()
    trie.construct(genes)
    time_it("total construction")

    min_health = 100000000000000000000000
    max_health = -1
    for s_itr in range(s):
        firstLastd = input().split()

        first = int(firstLastd[0])

        last = int(firstLastd[1])

        d = firstLastd[2]

        health = get_health(health_values, first, last, d, trie)
        if health > max_health:
          max_health = health
        if health < min_health:
          min_health = health

    print(min_health, max_health)
    print(f"GRAND TOTAL: {time.time() - true_start}")
