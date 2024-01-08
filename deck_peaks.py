# deck = ['1H', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', '11H', '12H', '13H',
#         '1D', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', '11D', '12D', '13D',
#         '1C', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', '11C', '12C', '13C',
#         '1S', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', '11S', '12S', '13S'] 
# # 2 to 10, J for Jack, Q for Queen, K for King, A for Ace
# # H for Hearts, D for Diamonds, C for Clubs, S for Spades

# card_number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
# card_color = ['H', 'D', 'C', 'S']
# my_deck = []
# for i in card_color:
#     for j in card_number:
#         my_deck.append(j + i)

# print(my_deck) # Donne deck
# print(my_deck[0]) # Donne 1H
# print(my_deck[0][0]) # Donne 1
# for card in my_deck:
#     print(card[0]) # Donne 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
#     print(card.__class__)
#     int_card = int(card[0])
#     print(int_card.__class__)

# # Faire un truc du genre:
# if "carte" in "rangée 1 n'a pas de correspondane (numéro), tourner carte deck action"

from action import *

# class Deck:
#     def __init__(self, cards):
#         super().__init__(self, cards)
#         self.cards = cards
#         self.deck = ['1H', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', '11H', '12H', '13H',
#                      '1D', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', '11D', '12D', '13D',
#                      '1C', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', '11C', '12C', '13C',
#                      '1S', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', '11S', '12S', '13S']

#     def deck_builder(self):
#         pass
#         # for card in self

#     def card_verification(self):
#         for card in self.deck:
#             if card not in self.cards:
#                 self.my_deck.append(card)
#         return self.my_deck


# Access the cards attribute of the Deck instance
print()