import collections

# Read gross inputs.
# Busses will be created a list of tuples [(start, end)], ...]
# Cities will be a list of ints [location, ...]
def read_gbus_input():
  busses = []
  cities = []
  gbus_count = int(input())
  city_ranges = input().strip().split(" ")
  for i in range(0, len(city_ranges), 2):
    busses.append((int(city_ranges[i]), int(city_ranges[i + 1])))
  city_count = int(input())
  for i in range(city_count):
    cities.append(int(input()))
  return busses, cities


# Returns a map of cities -> number of busses serving them.
def get_serve_count(busses):
  serve_count = collections.defaultdict(int)
  for bus_start, bus_finish in busses:
    for city in range(bus_start, bus_finish + 1):
      serve_count[city] += 1
  return serve_count


def main():
  test_cases = int(input())
  for i in range(test_cases):
    busses, cities = read_gbus_input()
    serve_count = get_serve_count(busses)
    visited_str = " ".join([str(serve_count[city]) for city in cities])
    print(f"Case #{i + 1}: {visited_str}")
    # Chomp the blank line.
    input()


if __name__ == "__main__":
  main()
