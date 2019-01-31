import collections
import pickle

from pprint import pprint

composer_graph = collections.defaultdict(list)
og_slots = collections.defaultdict(list)
slot_graph = collections.defaultdict(list)
counts = collections.defaultdict(int)
final_slots = collections.defaultdict(list)
num_composers = 0
with open("poll.csv", "r") as rh:
  for line in rh.readlines()[1:]:
    composer_slot = line.strip().split(",")
    if composer_slot[0] == "Andrea Ramsey":
      counts[composer_slot[1]] += 1
      final_slots[composer_slot[1]].append(composer_slot[0])
      continue
    if composer_slot[0] not in composer_graph:
      num_composers += 1
    composer_graph[composer_slot[0]].append(composer_slot[1])
    slot_graph[composer_slot[1]].append(composer_slot[0])
    og_slots[composer_slot[1]].append(composer_slot[0])


# The rest of the composers get 1 slot, so this is *almost* bi-partite matching,
# however, there will be overlaps. So, we want to minimize overlaps but give
# each composer a slot.
# We will attempt this with a greedy algorithm by using total_counts and counts.
# We will iterate through slots in order of how many are signed up for those slots.
# total_counts[slot] = 1, AND counts[slot] = 0, they win their slot. We prune them
# from the graph and repeat this process until there are no slots left with total_counts[slot] = 1.
# We then continue, incrementing total_counts allowed to 2, keeping counts[slot] at 0.
# Again, each time we prune, restarting from checking for total_counts[slot] = 1

def prune(composer_graph, slot_graph, composer, slot):
  """Prune a composer from the graph.

  This involves removing them from the graph, and updating the number of composers
  vying for a slot.
  """
  for slot in composer_graph[composer]:
    slot_graph[slot].remove(composer)
    if not slot_graph[slot]:
      del slot_graph[slot]
  del composer_graph[composer]

def get_node_with_least_competition(slot_graph):
  min_count = 100
  return_slot = ""
  return_composers = []
  # Look at slots in order of how many people are currently occupying them.
  for slot, composers in sorted(slot_graph.items(), key=lambda x: counts[x[0]]):
    # If len(composers) == 1, only 1 person is vying for this spot. Return immediately.
    if len(composers) == 1:
      return slot, composers
    if len(composers) < min_count:
      min_count = len(composers)
      return_slot = slot
      return_composers = composers
  return return_slot, return_composers

def choose_minimal(composer_graph, slot_graph, composers, slot):
  """Greedy here, select the minimally affecting composer among multiple.

  We do this by comparing the number of slots available.
  """
  return_composer = ""
  min_slots = 100
  for composer in composers:
    total_slots = len(composer_graph[composer])
    if total_slots < min_slots:
      min_slots = total_slots
      return_composer = composer
  return return_composer

def select_composer(final_slots, composer_graph, slot_graph, composer, slot):
  # print("SELECTED composer: %s for slot: %s." % (composer, slot))
  final_slots[slot].append(composer)
  counts[slot] += 1
  prune(composer_graph, slot_graph, composer, slot)


# Iterate until we find a spot for all composers.
while sum([len(vals) for vals in final_slots.values()]) < num_composers + 3:
  slot, composers = get_node_with_least_competition(slot_graph)
  if len(composers) == 1:
    select_composer(final_slots, composer_graph, slot_graph, composers[0], slot)
    continue
  # We have multiple composers vying for slots left.
  composer = choose_minimal(composer_graph, slot_graph, composers, slot)
  select_composer(final_slots, composer_graph, slot_graph, composer, slot)

with open("labels.pickle", "rb") as rh:
  labels = pickle.load(rh)
  for label in labels:
    if not label:
      continue
    print("%s: %s." % (label, final_slots[label]))
