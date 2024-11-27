# Hours vs Tickets Analysis

**Status:** In progress — Currently cleaning up the project in the `refactoring.ipynb` notebook.

## Project Overview

The Hours vs Tickets project analyzes the correlation between the hours worked by police officers and the number of citations they issue. The goal of this analysis is to determine whether there is a relationship between an officer's working hours and their ticket issuance patterns.

Multiple datasets are combined and cleaned to create a unified dataset, followed by feature engineering to calculate the total hours worked and the number of tickets issued. The analysis uncovers insights into how work hours may influence ticket issuance, providing useful information for police departments and policymakers.

**Key Findings**

- **Correlation Analysis:** The analysis reveals a weak positive correlation of 0.2151 between the hours worked and the number of tickets issued. This suggests that officers who work more hours tend to issue more tickets, but the correlation is not strong enough to establish a definitive relationship.

- **Data Insights:** The project includes insightful visualizations and summary statistics that provide a deeper understanding of the dataset and any patterns that emerge from the analysis.
Features

- **Data Cleaning and Integration:** Combines and cleans multiple datasets to ensure a unified dataset for analysis.

- **Feature Engineering:** Calculates key features, including total hours worked and the total number of tickets issued by each officer.

- **Correlation Calculation:** Identifies the relationship between the number of hours worked and ticket issuance, with a correlation coefficient of 0.2151.

- **Visualizations:** Utilizes data visualizations to illustrate key findings and trends.
Summary Statistics: Provides summary statistics to highlight important patterns within the data.

### Purpose

The purpose of this project is to explore the potential correlation between the hours worked by police officers and their ticket issuance. By better understanding this relationship, the project aims to provide valuable insights into the factors that may influence policing behavior and inform decision-making regarding workload and performance expectations.

### Technologies Used:

- **Python 3.10** + – Primary programming language for data processing and analysis.

- **Jupyter Notebook **– Used for exploratory analysis and cleaning (refactoring.ipynb).

- **Pandas** – Data manipulation and cleaning.

- **NumPy** – Numerical operations and statistical calculations.

- **Seaborn & Matplotlib** – Data visualization libraries used for generating charts and graphs.

### Installation and Setup

**Prerequisites**

Ensure you have Python 3.10 + installed, along with the required libraries. You can install the necessary dependencies by following these steps:

**Clone the repository:**

```bash
git clone https://github.com/dmorton714/Louisville_stats.git
```

**Navigate to the project directory:**

```bash
cd hours_vs_tickets
```

**Install the required dependencies:**
*Coming Soon* 
```bash
pip install -r requirements.txt
```

### Running the Analysis

Open the project’s Jupyter notebook `refactoring.ipynb`.
Execute the cells to clean, process, and analyze the data.
Review the correlation analysis and visualizations to explore trends between hours worked and ticket issuance.

## Future Work
The project is ongoing, and future enhancements may include:

- Expanding the dataset to incorporate additional variables, such as officer demographics or ticket types.
- Implementing more advanced statistical methods or machine learning models to explore the relationship between hours worked and ticket issuance in greater depth.
- Refining the data visualization components to present findings more clearly and interactively.