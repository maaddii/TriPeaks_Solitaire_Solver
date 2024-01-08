
class DeckError(Exception):
    """ Error when the deck is not valid. """
    pass

class CardNotValidError(DeckError):
    """" Error when a card is not valid. """
    pass

class DeckIncompleteError(DeckError):
    """ Error when the deck is not complete. """
    pass