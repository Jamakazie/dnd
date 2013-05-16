from stats import Stats
from item import Item
from character import Character
from random import randrange, choice
import json

class Fighter(Character):
	def __init__(self, level, race, cclass, name='no name'):
		Character.__init__(self,level, race, name)
		self.cclass = cclass
		self.stats()
		self.base_attack_bonus()
		self.base_saves()
		self.alignment()
		self.equipment()
	
	def stats(self):
		bonus = 0
		remaining = self.level
		while(remaining > 4):
			remaining -= 4
			bonus += 1
		strength = randrange(12,19) + bonus
		constitution = randrange(12,19)
		dexterity = randrange(7,14)
		wisdom = randrange(7,14)
		intelligence = randrange(9,16)
		charisma = randrange (9,16)
		statvalues = Stats(strength, constitution, dexterity, wisdom, intelligence, charisma)
		self.stats = statvalues
	
	def base_attack_bonus(self):
		self.base_attack_bonus = self.level

	def base_saves(self):
		saves = {}
		saves['fort'] = 2 + self.level / 2
		saves['reflex'] = self.level / 4
		saves['will'] = self.level / 4
		self.saves = saves

	def alignment(self):
		ge = ['good', 'neutral', 'evil']
		lc = ['lawful', 'neutral', 'chaotic']
		ln = ['loyal', 'self', 'disloyal']
		alignment = []
		alignment.append(choice(ge))
		alignment.append(choice(lc))
		alignment.append(choice(ln))
		self.alignment = alignment
	
	def equipment(self):
		equipments = []
		weapon = Item('right hand', '+2 attack', 2000, False)
		ring = Item('figner', '+2 main stat', 5000, False)
		equipments.append(weapon)
		equipments.append(ring)
		self.items = equipments

	def __str__(self):
		return "I am %s, a level %s %s, my stats are %s, my saves are %s, my base attack bonus is %s, my alignment is %s, I have %s gold" % (self.name, self.cclass, self.level, self.stats, self.saves, self.base_attack_bonus, self.alignment, self.money)

f = Fighter(100, "Orc", "Fighter", "Bob")
print(f)
print json.dumps(f.saves)
