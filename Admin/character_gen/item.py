class Item:
	""" A class for (magic) items that characters can use """
	def __init__(self, slot, effects, price, iscursed):
		self.slot = slot
		self.effects = effects
		self.price = price
		self.iscursed = iscursed
	
