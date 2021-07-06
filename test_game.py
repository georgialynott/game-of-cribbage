# Testing the `game_mechanics` module 

# IMPORTS
from game_mechanics import Card, Deck, Player

# Create a new deck
deck = Deck()
deck.shuffle()

# Create players with user-input names
player_1 = Player(input('Player 1 enter name: '))
player_2 = Player(input('Player 2 enter name: '))
print(player_1)
print(player_2)

# Create counter for rounds
round_number = 0

# Begin loop over rounds until either player reaches score of 121
while player_1.score & player_2.score < 121:

    # Start new round and print current scores
    round_number += 1
    print('Round {r}\n{p1}: {s1}, {p2}: {s2}'.format(r = round_number, 
                                                       p1 = player_1.name, 
                                                       s1 = player_1.score, 
                                                       p2 = player_2.name, 
                                                       s2 = player_2.score))

    # Select dealer based on round
    dealer = [player_1, player_2][round_number%2]
    non_dealer = [player_1, player_2][(round_number+1)%2]

    # Deal each player a hand of 6
    player_1.hand = deck.draw(6)
    player_2.hand = deck.draw(6)
    print(player_1.name, player_1.hand)
    print(player_2.name, player_2.hand)

    # Each player discards two cards to the crib
    crib = []
    # Get discarded cards from players
    print(player_1.name)
    player_1_discard = [int(input('Choose 1st card to discard to crib: '))-1,
                    int(input('Choose 2nd card to discard to crib: '))-1]
    print(player_2.name)
    player_2_discard = [int(input('Choose 1st card to discard to crib: '))-1,
                    int(input('Choose 2nd card to discard to crib: '))-1]
    # Add discarded cards to crib
    crib.extend(player_1.discard(player_1_discard))
    crib.extend(player_2.discard(player_2_discard))
    print('Crib: ', crib)
    # Print updated player hands
    print(player_1.name, player_1.hand)
    print(player_2.name, player_2.hand)

    # Turn over starter card
    starter_card = deck.draw(1)[0]
    print('Starter ', starter_card)
    # Check if starter card is a Jack
    if starter_card.rank == 'J':
        dealer.peg(2) # dealer pegs 2 points for "his heels"
    
# THE PLAY
# --------
# Starting with the non-dealer, players take turns placing cards, 
# beginning with the non-dealer, face-up and adding their scores
# up to a cumlative value of 31. If a player cannot play a card
# without going over 31, they say "Go". The other player must then
# place any remaining cards they can from their hand, without
# exceeding 31. Play then restarts with the player who called 
# "Go" playing first.
#
# SCORING IN THE PLAY
# -------------------
# It is possible to score points for making fifteen, pairs, runs etc. as in The Show;
# Cards need not be in sequence, provided that there are no "interrupting" cards
# between. Consider the following examples:
# Example 1
# Players:    M   G   M   G
# Cards:      2   4   5   3       G pegs 4 for the run "2 3 4 5"
# Example 2
# Players:    M   G   M   G
# Cards:      2   3   J   4       G does *not* peg 3 for the run "2 3 4" 
#                                 because of the intervening card "J"
#
# A player can peg points for extending a run, or getting 3/4 of a kind, even if the
# othe player pegged points previously for part of the run or a pair, say
# Example 3
# Players:    M   G   M   G
# Cards:      5   7   6   4       M pegs 3 upon playing "6" for the run "5 6 7"
#                                 G then pegs 4 upon playing "4" for the run "4 5 6 7"
# Example 4
# Players:    M   G   M
# Cards:      Q   Q   Q           G pegs 2 for placing the second "Q" in the pair "Q Q"
#                                 M then pegs 6 upon playing the third "Q" for a pair royal "Q Q Q"

# Non-dealer begins The Play
player_start = non_dealer
player_other = dealer
print(player_1.name, player_1.score, player_2.name, player_2.score)

# Begin loop for The Play
while player_1.hand and player_2.hand:
    running_total = 0
    player_1.go_flag = 0
    player_2.go_flag = 0
    cards_played = []
    print('Cards played: {c}'.format(c=cards_played))
    print('Running total: {r}'.format(r=running_total))
    print(player_start.name, player_other.name)
    while player_1.go_flag + player_2.go_flag < 2:
        for player in [player_start, player_other]:
            if (player.hand and 
                running_total + min([card.value for card in player.hand]) <= 31):
                # Show player's hand and get them to choose a card to play
                print('{p}\'s hand: {h}'.format(p=player.name, h=player.hand))
                player_input = input('{p} choose card to play (1-{l}): '.format(p=player.name, l=len(player.hand)))
                # Check card selection is valid
                while (not player_input.isdigit() or
                        int(player_input) < 1 or 
                        int(player_input) > len(player.hand) or 
                        player.hand[int(player_input)-1].value + running_total > 31):
                    print('Error: invalid card selected')
                    player_input = input('{p} choose card to play (1-{l}): '.format(p=player.name, l=len(player.hand)))
                # Remove card from player hand and add to played cards and running total
                card_pos = int(player_input) - 1
                cards_played.append(player.play_card(card_pos))
                running_total += cards_played[-1].value
                print('Cards played: {c}'.format(c=cards_played))
                print('Running total: {r}'.format(r=running_total))
                # Allow player to peg if points scored
                if len(cards_played) > 1:
                    peg_input = int(input('{p} enter points to be pegged for fifteen, pairs, runs etc. if any: '.format(p=player.name)))
                    player.peg(peg_input)
                # To add in future (possibly) - automatic scoring for of runs, pairs etc.
            # Check if player must call "Go" or end of round reached
            elif player_1.go_flag + player_2.go_flag == 0:
                player.go_flag = 1
                print('{p} calls "Go"'.format(p=player.name))
                player_start_temp = player
            elif player.go_flag == 1 and player_1.go_flag + player_2.go_flag == 1:
                pass
            # Player pegs 2 points for reaching exactly 31, or 1 point for playing
            # the last card after "Go" has been called
            elif player.go_flag == 0 and running_total == 31:
                player.peg(2)
                print('{p} pegs 2 for reaching 31'.format(p=player.name))
                player.go_flag = 1
                player_other_temp = player
            elif player.go_flag == 0:
                player.peg(1)
                print('{p} pegs 1 for playing last card'.format(p=player.name))
                player.go_flag = 1
                player_other_temp = player
    # The player who called "Go" goes first in the next round
    player_start = player_start_temp
    player_other = player_other_temp

print('Scores after The Play: {p} = {q}, {r} = {s}'.format(p=player_1.name, q=player_1.score,
                                                           r=player_2.name, s=player_2.score))