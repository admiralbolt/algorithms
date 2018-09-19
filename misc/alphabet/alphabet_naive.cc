#include <iostream>

const int NUM_LETTERS = 26;

int isPermutation(std::string input, int start) {
  bool occurences[NUM_LETTERS];
  for (int i = 0; i < start + NUM_LETTERS; ++i) {
    occurences[input[i] - 'A'] = true;
  }
  for (bool occurence : occurences) {
    if (!occurence) {
      return false;
    }
  }
  return true;
}

int findPermutation(std::string input) {
  for (int i = 0; i < input.size() - NUM_LETTERS + 1; ++i) {
    if (isPermutation(input, i)) {
      return i;
    }
  }
  return -1;
}


int main() {
  // std::cout << findPermutation("QQQQQQABCDEFGHIJKLMNOPQRSTUVWXYZABC");
  bool asdf[13];
  for (int i = 0; i < 13; i++) {
    std::cout << "asdf[" << i << "]: " << asdf[i] << "\n";
  }
  return -1;
}
