#include <iostream>
#include <map>

const int NUM_LETTERS = 26;

int findPermutation(std::string input) {
  std::map<char, int> lastSeen;
  int nSuccessfulSteps = 0;

  for (int index = 0; index < input.size(); ++index) {
    nSuccessfulSteps = std::min(nSuccessfulSteps + 1,
                                index - lastSeen[input[index] - 'A']);
    lastSeen[input[index] - 'A'] = index;
    if (nSuccessfulSteps == NUM_LETTERS) {
      return index - (NUM_LETTERS - 1);
    }
  }
  return -1;
}



int main() {
  std::cout << findPermutation("ABCDEFGHIJKLMNOPQRSTUVWXYZABC");
  return -1;
}
