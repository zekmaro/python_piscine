from statistics import ft_statistics
import sys


def main():
	"""Main function to test the ft_statistics function."""
	ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
	print("-----")
	ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
	print("-----")
	ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
	print("-----")
	ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		print(f"AssertionError: {e}")
		sys.exit(1)
