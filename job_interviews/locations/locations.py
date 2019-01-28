# Python 3
import collections
import sys, json

# Read from stdin
locations = json.loads(sys.stdin.read())

# Effectively, we are constructing a set of unique rooted
# graphs and then traversing them.

# Helper function to traverse our graph.
def traverse_location(location_graph, names, current_id, depth=0):
  print(f"{'-' * depth}{names[current_id]}")
  if current_id in location_graph:
    for child_id in location_graph[current_id]:
      traverse_location(location_graph, names, child_id, depth + 1)

names = {}
location_graph = collections.defaultdict(list)
location_roots = []
# By sorting them ahead of time we are guaranteed
# to print them in sorted order in the future.
for location in sorted(locations, key=lambda x: x["name"]):
  names[location["id"]] = location["name"]
  if location["parent_id"]:
    location_graph[location["parent_id"]].append(
      location["id"])
  else:
    # We found a root node.
    location_roots.append(location["id"])

# Actually traverse each root node.
for root in location_roots:
  traverse_location(location_graph, names, root)
