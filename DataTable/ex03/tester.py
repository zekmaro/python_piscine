from load_csv import load
from aff_pop import plot_population	
import sys


def main():
		"""Program that loads a CSV file and prints its dimensions."""
		gdp = load("population_total.csv")
		life_expectancy_data = load("life_expectancy_years.csv")
		


if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		print(f"AssertionError: {e}")
		sys.exit(1)