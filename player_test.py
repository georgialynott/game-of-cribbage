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
print(player_1.hand)
print(player_2.hand)

dealer = player_1
non_dealer = player_2

while player_1.hand is not [] & player_2.hand is not []:
        running_total = 0
        while running_total < 31:
            for player in [non_dealer, dealer]
                if running_total + min([card.value for card in player.hand]) > 31:
                    return
                else:
                    card_int = int(input('{n}: choose card to play: '.format(n=player.name)))-1
                    
                    player.play(card_int)
                    running_total += 
            print(player_1.played_cards)
            player_2.play(int(input('Choose card to play: '))-1)
            print(player_2.played_cards)