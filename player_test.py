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

while player_1.hand and player_2.hand:
    running_total = 0
    player_1.go_flag = 0
    player_2.go_flag = 0
    cards_played = []
    while running_total < 31 and player_1.go_flag + player_2.go_flag < 2:
        for player in [non_dealer, dealer]:
            print('Cards played: {c}'.format(c=cards_played))
            print('Running total: {r}'.format(r=running_total))
            if running_total + min([card.value for card in player.hand]) <= 31:
                print('{p}: {h}'.format(p=player.name, h=player.hand))
                card_pos = int(input('{p} choose card to play: '.format(p=player.name))) - 1
                cards_played.append(player.play_card(card_pos))
                running_total += cards_played[-1].value
            else:
                player.go_flag = 1
            
        
