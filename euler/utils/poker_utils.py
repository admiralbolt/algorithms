import collections
import operator

from enum import Enum
from functools import total_ordering

class Suit(Enum):
  CLUBS = 1
  SPADES = 2
  DIAMONDS = 3
  HEARTS = 4

@total_ordering
class HandValue(Enum):
  HOT_GARBAGE = 1
  ONE_PAIR = 2
  TWO_PAIR = 3
  THREE_OF_A_KIND = 4
  STRAIGHT = 5
  FLUSH = 6
  FULL_HOUSE = 7
  FOUR_OF_A_KIND = 8
  STRAIGHT_FLUSH = 9

  def __eq__(self, other):
    return self.value == other.value

  def __lt__(self, other):
    return self.value < other.value


# Maps characters to their correct values i.e. Ace is 14, King is 13 e.t.c
CARD_MAP = {
  "A": 14,
  "K": 13,
  "Q": 12,
  "J": 11,
  "T": 10
}

# Maps characters to their correct suit.
SUIT_MAP = {
  "C": Suit.CLUBS,
  "S": Suit.SPADES,
  "D": Suit.DIAMONDS,
  "H": Suit.HEARTS
}

@total_ordering
class PokerCard(object):
  """A representation of a poker card, keeps track of value and suit.

  Expects a two character string as input like:
  AD (Ace of diamonds), 8C (8 of clubs) e.t.c
  """

  def __init__(self, card_string):
    self.value = CARD_MAP.get(card_string[0]) or int(card_string[0])
    self.suit = SUIT_MAP[card_string[1]]

  def __eq__(self, other):
    return self.value == other.value

  def __lt__(self, other):
    return self.value < other.value


@total_ordering
class PokerHand(object):
  """Represents an entire hand of 5 cards."""

  cards = []

  def __init__(self, cards):
    self.cards = cards

  def __repr__(self):
    return str(self.get_total_hand_value())

  def get_total_hand_value(self):
    """Returns a tuple (x, y, z) corresponding to total hand value.

    x: The actual type of hand (two_pair, full_house, e.t.c).
    y: A tuple of individual card values in the hand.
    z: A tuple of high card values from cards "not" in the hand.

    A few examples:
      Full house AAA88 : (HandValue.FULL_HOUSE, (13, 8), ())
      Two Pair 334410: (HandValue.TWO_PAIR, (4, 3), 10)
      Flush (37JQA): (HandValue.FLUSH, (14, 12, 11, 7, 3), ())
      Nuthin (3579J): (HandValue.HOT_GARBAGE, (), (11, 9, 7, 5, 3))
    """
    is_repeated_value_hand, rep = self._get_repeated_value_hand()
    if is_repeated_value_hand:
      return rep

    # Left to check is straight, flush, and straight flush
    # We can use the fact that there are no repeated values at this point and
    # save some effort.
    max_card = max([card.value for card in self.cards])
    min_card = min([card.value for card in self.cards])
    is_straight = max_card - min_card == 4
    is_flush = all(self.cards[0] == card for card in self.cards)
    if is_straight and is_flush:
      return HandValue.STRAIGHT_FLUSH, (max_card,), ()
    elif is_straight:
      return HandValue.STRAIGHT, (max_card,), ()
    elif is_flush:
      return HandValue.FLUSH, tuple(sorted([card.value for card in self.cards], reverse=True)), ()

    return (HandValue.HOT_GARBAGE, (), tuple(sorted([card.value for card in self.cards], reverse=True)))

  def _get_repeated_value_hand(self):
    """Returns the correct representation for repeated value hands.

    Specifically: two, three, and four of a kind, two pair, and full house.
    """
    c = collections.Counter([card.value for card in self.cards])
    if len(c) == 5:
      return False, ()
    most_common = sorted(c.most_common(4), key=lambda x: (x[1], x[0]), reverse=True)
    # It's a full house or four of a kind.
    if len(most_common) == 2:
      if most_common[1][1] == 2:
        return True, (HandValue.FULL_HOUSE, (most_common[0][0], most_common[1][0]), ())
      return True, (HandValue.FOUR_OF_A_KIND, (most_common[0][0]), (most_common[1][0],))

    # It's a three of a kind or two pair.
    if len(most_common) == 3:
      if most_common[1][1] == 1:
        return True, (HandValue.THREE_OF_A_KIND, (most_common[0][0]), (most_common[1][0], most_common[2][0]))
      return True, (HandValue.TWO_PAIR, (most_common[0][0], most_common[1][0]), (most_common[2][0],))

    # It is but a single pear.
    return True, (HandValue.ONE_PAIR, (most_common[0][0],), (most_common[1][0], most_common[2][0], most_common[3][0]))


  def __eq__(self, other):
    return self.get_total_hand_value() == other.get_total_hand_value()

  def __lt__(self, other):
    self_value = self.get_total_hand_value()
    other_value = other.get_total_hand_value()
    if self_value[0] != other_value[0]:
      return self_value[0] < other_value[0]
    for x, y in zip(self_value[1], other_value[1]):
      if x != y:
        return x < y
    for x, y in zip(self_value[2], other_value[2]):
      if x != y:
        return x < y
    return False
