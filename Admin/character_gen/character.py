class Character(object):
	"""The Charater Creation Class"""
	money_values = [100, 300, 900, 2700]
	def __init__(self, level, race, name="No name"):
		self.level = level
		self.race = level
		self.name = name
		self.money()

	def money(self):
		if self.level <= len(self.money_values):
			self.money = self.money_values[self.level]
		else:
			self.money = self.level * 300
	
	