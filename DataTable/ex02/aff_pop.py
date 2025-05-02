import matplotlib.pyplot as plt
import pandas as pd


def parse_millions(value):
	if isinstance(value, str) and value.endswith("M"):
		try:
			return float(value[:-1])
		except ValueError:
			return None
	try:
		return float(value)
	except ValueError:
		return None


def plot_population(data: pd.DataFrame, country: str) -> None:
	"""
	Plot life expectancy data of Austria and given country.

	Parameters:
		data (pd.DataFrame): DataFrame containing life expectancy data.
	"""
	years = []
	try:
		years = [int(col) for col in data.columns[1:] if int(col) <= 2050]
	except ValueError:
		raise ValueError("The first row of the DataFrame must contain years as integers.")

	austria_data_row = data[data['country'] == 'Austria']
	country_data_row = data[data['country'] == country]
	austria_data = austria_data_row.iloc[0, 1:].apply(parse_millions)
	country_data = country_data_row.iloc[0, 1:].apply(parse_millions)
	array_length = len(years)
	plt.figure(figsize=(10, 6))
	plt.plot(years, country_data[:array_length])
	plt.plot(years, austria_data[:array_length])
	plt.title('Life Expectancy Over Years')
	plt.xlabel('Year')
	plt.ylabel('Life Expectancy (years)')
	plt.grid()
	plt.show()
