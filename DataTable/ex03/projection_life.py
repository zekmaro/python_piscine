import pandas as pd
import matplotlib.pyplot as plt


def plot_life_expectancy_against_gdp(df_life_expect: pd.DataFrame, df_gdp: pd.DataFrame) -> None:
	"""
	Plot life expectancy against GDP for a given country.

	Parameters:
		df_life_expect (pd.DataFrame): DataFrame containing life expectancy data.
		df_gdp (pd.DataFrame): DataFrame containing GDP data.
	"""
	merged_data = pd.merge(
		df_life_expect[["country", "1900"]],
		df_gdp[["country", "1900"]],
		on="country",
		suffixes=("_life", "_gdp")
	)

	print(merged_data.columns)

	merged_data["1900_life"] = pd.to_numeric(merged_data["1900_life"], errors="coerce")
	merged_data["1900_gdp"] = pd.to_numeric(merged_data["1900_gdp"], errors="coerce")

	merged_data.dropna(inplace=True)

	life_expect_1900 = merged_data["1900_life"]
	gdp_1900 = merged_data["1900_gdp"]

	plt.figure(figsize=(10, 6))
	plt.scatter(life_expect_1900, gdp_1900, color='blue', alpha=0.5)
	plt.title('Life Expectancy vs GDP in 1900')
	plt.xlabel('Life Expectancy (years)')
	plt.ylabel('GDP (in millions)')
	plt.grid()
	plt.show()
