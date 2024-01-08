""" Importations des exceptions """
from exceptions import DeckError, CardNotValidError, DeckIncompleteError
# 1H, 2H, 3H, 4H, 5H, 6H, 7H, 8H, 9H, 10H, 11H, 12H, 13H, 1D, 2D, 3D, 4D, 5D, 6D, 7D, 8D, 9D, 10D, 11D, 12D, 13D, 1C, 2C, 3C, 4C, 5C, 6C, 7C, 8C, 9C, 10C, 11C, 12C, 13C, 1S, 2S, 3S, 4S, 5S, 6S, 7S, 8S, 9S, 10S, 11S, 12S, 13S
# 1h, 2h, 3h, 4h, 5h, 6h, 7h, 8h, 9h, 10h, 11h, 12h, 13h, 1d, 2d, 3d, 4d, 5d, 6d, 7d, 8d, 9d, 10d, 11d, 12d, 13d, 1c, 2c, 3c, 4c, 5c, 6c, 7c, 8c, 9c, 10c, 11c, 12c, 13c, 1s, 2s, 3s, 4s, 5s, 6s, 7s, 8s, 9s, 10s, 11s, 12s, 13s
# 1h, 2h, 3h, 4h, 5h, 6h, 7h, 8h, 9h, 10h, 11h, 12h, 13h, 1d, 2d, 3d, 4d, 5d, 6d, 7d, 8d, 9d, 10d

class Deck:
    """"
    blablabla
    """
    def __init__(self, deck):
        self.deck = deck

    def cards_verif(self):
        """
        blablabla
        """
        normal_deck = ['1H', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', '11H', '12H', '13H',
                '1D', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', '11D', '12D', '13D',
                '1C', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', '11C', '12C', '13C',
                '1S', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', '11S', '12S', '13S']
        if len(self.deck) > 52:
            raise DeckError("Le deck est trop grand.")

        for card in self.deck:
            if card in normal_deck:
                normal_deck.remove(card)
                if not normal_deck:
                    print("Le deck est complet!")
            else:
                raise CardNotValidError(f"{card} n'est pas une carte valide.")
        
        if normal_deck:
                raise DeckIncompleteError(f"Il manque la / les carte(s)"
                                          f"suivante(s): {normal_deck}")

# if "__main__" == __name__:
#     my_deck = []
#     cards = input("Entrez les cartes: ")
#     cards = cards.upper()
#     cards_list = cards.split(", ")

#     for card in cards_list:
#         my_deck.append(card)

#     args = Deck(my_deck)
#     args.card_verif()
#     tri = TriPeaks()
