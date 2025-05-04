from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
	"""King class that inherits from Baratheon and Lannister classes."""
	def __init__(self, first_name, is_alive=True):
		"""Constructor for the King class."""
		super().__init__(first_name, is_alive)
		self.eyes = None
		self.hairs = None

	def __str__(self):
		"""String representation of the King class."""
		return f"Name: {self.first_name}, Status: {self.is_alive}, House: Baratheon, Lannister"
	
	def __repr__(self):
		"""Representation of the King class."""
		return f"King({self.first_name}, {self.is_alive})"
	
	def die(self):
		"""Switch the alive status of the character."""
		super().die()
	
	def set_eyes(self, eyes):
		"""Set the eye color of the character."""
		self.eyes = eyes
	
	def set_hairs(self, hairs):
		"""Set the hair color of the character."""
		self.hairs = hairs

	def get_eyes(self):
		"""Get the eye color of the character."""
		return self.eyes
	
	def get_hairs(self):
		"""Get the hair color of the character."""
		return self.hairs
