import os
import sys

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from utils import poker_utils

player1_wins = 0
with open("p54_poker.txt", "r") as rh:
  for line in rh.readlines():
    card_strings = line.strip().split()
    player1_hand = poker_utils.PokerHand(
      [poker_utils.PokerCard(card_string) for card_string in card_strings[:5]]
    )
    player2_hand = poker_utils.PokerHand(
      [poker_utils.PokerCard(card_string) for card_string in card_strings[5:]]
    )
    if player1_hand == player2_hand:
      print(player1_hand)
      print(player2_hand)
      print("HMMM")
    if player1_hand > player2_hand:
      player1_wins += 1

print(player1_wins)
