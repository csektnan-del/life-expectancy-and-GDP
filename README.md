# life-expectancy-and-GDP

## Overview

This project explores the relationship between GDP and life expectancy across six countries from 2000 to 2015.

The goal is to understand:

* Has life expectancy increased over time in the six nations?
* Has GDP increased over time in the six nations?
* Is there a correlation between GDP and life expectancy of a country?

Data Source: This dataset is commonly used for exploratory analysis and comes from the World Health Organization and the World Bank.

---

## Dataset

The dataset contains:

* Country
* Year
* GDP (in USD)
* Life expectancy at birth (years)

---

## Tools Used

* Python
* pandas
* seaborn
* matplotlib

---

## Key Visualizations

### Average Life Expectancy by Country

Most countries in the dataset cluster between 70 and 80 years, with Zimbabwe as an outlier.

<img width="640" height="480" alt="avg_life_expectancy_by_country" src="https://github.com/user-attachments/assets/d173e1e8-5327-4b9e-8bd7-8a8175a1078f" />


---

### Average GDP by Country (Log Scale)
GDP in this chart is shown using a log scale for clearer comparison given the variation in averages by country. 

<img width="640" height="480" alt="avg_GDP_by_country" src="https://github.com/user-attachments/assets/3bc24199-b146-4704-af74-567090192a76" />


---

### GDP vs Life Expectancy
All countries show a trend of increasing life expectancy along with increasing GDP, though that trend is most pronounced in Zimbabwe and there are diminishing returns in terms of life expectancy as GDP increases in the other, higher income, countries.

<img width="640" height="480" alt="gdp_vs_life_expectancy" src="https://github.com/user-attachments/assets/8adb4486-ac9a-456b-89d1-22ebfb057112" />


---

### GDP Over Time
GDP has generally increased across all countries over time, though the rate of increase varies by country.
<img width="640" height="480" alt="gdp_over_time" src="https://github.com/user-attachments/assets/d28b0ffc-1422-40d4-b6f0-bdd40487f042" />


---

### Life Expectancy Over Time
Similar to GDP, life expectancy has generally increased over time across all countries, though at different rates.
<img width="640" height="480" alt="life_expectancy_over_time" src="https://github.com/user-attachments/assets/76f110d7-2d1b-4da8-93b7-eb18e3304f5a" />

### Per Country Relationship between GDP and Life Expectancy
The following charts break down the relationship between GDP and life expectancy for each country over the time period measured (2000-2015).

<img width="600" height="400" alt="Chile_GDP_vs_Life_expectancy_over_time" src="https://github.com/user-attachments/assets/8bf55543-6fb5-4a97-a324-904dacf6b425" />

<img width="600" height="400" alt="China_GDP_vs_Life_expectancy_over_time" src="https://github.com/user-attachments/assets/84e06d2d-4ba0-4223-9a77-6a727288c575" />

<img width="600" height="400" alt="Germany_GDP_vs_Life_expectancy_over_time" src="https://github.com/user-attachments/assets/13ed19c7-37c9-412f-8cb2-89d2c5800510" />

<img width="600" height="400" alt="Mexico_GDP_vs_Life_expectancy_over_time" src="https://github.com/user-attachments/assets/6877f772-5879-472a-8dae-6af7c1f9f3f5" />

<img width="600" height="400" alt="USA_gdp_vs_life_expectancy_over_time" src="https://github.com/user-attachments/assets/c338244f-97ed-4206-903b-4c7dc71fc0ac" />

<img width="600" height="400" alt="Zimbabwe_GDP_vs_Life_expectancy_over_time" src="https://github.com/user-attachments/assets/5e15bd62-f634-4da7-b5c4-a4e1dc0f55fa" />


---

## Key Insights

* Countries with higher GDP generally show higher life expectancy
* Life expectancy has increased over time across all countries analyzed
* GDP growth varies significantly between countries but is generally positive or stable

---

## How to Run

1. Clone the repository:

   git clone https://github.com/csektnan-del/life-expectancy-and-GDP.git

2. Navigate to the project folder:

   cd life-expectancy-and-GDP

3. (Optional but recommended) Install dependencies:

   pip install pandas seaborn matplotlib

4. Run the script:

   python script_life_expectancy_gdp.py

---

## Future Improvements

* Add regression analysis to quantify relationships
* Normalize GDP for better comparison
* Expand dataset to include additional countries
* Create interactive visualizations
