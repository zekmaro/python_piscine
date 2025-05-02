import matplotlib.pyplot as plt
import pandas as pd


def plot_life_expectancy(data: pd.DataFrame, country: str) -> None:
	"""
	Plot life expectancy data.

	Parameters:
		data (pd.DataFrame): DataFrame containing life expectancy data.
	"""
	years = []
	try:
		years = [int(col) for col in data.columns[1:]]
	except ValueError:
		raise ValueError("The first row of the DataFrame must contain years as integers.")

	print(years)
	country_data = data[data['country'] == country]
	print(country_data)
	plt.figure(figsize=(10, 6))
	plt.plot(years, country_data.iloc[0, 1:], marker='o', linestyle='-', color='b')
	plt.title('Life Expectancy Over Years')
	plt.xlabel('Year')
	plt.ylabel('Life Expectancy (years)')
	plt.grid()
	plt.show()


