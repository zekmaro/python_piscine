from S1E7 import Baratheon, Lannister
import sys


def main():
	"""Main function to test the Character and Stark classes."""
	Robert = Baratheon("Robert")
	print(Robert.__dict__)
	print(Robert.__str__)
	print(Robert.__repr__)
	print(Robert.is_alive)
	Robert.die()
	print(Robert.is_alive)
	print(Robert.__doc__)
	print("---")
	Cersei = Lannister("Cersei")
	print(Cersei.__dict__)
	print(Cersei.__str__)
	print(Cersei.is_alive)
	print("---")
	Jaine = Lannister.create_lannister("Jaine", True)
	print(f"Name : {Jaine.first_name, type(Jaine).__name__}, Alive : {Jaine.is_alive}")


if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		print(f"AssertionError: {e}")
		sys.exit(1)