# life-expectancy-and-GDP
Analyze and plot data on GDP and life expectancy from the World Health Organization and the World Bank to try and identify the relationship between the GDP and life expectancy of six countries.

## Overview

This project explores the relationship between GDP and life expectancy across six countries from 2000 to 2015.

The goal is to understand:

* Has life expectancy increased over time in the six nations?
* Has GDP increased over time in the six nations?
* Is there a correlation between GDP and life expectancy of a country?

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

<img width="640" height="480" alt="avg_life_expectancy_by_country" src="https://github.com/user-attachments/assets/d173e1e8-5327-4b9e-8bd7-8a8175a1078f" />


---

### Average GDP by Country (Log Scale)

![Average GDP](images/avg_gdp.png)

---

### GDP vs Life Expectancy

![GDP vs Life Expectancy](images/gdp_vs_life_expectancy.png)

---

### GDP Over Time

![GDP Over Time](images/gdp_over_time.png)

---

### Life Expectancy Over Time

![Life Expectancy Over Time](images/life_expectancy_over_time.png)

---

## Key Insights

* Countries with higher GDP generally show higher life expectancy
* Life expectancy has increased over time across all countries
* GDP growth varies significantly between countries
* Zimbabwe shows notably lower life expectancy compared to others

---
## Project Structure

life-expectancy-gdp-analysis/
│
├── data_life_expectancy_gdp.csv
├── analysis.py
├── images/
│   ├── avg_life_expectancy.png
│   ├── avg_gdp.png
│   ├── gdp_vs_life_expectancy.png
│   ├── gdp_over_time.png
│   └── life_expectancy_over_time.png
└── README.md
_Data Source: 
This dataset is commonly used for exploratory analysis and is provided as part of the Codecademy Data Analytics career path._
---

## How to Run

1. Clone the repository:

   ```
   git clone <your-repo-link>
   ```

2. Navigate to the project folder:

   ```
   cd life-expectancy-gdp-analysis
   ```

3. Run the script:

   ```
   python analysis.py
   ```

---

## Future Improvements

* Add regression analysis to quantify relationships
* Normalize GDP for better comparison
* Create interactive visualizations
* Expand dataset to include more countries
