""" Deck and exceptions imports. """
from deck import Deck
from exceptions import DeckError, CardNotValidError, DeckIncompleteError


class TriPeaks(Deck):
    """
    This class allows finding the best solution for the 'TriPeaks' game.
    """
    def __init__(self, deck):
        super().__init__(deck)

    def tri_rangee(self):
        """
        A method for separating the deck into 5 rows.
        It allows visualizing the game.
        """
        rows = [self.deck[0:24], self.deck[24:34],
                self.deck[34:43], self.deck[43:49], self.deck[49:52]]
        res = []
        for row in rows:
            a = []
            for card in row:
                if len(card) == 3:
                    a.append(card[0:2])
                else:
                    a.append(card[0])
            res.append(a)
        return res
    
    def tri_action(self):
        """
        blablabla
        """
        r = self.tri_rangee()
        r1 = r[1]
        r2 = r[2]
        r3 = r[3]
        r4 = r[4]
        action_card = int(r[0][0])
        num1 = 0
        num2 = 0

        for n in range(0, 24):
            action_card = int(action_card)
            print(action_card)
            if action_card+1 == 14:
                num1 = 1
            else:
                num1 = action_card + 1

            if action_card-1 == 0:
                num2 = 13
            else:
                num2 = action_card - 1

            print(num1, num2)

            if str(num1) in r4:
                action_card = num1
                index = r4.index(str(action_card))
                r4[index] = 'X'
                print(action_card)
            elif str(num2) in r4:
                action_card = num2
                index = r4.index(str(action_card))
                r4[index] = 'X'
                print(action_card)
            else:
                action_card = int(r[0][n])
                print(action_card)

            if r4 == ['X', 'X', 'X']:
                print(r4)
                break
            print(r4)
            print()



if "__main__" == __name__:
    my_deck = []
    cards = input("Welcome to TriPeaks Solver! \n"
                  "1. Use the following notation to input the cards: "
                  "4D would be 4 of Diamonds, 12C would be Queen of Clubs, "
                  "1H would be Ace of Hearts etc."
                  "(1 to 13 for the value and H, D, C, S for the suit) \n"
                  "2. First card to 24th represent the deck of cards.\n"
                  "3. 24th to 34th card represent the first row of the game, "
                  "34th to 43th the second row, 43th to 49th the third row "
                  "and 49th to 52th the fourth row. \n"
                  "Enter the cards: "
                  )
    cards = cards.upper()
    cards_list = cards.split(", ")

    for card in cards_list:
        my_deck.append(card)

    args = Deck(my_deck)
    t = TriPeaks(my_deck)
    args.cards_verif()
    print(t.tri_rangee())
    print()
    t.tri_action()


# My deck of cards:
# 12D, 8C, 3D, 8D, 3H, 5D, 7S, 4D, 6C, 2D, 13S, 1C, 12S, 9H, 5C, 12C, 4C, 4H, 1D, 11C, 6D, 1S, 3C, 13D, 7H, 5S, 5H, 2S, 9C, 7D, 2H, 9S, 13H, 9D, 10H, 12H, 8S, 11S, 13C, 3S, 11D, 8H, 1H, 4S, 10C, 6H, 10S, 6S, 7C, 2C, 11H, 10D