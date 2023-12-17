from decimal import Decimal
from typing import List

from player import Player

class Pot:

    def __init__(self, players: List[Player]):
        self.players = players
        self.current_bet = Decimal("0.00")

    # handle updating of the pot
        
    # handle distribution of winnings

        # handle side pot