""" blablabla """
from deck import Deck


class TriPeaks(Deck):
    """
    blablabla
    """
    def __init__(self):
        super().__init__(self)

    def tri_rangee(self):
        """
        blablabla
        """
        rangee1 = self.deck[0:10]
        rangee2 = self.deck[11:19]
        rangee3 = self.deck[20:25]
        rangee4 = self.deck[26:28]
        action_deck = self.deck[29:52]
        return [rangee1, rangee2, rangee3, rangee4, action_deck]



if "__main__" == __name__:
    my_deck = []
    cards = input("Entrez les cartes: ")
    cards = cards.upper()
    cards_list = cards.split(", ")

    for card in cards_list:
        my_deck.append(card)

    args = Deck(my_deck)
    args.cards_verif()

    tri = TriPeaks()
    print(tri.tri_rangee())

