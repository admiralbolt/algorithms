import string

letter_score = {}
for i, letter in enumerate(string.ascii_lowercase):
  letter_score[letter] = i + 1


def calculate_score(i, name):
  return sum([letter_score[letter] for letter in name]) * (i + 1)


# All the names are on 1 line.
names = []
with open("p022_names.txt", "r") as rh:
  names = rh.readlines()[0].replace("\"","").lower().split(",")

names.sort()
print(sum([calculate_score(i, name) for i, name in enumerate(names)]))
