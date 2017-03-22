# -*- coding: utf-8 -*-
"""
Random functions for Data-Science-Curriculum
"""
import random 

class CardDeck:
    def __init__(self):
        cards = 4 * (range(2, 11) + ['J', 'Q', 'K', 'A'])
        suits = 13*['-Diamonds'] + 13*['-Hearts'] + 13*['-Spades'] + 13*['-Clubs']
        self.deck =  [str(c)+s for c, s in zip(cards, suits)]

    def draw(self):
        return self.deck.pop()
        
    def shuffle(self):
        random.shuffle(self.deck)
        
    def reset(self):
        self.__init__()
        
    def deal_poker_hands(self, player_ct):
        hands = [[] for p in range(player_ct)]
        for c in range(1, 6):
            for h in hands:
                h.append(self.draw())
        return hands