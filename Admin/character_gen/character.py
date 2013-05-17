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
	
	
