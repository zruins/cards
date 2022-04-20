from random import shuffle
from os import system as ossystem, name as osname

class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

class Deck:
	def __init__(self):
		self.contents = []
		for i in range(4):
			for j in range(13):
				self.contents.append(Card(j + 1, i))
		shuffle(self.contents)

	def reset(self):
		for i in dPile:
			if i == dPile.topCard():
				break
			self.contents.append(i)
			dPile.contents.remove(i)
		shuffle(self.contents)

class discardPile:
	def __init__(self):
		self.contents = []

	def topCard(self):
		return self.contents[len(self.contents) - 1]
		
class Hand:
	def __init__(self, num):
		self.num = num
		self.hand = []
		self.pile = drawPile.contents

	def discard(self, card):
		self.failed = False
		if isinstance(card, list):
			dPile.contents.append(self.hand[card[1]])
			self.hand.pop(int(card[1]))
		else:
			try:
				if int(self.hand[card].value) == int(dPile.topCard().value) or int(self.hand[card].suit) == int(dPile.topCard().suit):
					dPile.contents.append(self.hand[card])
					self.hand.pop(card)
			except ValueError:
				print("Cannot play card")
				self.failed = True

	def draw(self):
		if drawPile.contents == []:
			drawPile.reset()
		self.hand.append(self.pile[len(self.pile) - 1])
		self.pile.pop(len(self.pile) - 1)

drawPile = Deck()
dPile = discardPile()
clear = lambda: ossystem("cls" if osname in ('nt', 'dos') else "clear")

def init():
	print("How many players are there?")
	while True:
		try:
			players = int(input())
		except TypeError:
			print("Thats not a number")
			continue
		break
	playerlist = []
	turn = 0;
	faces = ["\u2660", "\u2663", "\u2665", "\u2666"]

	temp = Hand(None)
	temp.draw()
	temp.discard([None, 0])
	temp = None
	
	for i in range(players):
		playerlist.append(Hand(i))
		for j in range(7):
			playerlist[i].draw()

	while not (playerlist[(turn - 1) % len(playerlist)].hand == []):
		clear()
		input(f"Give the screen to Player {((turn + 1) % len(playerlist)) + 1}.\nIf you are Player {((turn + 1) % len(playerlist)) + 1}, press Enter\n")
		clear()

		temphand = []
		for i in playerlist[turn % len(playerlist)].hand:
			temphand.append(f"{faces[i.suit]}{i.value}")
		print(f"Last played card: {faces[dPile.topCard().suit]}{dPile.topCard().value}\n")
		print(f"Your cards: %s" % ", ".join(temphand))
		print("Number of cards: %s" % len(playerlist[turn % len(playerlist)].hand))
		print("1. Draw a card\n2. Play a card")
		
		while True:
			try:
				choice = int(input())
				if not (choice == 1 or choice == 2):
					raise TypeError
			except TypeError:
				print("Thats not a choice")
				continue
			break

		if choice == 1:
			playerlist[turn % len(playerlist)].draw()
		elif choice == 2:
			print("What card do you want to play?\n(First card is 0, second is 1, etc...)")
			playerlist[turn % len(playerlist)].failed = True
			while playerlist[turn % len(playerlist)].failed == True:
				c = input()
				playerlist[turn % len(playerlist)].discard(int(c))
		turn += 1

	clear();
	print(f"Player {playerlist[(turn % len(playerlist)) - 1].num + 1} wins!")

init()
