# You are given a string input that consists of uppercase ascii letters, 'A' to
# 'Z'. Write a function that returns the first index i, such that
# input[i]...input[i+25] forms a permutation of all letters 'A', 'Z'.

import string

NUM_LETTERS = 26

def char_to_index():
  char_map = {}
  for i, letter in enumerate(string.ascii_uppercase):
    char_map[letter] = i
  return char_map

def find_permutation(input_string):
  for i in range(len(input_string)):
    if is_permutation(input_string, i)
      return i
  return -1

def is_permutation(input_string, start):
  occurences = [False] * NUM_LETTERS
  for i in range(start, start + NUM_LETTERS + 1):
    occurences[char_map[input_string[i]]] = True
  for occurence in occurences:
    if not occurence:
      return False
  return True

# Duplicate based
def find_permutation_duplicates(input_string):
  last_seen = [-1] * NUM_LETTERS
  for i, letter in enumerate(input_string):
    last_seen[letter
