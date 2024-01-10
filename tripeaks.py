""" Deck and exceptions imports. """
from deck import Deck
from exceptions import DeckError, CardNotValidError, DeckIncompleteError


class TriPeaks(Deck):
    """
    This class allows finding the best solution for the 'TriPeaks' game.
    """
    def __init__(self, deck):
        super().__init__(deck)
        self.play_cards = []
        self.moves = []
        self.nummoves = 0

    def playable_cards(self):
        """
        A method shows playable cards
        """
        board = self.board_pile()
        for card in board:
            if card[1] == 1:
                self.play_cards.append(card)
            elif card[1] == 0:
                card[1] = 'X'
                self.waste_pile().append(card[0])

        return self.play_cards
    
    def actions(self):
        """
        A method to find the best move
        """
        playable = self.playable_cards()

        waste_cards = self.waste_pile()
        board = self.board_pile()
        board_digit = []
        for tp in board:
            di = ''.join(d for d in tp[0] if d.isdigit())
            board_digit.append(di)
        # print(f"BOARD DIGITS : {board_digit} \n")
        stock = self.stock_pile()
        playable_card_digits = []

        for n in enumerate(stock):
            waste_cards.sort()
            first_card = waste_cards[0]
            waste_num = int(''.join(n for n in first_card if n.isdigit()))
            num1 = 1 if waste_num+1 == 14 else waste_num + 1
            num2 = 13 if waste_num-1 == 0 else waste_num - 1
            print("pooopooo")
            print(f"n number : {n}")
            print(f"waste number : {waste_num}")
            print(f"NUM 1 ET NUM2 : {num1}, {num2} \n")
            # print(f"Cartes jouables : {playable}")
            for card, index in playable:
                digits = ''.join(c for c in card if c.isdigit())
                playable_card_digits.append(digits)

            # print(f"Playable card digits : {playable_card_digits} \n")

            if str(num1) in playable_card_digits:
                print("ACTION1 \n")
                waste_num = num1
                i = board_digit.index(str(waste_num))
                board[i] = 'X'
            elif str(num2) in playable_card_digits:
                print("ACTION2 \n")
                waste_num = num2
                i = board_digit.index(str(waste_num))
                board[i] = 'X'
            else:
                print("ACTION3 \n")
                first_card = stock[int(n[0])]
                waste_num = int(''.join(n for n in first_card if n.isdigit()))
            # print(f"FKING DIGITS : {digits}")
            # print()
        print(f"BOARD : {board}")
        print()


        # for n in range(0, 24):
        #     action_card = int(action_card)
        #     print(action_card)
        #     if action_card+1 == 14:
        #         num1 = 1
        #     else:
        #         num1 = action_card + 1

        #     if action_card-1 == 0:
        #         num2 = 13
        #     else:
        #         num2 = action_card - 1

        #     print(num1, num2)

            # if str(num1) in r4:
            #     action_card = num1
            #     index = r4.index(str(action_card))
            #     r4[index] = 'X'
            #     print(action_card)
            # elif str(num2) in r4:
            #     action_card = num2
            #     index = r4.index(str(action_card))
            #     r4[index] = 'X'
            #     print(action_card)
            # else:
            #     action_card = int(r[0][n])
            #     print(action_card)

            # if r4 == ['X', 'X', 'X']:
            #     print(r4)
            #     break
            # print(r4)
            # print()



if "__main__" == __name__:
    #               Welcome to TriPeaks Solver!
    #   1 - Use the following notation to input the cards:
    #       4D would be 4 of Diamonds, 12C would be Queen of Clubs,
    #       1H would be Ace of Hearts etc. (1 to 13 for the value and H, D, C, S for the suit)

    #   2 - First card to 24th represent the deck of cards.

    #   3 - 24th to 34th card represent the first row of the game,
    #       34th to 43th the second row, 43th to 49th the third row
    #       and 49th to 52th the fourth row.
    # Enter or replace the cards below:
    my_cards = [            "2C",           "11H",          "10D",
                         "4S", "10C",    "6H", "10S",    "6S", "7C",
                     "10H", "12H", "8S", "11S", "13C", "3S", "11D", "8H", "1H",
                    "7H", "5S", "5H", "2S", "9C", "7D", "2H", "9S", "13H", "9D",

                                            "12D",     "8C", "3D", "8D", "3H", "5D",
                                                       "7S", "4D", "6C", "2D", "13S",
                                                       "1C", "12S", "9H", "5C", "12C",
                                                       "4C", "4H", "1D", "11C", "6D",
                                                       "1S", "3C", "13D",
                ]
    my_deck = []
    for card in my_cards:
        my_deck.append(card.upper())
    print(f"My Deck : {my_deck} \n")

    args = Deck(my_deck)
    t = TriPeaks(my_deck)
    args.cards_verif()

    print(f"The board : {t.board_pile()} \n")
    print(f"Playable cards : {t.playable_cards()} \n")
    print(f"Waste pile : {args.waste_pile()} \n")
    print(f"Stock pile : {args.stock_pile()} \n")
    print(f"Actions : {t.actions()} \n")



# My deck of cards:
# 12D, 8C, 3D, 8D, 3H, 5D, 7S, 4D, 6C, 2D, 13S, 1C, 12S, 9H, 5C, 12C, 4C, 4H, 1D, 11C, 6D, 1S, 3C, 13D, 7H, 5S, 5H, 2S, 9C, 7D, 2H, 9S, 13H, 9D, 10H, 12H, 8S, 11S, 13C, 3S, 11D, 8H, 1H, 4S, 10C, 6H, 10S, 6S, 7C, 2C, 11H, 10D