# Find the sum of all the multiples of 3 or 5 below 1000.
import argparse
import math
import math_utils

parser = argparse.ArgumentParser(description="Sum some.")
parser.add_argument("--max", default=1000, type=int, help="maximum value")
args = parser.parse_args()

def slow_solve(max_inclusive):
  """
  Iterate through the numbers and sum them if they are divisible by 3 or 5.
  """
  total_sum = 0
  for i in range(1, max_inclusive):
    if i % 3 == 0 or i % 5 == 0:
      numbers.append(i)
      total_sum += i
  return total_sum

def discrete_solve(max_inclusive):
  """
  Discretly solves the problem with the following formula:
    R_3 + R_5 - R_15
  Where:
    R_3 = sum all numbers divisble by 3 <= max
    R_5 = sum all numbers divisible by 5 <= max
    R_15 = sum all numbers divisble by 15 <= max
  The sums are calculated quickly using the guassian sum, we can think of it
  in the following way.
  If the max is 6 we have 3 and 6 divisble by 3 or 3 * 3
  If the max is 9 we have 3, 6, and 9 divisble by 3 or 6 * 3
  If the max is 12 we have 3, 6, 9, and 12 divisble by 3 or 12 * 3
  ...
  """
  three_sum = math_utils.gaussian_sum(math.floor(max_inclusive / 3)) * 3
  five_sum = math_utils.gaussian_sum(math.floor(max_inclusive / 5)) * 5
  fifteen_sum = math_utils.gaussian_sum(math.floor(max_inclusive / 15)) * 15
  return int(three_sum + five_sum - fifteen_sum)


if __name__ == "__main__":
  print("Total Sum: %s." % discrete_solve(args.max))
