class Stats:
	def __init__(self, strength, dexterity, constitution, wisdom, intelligence, charisma):
		self.strength = strength
		self.dexterity = dexterity
		self.constitution = constitution
		self.wisdom = wisdom
		self.intelligence = intelligence
		self.charisma = charisma
	def __str__(self):
		return "Str:%s Dex: %s Con: %s Wis: %s Int: %s Cha: %s" % (self.strength, self.dexterity, self.constitution, self.wisdom, self.intelligence, self.charisma)
	