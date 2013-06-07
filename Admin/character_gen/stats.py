class Stats:
	def __init__(self, strength,constitution, dexterity, wisdom, intelligence, charisma, race):
		self.strength = strength
		self.dexterity = dexterity
		self.constitution = constitution
		self.wisdom = wisdom
		self.intelligence = intelligence
		self.charisma = charisma
		self.modStats(race)

	def __str__(self):
		return "Str:%s Dex: %s Con: %s Wis: %s Int: %s Cha: %s" % (self.strength, self.dexterity, self.constitution, self.wisdom, self.intelligence, self.charisma)

	def fromDict(self, dic):
		fromdic = eval(dic)
		self.strength = fromdic['strength']
		self.dexterity = fromdic['dexterity']
		self.constituion = fromdic['constitution']
		self.wisdom = fromdic['wisdom']
		self.intelligence = fromdic['intelligence']
		self.charisma = fromdic['charisma']
	def modStats(self, race):
		if race == "Orc":
			self.strength += 4
			self.intelligence -= 2
			self.wisdom -= 2
			self.charisma -= 2
		elif race == "Dwarf":
			self.constitution += 2
			self.wisdom += 2
			self.charisma -= 2
		elif race == "Elf":
			self.dexterity += 2
			self.intelligence += 2
			self.constitution -= 2
		elif race == "Gnome":
			self.constitution += 2
			self.charisma += 2
			self.strength -= 2
		elif race == "Halfling":
			self.dexterity += 2
			self.charisma += 2
			self.strength -= 2
		elif race == "Kobold":
			self.strength -= 4
			self.constitution -= 2
			self.dexterity += 2
		
		pass
