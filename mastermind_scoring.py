import collections

def score_guess(solution, guess):
  """
  Scores a guess in the game mastermind. If a peg in the guess is the correct
  color in the correct location a red peg is awarded. If a peg in the guess
  is the correct color in the incorrect location a white peg is awarded. Returns
  the number of (red, white) pegs in the score. Example:
  Input:
    solution = [B, D, F, G]
    guess = [B, F, Q, F]
  Output: (1, 1)
  """
  num_blacks = sum([1 for i, peg in enumerate(solution) if peg == guess[i]])
  solution_colors = collections.Counter(solution)
  guess_colors = collections.Counter(guess)
  # Computing the intersection will yield the total number of pegs we should return.
  intersection = solution_colors & guess_colors
  return (num_blacks, sum(intersection.values()) - num_blacks)
