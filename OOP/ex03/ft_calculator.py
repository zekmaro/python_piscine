class calculator:
	"""A simple calculator class to perform basic arithmetic operations."""
	def __init__(self, vector: list[float]) -> None:
		"""Constructor for the calculator class."""
		self.vector = vector
	
	def __add__(self, object) -> None:
		self.vector = [x + object for x in self.vector]
		print(self.__str__())

	def __mul__(self, object) -> None:
		self.vector = [x * object for x in self.vector]
		print(self.__str__())

	def __sub__(self, object) -> None:
		self.vector = [x - object for x in self.vector]
		print(self.__str__())

	def __truediv__(self, object) -> None:
		if object == 0:
			raise ZeroDivisionError("Division by zero is not allowed.")
		self.vector = [x / object for x in self.vector]
		print(self.__str__())
	
	def __str__(self):
		return f"({self.vector})"

	def __repr__(self):
		return self.__str__()
