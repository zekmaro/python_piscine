from S1E9 import Character


class Baratheon(Character):
	def __init__(self, first_name, is_alive=True):
		"""Constructor for the Baratheon class."""
		super().__init__(first_name, is_alive)

	def __str__(self):
		"""String representation of the Baratheon class."""
		return f"Name: {self.first_name}, Status: {self.is_alive}, House: Baratheon"

	def __repr__(self):
		"""Representation of the Baratheon class."""
		return f"Baratheon({self.first_name}, {self.is_alive})"

	def die(self):
		"""Switch the alive status of the character."""
		super().die()


class Lannister(Character):
	def __init__(self, first_name, is_alive=True):
		"""Constructor for the Lannister class."""
		super().__init__(first_name, is_alive)
	
	def __str__(self):
		"""String representation of the Lannister class."""
		return f"Name: {self.first_name}, Status: {self.is_alive}, House: Lannister"
	
	def __repr__(self):
		"""Representation of the Lannister class."""
		return f"Lannister({self.first_name}, {self.is_alive})"
	
	def die(self):
		"""Switch the alive status of the character."""
		super().die()

	@staticmethod
	def create_lannister(name, is_alive=True):
		"""Static method to create a Lannister character."""
		return Lannister(name, is_alive)
