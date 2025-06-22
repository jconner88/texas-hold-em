from game_pkg.deck import Deck, Card, Player, Opponent
import webbrowser

while True:
    rules = input("Do you know how to play Texas Holdem?\nYes or No: ").casefold()
    if rules == "yes" or rules == "y":
        break
    elif rules == "no" or rules =="n":
        show_rules = input("Do you want to read the rules?\nOpens in Web Browser.\nYes or No: ").casefold()
        if show_rules == "yes" or show_rules == "y":
            webbrowser.open("https://www.wsop.com/poker-games/texas-holdem/rules/")
        elif show_rules == "":
            print("PLease enter yes or no.\n")
        else: 
            break
    else:
        print("Please enter Yes or No.\n")

while True:
    deck = Deck()
    deck.shuffle()
    pot = 0
    player_pool = 1000
    blind1 = 50
    player_pool -= blind1
    pot = pot + blind1 + blind1
    table_cards = []
    print("All players put in $" + str(blind1), "into the pot.")
    print("\nThe pot is $" + str(pot), "\nYour pool is $" + str(player_pool))

    def play_again():
        again = input("\nDo you want to play another hand? \nYes or No: ").casefold()
        if again == "no" or again == "n":
            print ("Thanks for playing.\nYou won $" + str(player_pool))
            quit()
        elif again == "yes" or again == "y":
            return

    def bets():
        while True:
            global player_pool, opponent_pool, blind1, pot
            bet = (input("\nDo you want to Call, Raise, or Fold: ")).casefold()
            if bet == "fold":
                print("You folded.\nYour pool : $" + str(player_pool))
                play_again()
                break
            elif bet == "call":
                player_pool -= blind1
                pot += blind1
                print("Your pool: $" + str(player_pool),"\nPot: $" + str(pot))
                return
            elif bet == "raise":
                amnt = int(input("Enter an amount to bet: $"))
                try:
                    if amnt > player_pool:
                        print("You don't have enough for that bet.\nEnter a smaller bet")
                    elif amnt == player_pool:
                        all_in = input("Are you sure you want to go all in? Yes or NO: ").casefold()
                        if all_in == "yes":
                            player_pool -= amnt
                            pot += amnt
                            print("Pot: $" + str(pot),"\nYour pool: $" + str(player_pool))
                            return
                    elif amnt >= 1 and amnt < player_pool:
                        player_pool -= amnt
                        pot = pot+ amnt
                        print("Pot: $" + str(pot),"\nYour pool: $" + str(player_pool))
                        return
                except ValueError:
                    print("Bet must be a number.")
            else: 
                print("You must Call, Raise or Fold.")

# Players hole cards. Visible to player
    print("\nYou were dealt: ")
    for i in range(2):
        # deck = Deck()
        # deck.shuffle()
        player1 = Player("John")
        player1.draw(deck)
        player1.show_hand()

# Opponent hole cards. Hidden from player
    print("\nYour opponent was dealt 2 cards: ")
    for i in range(2):
        # deck = Deck()
        # deck.shuffle()
        player2 = Opponent("Opponent")
        player2.draw(deck)
        player2.show_hand()
    
# Betting Round 1
    bets()
  
# Flop CARDS
    print("\nFlop Cards ")
    for i in range(3):
        card = deck.deal_card()
        table_cards.append(card)
        card.show()

# Betting Round 2
    bets()

# Turn Card
    print("\nTurn Card:")
    card = deck.deal_card()
    table_cards.append(card)
    card.show()

# Betting Round 3
    bets()

# River Card
    print("\nRiver Card:")
    card = deck.deal_card()
    table_cards.append(card)
    card.show()

# Final Bet
    bets()

# TODO Implement Hand Evaluation
    """"
    def evaluation(player_hand, table_cards):
        overall_hand = player_hand + table_cards
        counts = {}
        suits = {}
        vals = set
        for card in overall_hand:
            card_value = card.value
            if card_value in counts:
                counts[card_value] += 1
            else:
                counts[card.suits] = 1
            if card.suit in suits:
                suits[card.suit] += 1
            else:
                suits[card.suit] = 1

        sorted_counts = sorted(counts.items(), key = lambda item:(item[1], item[0]), reverse = True)
        sorted_suits = sorted(suits.items(), key = lambda item:(item[1], item[0]), reverse = True)
        straight = [sorted(list(vals))[0]]
        last_val = sorted(list(vals))[0]
        is_straight = False
        for val in sorted(list(vals)):
            if val - last_val == 1:
                straight.append(val)
            else:
                straight = [val]
            lastval = val
            if len(straight) == 5:
                is_straight = True
                break
            is_flush = False
            if sorted_suits[0][1] == 5:
                is_flush = True
            if is_straight:
                if is_flush:
                    return "Straight Flush!"
                """



# Option to play another hand
    if player_pool <= 0:
            print("Game Over")
            quit()
    elif player_pool > 0:
        play_again()