def main():
  test_cases = int(input())
  for i in range(test_cases):
    energy, rival_teams = map(int, input().split(" "))
    honor = 0
    # O(nlogn) bit.
    team_skill = sorted(map(int, input().split(" ")))
    weakest_team = 0
    strongest_team = -1
    # Greedy algorithm: Dance lowest until we can't, recruit highest.
    # Takes O(n) time.
    while len(team_skill) > 0:
      # If we have energy beat the lowest team.
      if energy > team_skill[0]:
        # Base cases --
        energy -= team_skill[0]
        honor += 1
        del team_skill[0]
      # We don't want to recruit the last team.
      elif honor > 0 and len(team_skill) > 1:
        energy += team_skill[-1]
        honor -= 1
        del team_skill[-1]
      else:
        # Can't dance no more. :(
        break
    print(f"Case #{i + 1}: {honor}")


if __name__ == "__main__":
  main()
