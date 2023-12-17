from decimal import Decimal
from typing import List

from player import Player
from pot import Pot

class PokerGame:

    def __init__(self, players: List[Player]):
        self.players = players
        self.pot = Pot(players)
        self.current_round = 0
    
    # handle conditions and events for starting a new round
    
    # handle player betting actions
        
    # handle dealer
        
    # handle big blind
        
    # handle small blind
        
    # handle conditions and events for ending a round