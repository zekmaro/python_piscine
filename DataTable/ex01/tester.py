from load_csv import load
from aff_life import plot_life_expectancy
import sys


def main():
		"""Program that loads a CSV file and prints its dimensions."""
		life_expectancy_data = load("life_expectancy_years.csv")
		plot_life_expectancy(life_expectancy_data, "France")


if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		print(f"AssertionError: {e}")
		sys.exit(1)