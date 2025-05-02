from load_csv import load
import sys


def main():
		"""Program that loads a CSV file and prints its dimensions."""
		print(load("life_expectancy_years.csv"))


if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		print(f"AssertionError: {e}")
		sys.exit(1)