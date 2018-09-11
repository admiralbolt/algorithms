# How much water can a bar graph hold? (Easy to draw whiteboard examples)
# Example: [3, 2, 7, 2, 3, 7] -> 10 units of water.

# O(n) solution. We want to find the point at which we go from decreasing values
# to increasing. Each of these points creates a discrete lake, which we will
# calculate the total area of.
def water(bar_graph):
  left = -1
  right = -1
  lake_width = 0
  lake_bottom = 0
  total_water = 0
  for i, height in enumerate(bar_graph):
    if left == -1:
      left = height
    elif height > bar_graph[i - 1]:
      # Do calculation here
      ridge_height = min(left, height)
      total_water += lake_width * ridge_height - lake_bottom
      lake_bottom = lake_width * ridge_height
      # If the height is greater than our left ridge, it becomes the new left
      # value looking forward.
      if height > left:
        left = height
        lake_width = 0
        lake_bottom = 0
      else:
        lake_width += 1
        lake_bottom += height
    else:
      lake_width += 1
      lake_bottom += height
  return total_water


# Calculate the water height at each point, by finding the tallest bar to the
# left / right of the current. The min(left, right) - curr will be the heigh
# of the water at location x.
def water_slow(bar_graph):
  left = -1
  right = -1
  total_water = 0
  for i, height in enumerate(bar_graph):
    # Skip the first / last elements
    if i == 0 or i == len(bar_graph) -1:
      continue
    max_left = max(bar_graph[:i])
    max_right = max(bar_graph[i + 1:])
    if max_left > height and max_right > height:
      total_water += min(max_left, max_right) - height
  return total_water
