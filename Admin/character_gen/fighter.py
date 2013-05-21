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
		self.equipment()
		self.skills()
	
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
		weapon = Item('right hand', '+2 attack', 2000, False)
		ring = Item('figner', '+2 main stat', 5000, False)
		equipments.append(weapon.__dict__)
		equipments.append(ring.__dict__)
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

