import random

# starting deck
full_deck = []

# card spaces
player_1_deck = []
player_1_pile = []
player_1_field = []
player_2_deck = []
player_2_pile =[]
player_2_field = []
player_1_deck_size = 0
player_2_deck_size = 0
player_1_wagers = []
player_2_wagers = []

class Card:
	def __init__(self, num_value, suit, name):
		self.num_value = num_value
		self.suit = suit
		self.name = name

def print_deck_size():
	print(f"Deck Size: {player_1_deck_size} cards.")
	print(f"Opponent Deck Size: {player_2_deck_size} cards.")
	print("")

def game_loop():
	update_deck_size()
	while player_1_deck_size > 0 and player_2_deck_size > 0:
		update_deck_size()
		print_deck_size()
		print("Play hand.")
		hand()
		
	update_deck_size()
	if player_1_deck_size < 1:
		print("You lose...")
	elif player_2_deck_size < 1:
		print("You win!")
	else:
		print("Error: Game win/lose conditions are broken.")

def hand():
	global player_1_field, player_2_field, player_1_deck, player_1_pile, player_2_deck, player_2_pile

	#shuffle as required
	if len(player_1_deck) == 0 and len(player_1_pile) > 0:
		player_1_deck = shuffle(player_1_pile)
	player_1_field.append(player_1_deck[0])
	player_1_deck.remove(player_1_deck[0])
	print(f"You play: {player_1_field[-1].name}")
	
	# shuffle as required
	if len(player_2_deck) == 0 and len(player_2_pile) > 0:
		player_2_deck = shuffle(player_2_pile)
	player_2_field.append(player_2_deck[0])
	player_2_deck.remove(player_2_deck[0])
	print(f"Your Opponent plays: {player_2_field[-1].name}")
	print("")
	
	# fight!
	combat()

def combat ():
	if player_1_field[-1].num_value > player_2_field[-1].num_value:
		if len(player_1_field) == 1: 
			player_1_pile.append(player_1_field[0])
			player_1_pile.append(player_2_field[0])			
			print(f"You win the hand! And acquire your opponent's {player_2_field[0].name}.")
			clear_fields()
		else:
			for card in player_1_field:
				player_1_pile.append(card)
			for card in player_2_field:
				player_1_pile.append(card)			
			print("You win the war!! And acquire all wagered cards!")
			display_wagers()
			clear_fields()

	elif player_1_field[-1].num_value < player_2_field[-1].num_value:
		if len(player_1_field) == 1: 
			player_2_pile.append(player_1_field[0])
			player_2_pile.append(player_2_field[0])
			print(f"You lose the hand, relinquishing your {player_1_field[0].name}...")
			clear_fields()
		else:
			for card in player_1_field:
				player_2_pile.append(card)
			for card in player_2_field:
				player_2_pile.append(card)			
			print("You lose the war!! And relinquish all wagered cards!")
			display_wagers()
			clear_fields()

	elif player_1_field[-1].num_value == player_2_field[-1].num_value:
		# this needs to be a dynamic function
		print(f"It's time to go to war!")
		print("")
		war()		
	else:
		print("Error: Card values cannot be compared.")

def war():
	global player_1_deck, player_2_deck

	update_deck_size()
	if player_1_deck_size < 4 and player_2_deck_size < 4:
		if player_1_deck_size > player_2_deck_size:
			print("Neither player has enough cards to go to war, but your opponent ran out of cards first, so you win by default!")
			lose()
		else:
			print("Neither player has enough cards to go to war, but you ran out of cards first, so you lost by default!")
			win()
	elif player_1_deck_size > 4 and player_2_deck_size < 4:
		print("Your opponent doesn't have enough cards to go to war, so you win by default!")
		win()
	elif player_1_deck_size < 4 and player_2_deck_size > 4:
		print("You don't have enough cards to go to war, so you lose by default!")
		lose()
	
	# war happens
	else:
		#shuffle as required
		if len(player_1_deck) == 0 and len(player_1_pile) > 0:
			player_1_deck = shuffle(player_1_pile)
		for i in range(4):
			player_1_field.append(player_1_deck[i])
		for i in range (3):
			player_1_wagers.append(player_1_deck[i].name)
		for i in range(4):
			player_1_deck.remove(player_1_field[-1-i])
		print("You wager three face-down cards and flip the fourth one, revealing...")
		print(f'{player_1_field[-1].name}!')

		# shuffle as required
		if len(player_2_deck) == 0 and len(player_2_pile) > 0:
			player_2_deck = shuffle(player_2_pile)
		for i in range(4):
			player_2_field.append(player_2_deck[i])
		for i in range (3):
			player_2_wagers.append(player_2_deck[i].name)
		for i in range(4):
			player_2_deck.remove(player_2_field[-1-i])
		print("Your opponent does the same, revealing...")
		print(f'{player_2_field[-1].name}!')

		combat()


def win():
	global player_2_deck, player_2_field, player_2_pile

	player_2_deck, player_2_field, player_2_pile = [], [], []

def lose():
	global player_1_deck, player_1_field, player_1_pile

	player_1_deck, player_1_field, player_1_pile = [], [], []

# returns False if a dupllicate card is found in a deck
def check_duplicates(deck):
	seen = []
	for card in deck:
		if card in seen:
			return False
		seen.append(card)
	return True

def update_deck_size():
	global player_1_deck_size, player_2_deck_size
	
	player_1_deck_size = len(player_1_deck) + len(player_1_pile)
	player_2_deck_size = len(player_2_deck) + len(player_2_pile)

def clear_fields():
	global player_1_field, player_2_field

	player_1_field, player_2_field = [], []

def startup():
	global player_2_deck
	
	for card in playing_cards.values():
		full_deck.append(card)

	if len(full_deck) == 52 and check_duplicates(full_deck):
		pass
	else:
		print("Error: The 52 card playing deck was not intialized properly.")
	
	# split the full_deck in half randomly
	while len(full_deck) > 26:
		card_index = random.randint(0,len(full_deck)-1)
		player_1_deck.append(full_deck[card_index])
		full_deck.remove(full_deck[card_index])
	
	# assign remaining cards to the other deck
	player_2_deck = full_deck
		
# call by saying for example: player_1_deck = shuffle(player_1_deck)
def shuffle(pile):
	shuffled_deck = []
	for card in pile:
		card_index = random.randint(0, len(pile)-1)
		shuffled_deck.append(pile[card_index])
		pile.remove(pile[card_index])
	return shuffled_deck





def display_wagers():
	print(f"You wagered: {player_1_wagers}")
	print(f"Your opponent wagered: {player_2_wagers}")
	clear_wagers()

def clear_wagers():
	global player_1_wagers, player_2_wagers

	player_1_wagers, player_2_wagers = [], []

# Intialize a full deck playing cards
playing_cards ={
    'two_spades': Card(2, 'spades', 'Two of Spades'),
	'two_clubs': Card(2, 'clubs', 'Two of Clubs'),
	'two_diamonds': Card(2, 'diamonds', 'Two of Diamonds'),
	'two_hearts': Card(2, 'hearts', 'Two of Hearts'),
	'three_spades': Card(3, 'spades', 'Three of Spades'),
	'three_clubs': Card(3, 'clubs', 'Three of Clubs'),
	'three_diamonds': Card(3, 'diamonds', 'Three of Diamonds'),
	'three_hearts': Card(3, 'hearts', 'Three of Hearts'),
	'four_spades': Card(4, 'spades', 'Four of Spades'),
	'four_clubs': Card(4, 'clubs', 'Four of Clubs'),
	'four_diamonds': Card(4, 'diamonds', 'Four of Diamonds'),
	'four_hearts': Card(4, 'hearts', 'Four of Hearts'),
	'five_spades': Card(5, 'spades', 'Five of Spades'),
	'five_clubs': Card(5, 'clubs', 'Five of Clubs'),
	'five_diamonds': Card(5, 'diamonds', 'Five of Diamonds'),
	'five_hearts': Card(5, 'hearts', 'Five of Hearts'),
	'six_spades': Card(6, 'spades', 'Six of Spades'),
	'six_clubs': Card(6, 'clubs', 'Six of Clubs'),
	'six_diamonds': Card(6, 'diamonds','Six of Diamonds'),
	'six_hearts': Card(6, 'hearts', 'Six of hearts'),
	'seven_spades': Card(7, 'spades', 'Seven of Spades'),
	'seven_clubs': Card(7, 'clubs','Seven of Clubs'),
	'seven_diamonds': Card(7, 'diamonds', 'Seven of Diamonds'),
	'seven_hearts': Card(7, 'hearts','Seven of Hearts'),
	'eight_spades': Card(8, 'spades','Eight of Spades'),
	'eight_clubs': Card(8, 'clubs','Eight of Clubs'),
	'eight_diamonds': Card(8, 'diamonds','Eight of Diamonds'),
	'eight_hearts': Card(8, 'hearts','Eight of Hearts'),
	'nine_spades': Card(9, 'spades','Nine of Spades'),
	'nine_clubs': Card(9, 'clubs','Nine of Clubs'),
	'nine_diamonds': Card(9, 'diamonds','Nine of Diamonds'),
	'nine_hearts': Card(9, 'hearts','Nine of Hearts'),
	'ten_spades': Card(10, 'spades','Ten of Spades'),
	'ten_clubs': Card(10, 'clubs','Ten of Clubs'),
	'ten_diamonds': Card(10, 'diamonds','Ten of Diamonds'),
	'ten_hearts': Card(10, 'hearts','Ten of Hearts'),
	'jack_spades': Card(11, 'spades','Jack of Spades'),
	'jack_clubs': Card(11, 'clubs','Jack of Clubs'),
	'jack_diamonds': Card(11, 'diamonds','Jack of Diamonds'),
	'jack_hearts': Card(11, 'hearts','Jack of Hearts'),
	'queen_spades': Card(12, 'spades','Queen of Spades'),
	'queen_clubs': Card(12, 'clubs','Queen of Clubs'),
	'queen_diamonds': Card(12, 'diamonds','Queen of Diamonds'),
	'queen_hearts': Card(12, 'hearts','Queen of Hearts'),
	'king_spades': Card(13, 'spades','King of Spades'),
	'king_clubs': Card(13, 'clubs','King of Clubs'),
	'king_diamonds': Card(13, 'diamonds','King of Diamonds'),
	'king_hearts': Card(13, 'hearts','King of Hearts'),
	'ace_spades': Card(14, 'spades','Ace of Spades'),
	'ace_clubs': Card(14, 'clubs','Ace of Clubs'),
	'ace_diamonds': Card(14, 'diamonds','Ace of Diamonds'),
	'ace_hearts': Card(14, 'hearts','Ace of Hearts')
}

startup()
print("War: The Card Game.")
print("")
print("Press Enter to play.")
print("")
game_loop()

# make rules callable with user print somehow
#print("Rules: Each player begins with 26 randomized playing cards in their deck. Each turn, both players draw the top card of their deck and then those cards fight each other. The high card takes the loser hostage, assimilating that losing card into their own deck. If there is a tie, a war occurs and players then wager three face down cards from the top of their deck, battling with the fourth to determine who wins all of the wagered cards. The first player to run out of cards in their deck loses the game.")
