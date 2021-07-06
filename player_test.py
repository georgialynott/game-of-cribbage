from game_mechanics import Card, Deck, Player

# Create a new deck
deck = Deck()
deck.shuffle()

# Create players
player_1 = Player('G')
player_2 = Player('M')

# Deal each player a hand of 4 (as if already discarded to crib)
player_1.hand = deck.draw(4)
player_2.hand = deck.draw(4)

dealer = player_1
non_dealer = player_2

player_start = non_dealer
player_other = dealer
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
            if player.hand and running_total + min([card.value for card in player.hand]) <= 31:
                print('{p}: {h}'.format(p=player.name, h=player.hand))
                card_pos = int(input('{p} choose card to play: '.format(p=player.name))) - 1
                cards_played.append(player.play_card(card_pos))
                running_total += cards_played[-1].value
                print('Cards played: {c}'.format(c=cards_played))
                print('Running total: {r}'.format(r=running_total))
            elif player_1.go_flag + player_2.go_flag == 0:
                player.go_flag = 1
                print('{p} calls "Go"'.format(p=player.name))
                player_start_temp = player
            elif player.go_flag == 1 and player_1.go_flag + player_2.go_flag == 1:
                pass
            elif player.go_flag == 0 and running_total == 31:
                player.peg(2)
                player.go_flag = 1
                player_other_temp = player
            elif player.go_flag == 0:
                player.peg(1)
                player.go_flag = 1
                player_other_temp = player
    player_start = player_start_temp
    player_other = player_other_temp

print('Scores after The Play: {p} = {q}, {r} = {s}'.format(p=player_1.name, q=player_1.score,
                                                           r=player_2.name, s=player_2.score,))
        
