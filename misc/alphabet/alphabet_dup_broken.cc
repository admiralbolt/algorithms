const int NUM_LETTERS = 26;

int FindPermutation(std::string input) {
  int lastSeen[NUM_LETTERS];
  int nSuccessfulSteps = 0;

  for (int index = 0; index < input.size(); ++index) {
    nSuccessfulSteps = std::min(nSuccessfulSteps + 1,
                                index - lastSeen[input[index]]);
    lastSeen[input[index]] = index;
    if (nSuccessfulSteps == NUM_LETTERS) {
      return index - (NUM_LETTERS - 1);
    }
  }
  return -1;
}
