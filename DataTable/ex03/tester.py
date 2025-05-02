from load_csv import load
from projection_life import plot_life_expectancy_against_gdp
import sys


def main():
		"""Program that loads a CSV file and prints its dimensions."""
		gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
		life_expectancy_data = load("life_expectancy_years.csv")
		plot_life_expectancy_against_gdp(life_expectancy_data, gdp)


if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		print(f"AssertionError: {e}")
		sys.exit(1)