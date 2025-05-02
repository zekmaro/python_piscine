from S1E9 import Character, Stark
import sys


def main():
	"""Main function to test the Character and Stark classes."""
	Ned = Stark("Ned")
	print(Ned.__dict__)
	print(Ned.is_alive)
	Ned.die()
	print(Ned.is_alive)
	print(Ned.__doc__)
	print(Ned.__init__.__doc__)
	print(Ned.die.__doc__)
	print("---")
	Lyanna = Stark("Lyanna", False)
	print(Lyanna.__dict__)
	# hodor = Character("hodor")


if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		print(f"AssertionError: {e}")
		sys.exit(1)