from stats import Stats
import math
class Character(object):
	"""The Charater Creation Class"""
	gold_values = [100, 300, 900, 2700]
	def __init__(self, level, race, name="No name"):
		self.level = int(level)
		self.race = race 
		self.name = name
		self.gold()

	def gold(self):
		if self.level <= len(self.gold_values):
			self.gold = self.gold_values[self.level]
		else:
			self.gold = self.level * 300
	def base_attack_bonus(self, amount):
		bab = '+';
		base = math.floor(self.level * amount)
		bab += str(int(base))
		while( base >= 6):
			base -= 5
			bab += "/+"  + str(int(base))
		self.base_attack_bonus = bab
	
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
