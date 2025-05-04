from abc import ABC, abstractmethod


class Character(ABC):
	"""Abstract base class for characters in the game."""

	def __init__(self, first_name, is_alive=True):
		"""Constructor for the Character class."""
		self.first_name = first_name
		self.is_alive = is_alive

	def __str__(self):
		"""String representation of the Character class."""
		return f"Name: {self.first_name}, Age: {self.age}"

	def __repr__(self):
		"""Representation of the Character class."""
		return f"Character({self.first_name}, {self.age})"
	
	@abstractmethod
	def die(self):
		"""Switch the alive status of the character."""
		if self.is_alive:
			self.is_alive = False


class Stark(Character):
	def __init__(self, first_name, is_alive=True):
		"""Constructor for the Stark class."""
		super().__init__(first_name, is_alive)
		self.age = 0

	def __str__(self):
		"""String representation of the Stark class."""
		return f"Name: {self.first_name}, Age: {self.age}, House: Stark"

	def __repr__(self):
		"""Representation of the Stark class."""
		return f"Stark({self.first_name}, {self.age})"

	def die(self):
		super().die()
