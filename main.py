# this is the main module which holds the main game logic
# import myclasses
from myclasses import Card
from myclasses import Deck
from myclasses import Player

new_deck = Deck()
print(new_deck.all_cards[-1])

new_deck.shuffle()
print(new_deck.all_cards[-1])

player1 = Player("player1")
print(player1)
player2 = Player("player2")
print(player2)

print('Welcome to War!')
