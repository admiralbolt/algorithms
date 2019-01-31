import collections
import copy
import pickle

composer_graph = collections.defaultdict(list)
og_slots = collections.defaultdict(list)
slot_graph = collections.defaultdict(list)
counts = collections.defaultdict(int)
final_slots = collections.defaultdict(list)
composers = []
slots = []
with open("poll.csv", "r") as rh:
  for line in rh.readlines()[1:]:
    composer_slot = line.strip().split(",")
    if composer_slot[0] == "Andrea Ramsey":
      counts[composer_slot[1]] += 1
      final_slots[composer_slot[1]].append(composer_slot[0])
      continue
    composer_graph[composer_slot[0]].append(composer_slot[1])
    slot_graph[composer_slot[1]].append(composer_slot[0])
    og_slots[composer_slot[1]].append(composer_slot[0])
    if composer_slot[0] not in composers:
      composers.append(composer_slot[0])

num_composers = len(composers)
all_possible = []
print(composers)

def brute(final_slots = [], depth = 0):
  if depth == num_composers:
    all_possible.append(final_slots)
    return
  composer = composers[depth]
  for slot in composer_graph[composer]:
    brute(final_slots + [(slot, composer)], depth + 1)

brute()

with open("all_possible.pickle", "wb") as wh:
  pickle.dump(all_possible, wh)
