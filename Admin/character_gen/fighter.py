from stats import Stats
from item import Item
from character import Character
from random import randrange, choice
from Admin import models
import json

class Fighter(Character):
	def __init__(self, level, race, name='no name'):
		Character.__init__(self,level, race, name)
		self.cclass = "Fighter"
		self.stats()
		self.hp(10)
		self.base_attack_bonus(1.0)
		self.base_saves()
		self.skills()
		self.ac = 10 + int((self.stats.dexterity - 10) / 2 )
		self.equipment()
		self.totaltohit += int(1.0 * self.level) + int((self.stats.strength - 10) / 2)
	
	def stats(self):
		bonus = self.level  / 4 
		strength = randrange(12,19) + bonus
		constitution = randrange(12,19)
		dexterity = randrange(7,14)
		wisdom = randrange(7,14)
		intelligence = randrange(9,16)
		charisma = randrange (9,16)
		statvalues = Stats(strength, constitution, dexterity, wisdom, intelligence, charisma, self.race)
		self.stats = statvalues

	def base_saves(self):
		saves = {}
		saves['fort'] = 2 + self.level / 2
		saves['reflex'] = self.level / 3
		saves['will'] = self.level / 3
		self.saves = saves
	
	def equipment(self):
		equipments = []
		weapongold = self.gold * .6
		armorgold = self.gold * .4
		weaponbonus = 0
		armorcost = 0
		weaponcost = 0
		while weapongold >= (weaponbonus + 1) ** 2 * 2000:
			weaponbonus += 1
			weaponcost = weaponbonus ** 2 * 2000
		
		armorbonus = 0
		while armorgold >= (armorbonus + 1) ** 2 * 1000:
			armorbonus += 1
			armorcost = armorbonus ** 2 * 1000

		leftover = self.gold - weaponcost - armorcost
		bonus = 0
		while leftover >= (bonus + 1) ** 2 * 1000:
			bonus += 1

		self.totaltohit = weaponbonus
		self.stats.strength += bonus
		self.ac += armorbonus
		weapon = Item('Weapon', ('+%s attack' % weaponbonus), weaponcost, False)
		armor = Item('Armor', ('+%s' % armorbonus), armorcost, False)
		magic = Item('Magic', ('+%s strength' % bonus), bonus ** 2 * 1000, False)
		leftover = Item('leftover', 'gold', self.gold, False)
		equipments.append(weapon.__dict__)
		equipments.append(armor.__dict__)
		equipments.append(magic.__dict__)
		equipments.append(leftover.__dict__)
		self.items = equipments
	
	def skills(self):
		self.skills = ["i am good at stuff"]

	def __str__(self):
		return "I am %s, a level %s %s, my stats are %s, my saves are %s, my base attack bonus is %s, my alignment is %s, I have %s gold" % (self.name, self.cclass, self.level, self.stats, self.saves, self.base_attack_bonus, self.alignment, self.gold)
	
	def jsonify(self):
		return { 'Fighter':{
				'stats': self.stats.__dict__,
				'skills': self.skills,
				'saves': self.saves,
				'attack_bonus':self.base_attack_bonus,
				'items' : self.items,
				'alignment' : self.alignment,
				'race' : self.race,
				'name' : self.name,
				'gold' : self.gold,
				'level' : self.level,
				'class' : self.cclass,
				}
			}
	def json(self):
		return json.dumps(self.jsonify())

