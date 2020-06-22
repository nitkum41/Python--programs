

#RULES
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.

# The Play:

# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#

# Ignore "double" wars

import random
from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()



class Deck():
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    pass

    def __init__(self):
        self.deck=[(s,r) for s in SUITE for r in RANKS]  #list comprehension for creating deck


    def split_in_half(self):
        return (self.deck[:26],self.deck[26:])



    def shuffle(self):
        shuffle(self.deck)







class Hand():
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    pass
    def __init__(self,cards):  #cards is a list
        self.cards=cards

    def __str__(self):
        return "contains {} cards".format(len(cards))

    def add_card(self,added_cards):
        self.cards.extend(added_cards)  #added cards is a list

    def remove_card(self):
        return self.cards.pop()


class Player():
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    pass

    def __init__(self,name,hand):
        self.name=name
        self.hand=hand

    def play_card(self):
        drawn_card=self.hand.remove_card()
        print("{} has placed {}".format(self.name,drawn_card))
        print("\n")
        return drawn_card

    def remove_war_card(self):
        war_cards=[]
        if(len(self.hand.cards)<3):
            return self.hand.cards
        else:
            for i in range(3):
                war_cards.append(self.hand.cards.pop())
        return war_cards

    def still_has_cards(self):
        return len(self.hand.cards) !=0


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Use the 3 classes along with some logic to play a game of war!


#create a new deck and split it in half

deck=Deck()
deck.shuffle()
half1,half2 = deck.split_in_half()

#create players
comp=Player("computer",Hand(half1))
name=input("What is your name ??")
user=Player(name,Hand(half2))

war =0
count=0
while comp.still_has_cards() and user.still_has_cards():
    count+=1

    print("play a card")
    table_cards=[]
    p_card=user.play_card()
    c_card=comp.play_card()

    table_cards.append(p_card)
    table_cards.append(c_card)

    if p_card[1] == c_card[1] :
        print("we have war now!!")
        war+=1

        table_cards.extend(user.remove_war_card())
        table_cards.extend(comp.remove_war_card())


        p_card=user.play_card()
        c_card=comp.play_card()

        table_cards.append(p_card)
        table_cards.append(c_card)


        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add_card(table_cards)
        else:
            comp.hand.add_card(table_cards)

    else:
            if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
                user.hand.add_card(table_cards)
            else:
                comp.hand.add_card(table_cards)

print("{} no of wars happened".format(war))
print("{} no of rounds took place".format(count))
print("user {}".format(user.still_has_cards()))
print("computer {}".format(comp.still_has_cards()))
