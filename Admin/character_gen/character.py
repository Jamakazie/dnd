import json
from Admin import models
from stats import Stats
from random import choice, randint
import math
class Character(object):
	"""The Charater Creation Class"""
	gold_values = [0, 500, 1000,3000,6000,10500,16000,23500,33000,46000,62000,82000,108000,140000,185000,240000,315000,410000,530000,685000,880000] 
	def __init__(self, level, race, name="No name"):
		self.level = int(level)
		self.race = race 
		self.name = name
		self.alignment()
		self.gold()

	def gold(self):
		if self.level <= len(self.gold_values) -1:
			self.gold = self.gold_values[self.level]
		else:
			self.gold = self.level * 3000 + 880000
	def base_attack_bonus(self, amount):
		bab = '+';
		base = math.floor(self.level * amount)
		bab += str(int(base))
		while( base >= 6):
			base -= 5
			bab += "/+"  + str(int(base))
		self.base_attack_bonus = bab
		
	def alignment(self):
		lc = ['lawful', 'neutral', 'chaotic']
		ge = ['good', 'neutral', 'evil']
		ln = ['loyal', 'self', 'disloyal']
		alignment = []
		alignment.append(choice(lc))
		alignment.append(choice(ge))
		alignment.append(choice(ln))
		self.alignment = alignment
								
	def hp(self, mmax):
		mod = math.floor((self.stats.constitution - 10) / 2)
		total = mmax + mod
		for i in range(1, self.level):
			total += randint(1, mmax) + mod
		self.hp = int(total)
	
	def commit(self):
		self.charmod.save()
		
	def charmod(self):
		stats = json.dumps(self.stats.__dict__)
		skills = json.dumps(self.skills)
		saves = json.dumps(self.saves)
		attack_bonus = self.base_attack_bonus
		items = self.items
		alignment = self.alignment
		race = self.race
		hp = self.hp
		name = self.name
		gold = self.gold
		level = self.level
		cclass = self.cclass
		self.charmod = models.character(hp=hp,stats=stats, skills=skills, saves=saves, attack_bonus=attack_bonus, items=items, alignment=alignment, race=race, name=name, gold=gold, level=level, cclass=cclass)
		return self.charmod

	def fromCharacterDB(self,dbitem):
		self.stats = eval(dbitem.stats)#Stats.fromDict(dbitem.stats)
		self.skills = eval(dbitem.skills)
		self.saves = eval(dbitem.saves)
		self.base_attack_bonus = eval(dbitem.attack_bonus)
		self.items = eval(dbitem.items)
		self.alignment = eval(dbitem.alignment)
		self.race = dbitem.race
		self.name = dbitem.name
		self.gold = eval(dbitem.gold)
		self.level = eval(dbitem.level)
		self.cclass = dbitem.cclass
