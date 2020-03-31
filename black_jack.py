import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        new_string = ""
        for card in self.deck:
            new_string += str(card) + "\n"
        return new_string

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_aces(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):

    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except:
            print("Sorry, bet must be an integer!")
        else:
            if chips.bet > chips.total:
                print(f"Sorry, your bet cannot exceed {chips.total}")
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_aces()

def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("\nWould you like to Hit or Stand? Enter 'h' or 's'")
        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing")
            playing = False
        else:
            print("Sorry, please try again")
            continue
        break

def show_some(player, dealer):
    print("\n\nDealer's Hand: ")
    print("<card hidden>")
    print(dealer.cards[1])
    print("\nPlayer's Hand: ")
    for card in player.cards:
        print(card)

def show_all(player, dealer):
    print("\n\nDealer's Hand: ")
    for card in dealer.cards:
        print(card)
    print("\nPlayer's Hand: ")
    for card in player.cards:
        print(card)

def player_busts(chips):
    print("\nPlayer Busts!")
    chips.lose_bet()

def player_wins(chips):
    print("\nPlayer Wins!")
    chips.win_bet()

def dealer_busts(chips):
    print("\nDealer Busts!")
    chips.win_bet()

def dealer_wins(chips):
    print("\nDealer Wins!")
    chips.lose_bet()

def push(player, dealer):
    print("\nDealer and Player tie! It's a push.")

while True:
    print("Welcome to BlackJack!\n")

    deck = Deck()
    deck.shuffle()

    player = Hand()
    player.add_card(deck.deal())
    player.add_card(deck.deal())

    dealer = Hand()
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())

    chips = Chips()

    take_bet(chips)

    show_some(player, dealer)

    while playing:
        hit_or_stand(deck, player)

        show_some(player, dealer)

        if player.value > 21:
            player_busts(chips)
            break

    if player.value <= 21:
        while dealer.value < 17:
            hit(deck, dealer)

        show_all(player, dealer)

        if dealer.value > 21:
            dealer_busts(chips)

        elif dealer.value > player.value:
            dealer_wins(chips)

        elif dealer.value < player.value:
            player_wins(chips)
        else:
            push(player, dealer)

    print(f"\nPlayer's winnings stand at {chips.total}")

    play_again = input("\nWould you like to play again? Enter 'y' or 'n'")
    if play_again[0].lower() == 'y':
        playing = True
    else:
        print("\nThanks for playing!")
        break
