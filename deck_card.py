from random import shuffle
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
           #return f"{} of {}".format(self.value, self.suit)
            return f"{self.value} of {self.suit}"

# instances of deck
# each instance of card should have all the 52 possible instances of card
# count, returns a count of how many card are left
# __repr__, display how many are left in the deck
# _deal- accepts number and remove at most many cards from the deck.:

# shuffle - shuffles a full deck
# deal card, uses the deal method to deal a single card from the deck
# deal_hand accepts a number and uses the deal method to deal a list of cards

class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "clubs", "spades"]
        values = ['A', ' 2', '3', '4', ' 5', '6', '7', ' 8', '9', '10',' J ',' Q', 'K']
        self.cards = [Card(value, suit) for suit in suits for value in values]
        # print(self.cards)
        # for suit in suits:
        #     for value in values:
        #          print(Card(value, suits))

    def __repr__(self):
        return f"Deck of {self.count()} cards"
    def count(self):
        return len(self.cards)
    def _deal(self , num):
        count = self.count()
        actual = min([count, num])
        # print(f"Going to remove {actual} cards")
        if count == 0:
            raise ValueError("All cards has been dealt with")
        cards = self.cards[-actual:]
        self.cards= self.cards[:-actual]
        return cards

    def deal_card(self):
            return self._deal(1)[0]

    def deal_hand(self,hand_size):
        return self._deal(hand_size)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks are shuffled")
        shuffle(self.cards)
        return self


d = Deck()
d.shuffle()
card = d.deal_card()
print(card)
hand = d.deal_hand(2)
print(hand)
card2 = d.deal_card()
print(card2)
