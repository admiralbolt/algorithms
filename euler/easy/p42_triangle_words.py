def gaussian_sum(x):
  """Returns the gaussian sum of x."""
  return x * (x + 1) / 2

word_map = {
  "a": 1,
  "b": 2,
  "c": 3,
  "d": 4,
  "e": 5,
  "f": 6,
  "g": 7,
  "h": 8,
  "i": 9,
  "j": 10,
  "k": 11,
  "l": 12,
  "m": 13,
  "n": 14,
  "o": 15,
  "p": 16,
  "q": 17,
  "r": 18,
  "s": 19,
  "t": 20,
  "u": 21,
  "v": 22,
  "w": 23,
  "x": 24,
  "y": 25,
  "z": 26
}

def word_num(word):
  return sum([word_map[letter] for letter in word])


gaussian_nums = set()
for i in range(100):
  gaussian_nums.add(gaussian_sum(i))

with open("p42_words.txt", "r") as rh:
  line = rh.readlines()[0]
  words = line.replace("\"", "").lower().split(",")

num_triangles = 0
for word in words:
  if word_num(word) in gaussian_nums:
    num_triangles += 1

print(num_triangles)
