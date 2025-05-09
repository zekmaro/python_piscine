from load_csv import load
from aff_pop import plot_population	
import sys


def main():
		"""Program that loads a CSV file and prints its dimensions."""
		population_total = load("population_total.csv")
		plot_population(population_total, "France")


if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		print(f"AssertionError: {e}")
		sys.exit(1)