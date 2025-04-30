from array2D import slice_me
import sys

def main():
	"""
	Test the slice_me function.
	"""
	family = [[1.80, 78.4],
		[2.15, 102.7],
		["hello", 98.5],
		[1.88, 75.2]
	]

	print(slice_me(family, 0, 2))
	print(slice_me(family, 1, -2))

if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		print(f"AssertionError: {e}")
		sys.exit(1)
