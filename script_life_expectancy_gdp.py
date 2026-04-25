#Import neded packages
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Load the data
from pathlib import Path
file_path = Path(__file__).parent / "data_life_expectancy_gdp.csv"
df = pd.read_csv(file_path)

#Create file to save charts
output_dir = Path(__file__).parent / "images"
output_dir.mkdir(exist_ok=True)

#Shorten USA label for charts
df['Country'] = df['Country'].replace({'United States of America': 'USA'})

#Chart average life expectancy by country
avg_life_expectancy = df.groupby('Country')['Life expectancy at birth (years)'].mean().reset_index().sort_values(by='Life expectancy at birth (years)', ascending=True)
plt.bar(avg_life_expectancy['Country'], avg_life_expectancy['Life expectancy at birth (years)'])
plt.xlabel('Country')
plt.ylabel('Life Expectancy (years)')
plt.title('Average Life Expectancy by Country')
plt.xticks(rotation = 45)
plt.tight_layout()
#plt.show()
plt.savefig(output_dir / "avg_life_expectancy_by_country.png")
plt.clf()

#Chart average GDP by country
avg_gdp = df.groupby('Country')['GDP'].mean().reset_index().sort_values(by='GDP', ascending=True)
plt.bar(avg_gdp['Country'], avg_gdp['GDP'])
plt.xlabel('Country')
plt.ylabel('GDP (USD, log scale)')
plt.title('Average GDP by Country (Log Scale)')
plt.xticks(rotation = 45)
plt.tight_layout()
plt.yscale('log')
#plt.show()
plt.savefig(output_dir / "avg_GDP_by_country.png")
plt.clf()

#Relationship of GDP and life expectancy
sns.scatterplot(data = df, x = "GDP", y = "Life expectancy at birth (years)", hue = 'Country')
plt.xscale('log')
plt.xlabel('GDP (USD, log scale)')
plt.ylabel('Life Expectancy (years)')
plt.title('GDP vs Life Expectancy')
#plt.show()
plt.savefig(output_dir / "gdp_vs_life_expectancy.png")
plt.clf()

#Relationship of GDP and time
sns.lineplot(data = df, y = "GDP", x = "Year", hue = 'Country')
plt.yscale('log')
plt.ylabel('GDP (USD, log scale)')
plt.xlabel('Year')
plt.title('GDP Over Time by Country')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
#plt.show()
plt.savefig(output_dir / "gdp_over_time.png")
plt.clf()

#Relationship of life expectancy and time
sns.lineplot(data = df, x = "Year", y = "Life expectancy at birth (years)", hue = 'Country')
plt.xlabel('Year')
plt.ylabel('Life Expectancy (years)')
plt.title('Life Expectancy Over Time by Country')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
#plt.show()
plt.savefig(output_dir / "life_expectancy_over_time.png")
plt.clf()

#Create GDPxLife expectancy charts for each country
for country in df['Country'].unique():
    country_data = df[df['Country'] == country]
    plt.figure(figsize=(6,4))
    sns.lineplot(data=country_data, x='GDP', y='Life expectancy at birth (years)')
    plt.title(f'{country}: GDP vs Life expectancy over time')
    plt.xlabel('GDP in dollars')
    plt.ylabel('Life Expectancy (years)')
    plt.tight_layout()
    #plt.show()
    plt.savefig(output_dir / (f'{country}_gdp_vs_life_expectancy_over_time.png'))
    plt.clf()