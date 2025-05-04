from in_out import outer, square, pow
import sys


def main():
	"""Main function to test the outer and inner functions."""
	my_counter = outer(3, square)
	print(my_counter())
	print(my_counter())
	print(my_counter())
	print("---")
	another_counter = outer(1.5, pow)
	print(another_counter())
	print(another_counter())
	print(another_counter())


if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		print(f"AssertionError: {e}")
		sys.exit(1)
