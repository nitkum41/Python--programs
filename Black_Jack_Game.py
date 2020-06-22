import random



class Card:  #card class which holds suit and rank of a card
    value=0
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"



class Deck:  #deck class to deal,shuffle deck of cards

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                                                              #STORING AS CARD OBJECTS

    def __str__(self):
        st=''
        for deck in self.deck:          #using str to directly print an object
            st+= '\n ' + Card.__str__() #IT IS A CARD OBJECT SO PRINTS CARD CLASS STRING METHOD TO CONCATENATE
        return "The Cards Are :"+st

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return_card=self.deck.pop()
        return return_card

#test_deck = Deck()
#print(test_deck)


class Hand:  #hand class to show cards in each hand for each player
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if self.aces=='Aces':
            self.aces+=1

    def adjust_for_ace(self):
        if self.value > 21 and self.aces:
            self.value-=10
            self.aces-=1
'''
test_deck = Deck()
test_deck.shuffle()
test_player = Hand()
test_player.add_card(test_deck.deal())
test_player.add_card(test_deck.deal())
print(test_player.value)

for card in test_player.cards:
    print(card)

'''


class Chips:  #chip class to check the bets placed by each player and also check for win and loss

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total+=self.bet

    def lose_bet(self):
        self.total-=self.bet



#SOME FUNCTIONS TO ASSIST THE GAME logic

def take_bet(chips):     #chip object to place a bet

    while True:

        try:
            chips.bet=int(input('\nEnter your bet value\n'))
        except ValueError:
            print('\nEnter an integer value\n')

        else:
            if chips.bet > chips.total:
                print('\nbet value cannt be greater than :',chips.total)
            else:
                break

def hit(deck,hand):   #it deals a card and then adjust for ace 
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop


    while playing:
        choose=input('\n what you wanna do ? hit or stand \n')

        if choose[0].lower() =='h':
            hit(deck,hand)
        elif choose[0].lower() == 's':
            print('\n Player stands . Dealer is playing')
            playing=False
        else:
            print('\nPlease continue')
            continue
        break

def show_some(player,dealer):    #show all hand of player and dealers first hand is hidden after each hand

    print('\nPlayer cards:')
    for card in player.cards:
        print(card)

    print('\nDealer cards:')
    print('<first one is hidden>')
    print(dealer.cards[1])



def show_all(player,dealer):    #show all hand of player and dealers hands also at the end of hand

    print('\nPlayer cards:')
    for card in player.cards:
        print(card)
    print('value of card is:',player.value)

    print('\nDealer cards:')
    for card in dealer.cards:
        print(card)
    print('value of card is:',dealer.value)


def player_busts(player,dealer,chips):
    print('\nPlayer busts:')
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('\nPlayer wins:')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('\nDealer busts:')
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print('\nDealer wins:')
    chips.lose_bet()

def push(player,dealer):
    print('Nobody wins its a tie')


#using tuples for suits
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
#using tuples for ranks
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
#using dictionary to link ranks with its actual values
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


playing = True

#game logic
while True:
    # Print an opening statement
    print('\nWelcome to a game of black jack : \n')

    # Create & shuffle the deck, deal two cards to each player
    deck=Deck()
    deck.shuffle()

    player_hand=Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand=Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips
    player_chip=Chips()

    # Prompt the Player for their bet
    take_bet(player_chip)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)


    while playing:  # recall this variable from our hit_or_stand function
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chip)
            break


    if player_hand.value <= 21:     # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        while dealer_hand.value <= 17:
            hit(deck,dealer_hand)
        show_all(player_hand,dealer_hand)    # Show all cards
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chip)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chip)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chip)
        else:
            push(player_hand,dealer_hand)


    print('\nPlayer winnings stand at',player_chip.total)   # Inform Player of their chips total

    newgame = input('\nDo you want to play another hand: Y or N ? \n')                      # Ask to play again

    if newgame[0].lower() == 'y':
          playing=True
          continue
    else:
          print('\nThanks for playing')
          break
