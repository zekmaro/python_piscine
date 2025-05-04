class calculator:
	"""A simple calculator class to perform basic arithmetic operations."""
	def __init__(self, vector: list[float]) -> None:
		"""Constructor for the calculator class."""
		self.vector = vector

	@staticmethod
	def dotproduct(V1: list[float], V2: list[float]) -> None:
		"""Calculate the dot product of two vectors."""
		print(f"Dot product is: {sum(x * y for x, y in zip(V1, V2))}")

	@staticmethod
	def add_vec(V1: list[float], V2: list[float]) -> None:
		print(f"Add Vector is: {[(float)(x + y) for x, y in zip(V1, V2)]}")

	@staticmethod
	def sous_vec(V1: list[float], V2: list[float]) -> None:
		print(f"Sous Vector is: {[(float)(x - y) for x, y in zip(V1, V2)]}")
