# this module contains all the classes defined
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, \
          'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    # class for a deck where all objects of each card is held in a list
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # create the card object for each card
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        # method to shuffle the cards within the deck object list
        random.shuffle(self.all_cards)

    def deal_one(self):
        # method to remove one card at the bottom and return it
        # pop by default removes the last item in the list
        # assume 0 is top and -1 the bottom
        return self.all_cards.pop()

class Player:
    def __init__(self,name):
        self.name = name
        # a new player has no cards
        self.all_cards = []

    def remove_one(self):
        # remove one card from the top that is at 0
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        # add cards on the table to the player after he wins a round or war
        print(type(new_cards))
        if type(new_cards) == type([]):
            # if new cards is a list of card objects (multiple cards)
            self.all_cards.extend(new_cards)
            print('extended')
        else:
            # if new cards is a single card object
            self.all_cards.append(new_cards)
            print('appended')

    def __str__(self):
        # make the class printable
        return f'Player {self.name} has {len(self.all_cards)} cards.'
