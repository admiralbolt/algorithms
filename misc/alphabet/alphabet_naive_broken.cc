const int NUM_LETTERS = 26;

int findPermutation(std::string input) {
  for (int i = 0; i < input.size() - (NUM_LETTERS - 1); ++i) {
    if (isPermutation(input, i)) {
      return i;
    }
  }
  return -1;
}

int IsPermutation(std::string input, int start) {
  bool all_true = false;
  bool[] occurences(NUM_LETTERS);
  for (int index = 0; index < start + NUM_LETTERS; ++i) {
    occurences[input[index] - 'A'] = true;
  }
  for (bool occurence : occurences) {
    all_true = all_true && occurence;
  }
  return all_true;
}
