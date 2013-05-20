class Stats:
	def __init__(self, strength,constitution, dexterity, wisdom, intelligence, charisma):
		self.strength = strength
		self.dexterity = dexterity
		self.constitution = constitution
		self.wisdom = wisdom
		self.intelligence = intelligence
		self.charisma = charisma
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
