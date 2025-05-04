from DiamondTrap import King
import sys


def main():
	"""Main function to test the Character and Stark classes."""
	Joffrey = King("Joffrey")
	print(Joffrey.__dict__)
	Joffrey.set_eyes("blue")
	Joffrey.set_hairs("light")
	print(Joffrey.get_eyes())
	print(Joffrey.get_hairs())
	print(Joffrey.__dict__)


if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		print(f"AssertionError: {e}")
		sys.exit(1)
