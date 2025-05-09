from ft_calculator import calculator
import sys


def main():
	v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
	v1 + 5
	print("---")
	v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
	v2 * 5
	print("---")
	v3 = calculator([10.0, 15.0, 20.0])
	v3 - 5
	v3 / 5


if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		print(f"AssertionError: {e}")
		sys.exit(1)
