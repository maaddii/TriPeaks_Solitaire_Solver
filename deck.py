""" Exception imports """
from exceptions import DeckError, CardNotValidError, DeckIncompleteError
# 1H, 2H, 3H, 4H, 5H, 6H, 7H, 8H, 9H, 10H, 11H, 12H, 13H, 1D, 2D, 3D, 4D, 5D, 6D, 7D, 8D, 9D, 10D, 11D, 12D, 13D, 1C, 2C, 3C, 4C, 5C, 6C, 7C, 8C, 9C, 10C, 11C, 12C, 13C, 1S, 2S, 3S, 4S, 5S, 6S, 7S, 8S, 9S, 10S, 11S, 12S, 13S
# 1h, 2h, 3h, 4h, 5h, 6h, 7h, 8h, 9h, 10h, 11h, 12h, 13h, 1d, 2d, 3d, 4d, 5d, 6d, 7d, 8d, 9d, 10d, 11d, 12d, 13d, 1c, 2c, 3c, 4c, 5c, 6c, 7c, 8c, 9c, 10c, 11c, 12c, 13c, 1s, 2s, 3s, 4s, 5s, 6s, 7s, 8s, 9s, 10s, 11s, 12s, 13s
# 1h, 2h, 3h, 4h, 5h, 6h, 7h, 8h, 9h, 10h, 11h, 12h, 13h, 1d, 2d, 3d, 4d, 5d, 6d, 7d, 8d, 9d, 10d

class Deck:
    """"
    This class is used to verify if the deck given is valid.
    """
    def __init__(self, deck):
        self.deck = deck

    def cards_verif(self):
        """
        This method is used to verify if the deck given is valid.
        """
        norm_d = ['1H', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', '11H', '12H', '13H',
                '1D', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', '11D', '12D', '13D',
                '1C', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', '11C', '12C', '13C',
                '1S', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', '11S', '12S', '13S']

        if self.deck == ['']:
            raise DeckError("The deck is empty!")

        if len(self.deck) > 52:
            raise DeckError("The number of cards is too high!")

        for card in self.deck:
            if card in norm_d:
                norm_d.remove(card)
                if not norm_d:
                    print("The deck of card is valid!")
            else:
                raise CardNotValidError(f"{card} is not valid.")

        if norm_d:
            raise DeckIncompleteError(f"Missing the following card(s): {norm_d}")
