# Louisville Open Data Analysis Projects

This repository is a dynamic learning environment dedicated to exploring Louisville's open data through a series of diverse passion projects. Designed to foster growth in data analysis, it offers hands-on experience with real-world datasets, emphasizing the development of robust data processing, cleaning, and visualization skills. Each project is carefully crafted to uncover insights while showcasing best practices in data science. To ensure clarity and transparency, every project includes its own README.md file, detailing its scope, objectives, and methodologies. All data sourced from  [Louisville Open Data](https://data.louisvilleky.gov/) or Freedom of Information Act requests. 

---

## Projects: 
The projects below, each providing a unique opportunity to engage with Louisville's open data and extract valuable insights. These projects are designed to challenge and enhance data analysis my skills, offering practical experience in data processing, merging, and visualization. Analyzing trends or uncovering hidden patterns.

## **hours vs tickets:**
**status:** Working on cleaning up the project in the `refactoring.ipynb` notebook. 

Hours vs Tickets, investigates whether there is a correlation between the hours worked by police officers and the number of citations they issue. 

We combine multiple datasets to create a unified, clean dataset. We then engineered features to determine hours worked and ticket counts. So we could then better understand trends and relationships in the data.

The analysis reveals a weak positive correlation of 0.2151 between hours worked and the number of tickets issued, suggesting a slight tendency for officers who work more hours to write more tickets. However, the correlation is not strong, indicating that other factors likely influence ticket issuance. 

The project also includes insightful data visualizations and summary statistics, allowing for a deeper understanding of the dataset. 

## **Salary Dashboard**

**Status:** In the early stages setting up how the data will be called and used. 

The Salary Dashboard is a data analysis tool designed to track the city's salary spending and ensure adherence to the allocated budget. The dashboard provides an overview of the city's total salary expenditures, comparing actual spending against the budget. It also offers a detailed breakdown by department, highlighting areas where salary spending is deviating from expectations.

Key features include:

- **City-Wide Overview:** Displays the overall salary spending, showing whether the city is on track with its budget.

- **Department Breakdown:** Allows users to view salary expenditures by individual departments, helping to identify discrepancies and trends.

- **Top Employees:** Highlights the top employees whose salaries deviate significantly from the expected amounts.

- **Trend Analysis:** Users can drill down by department and year to explore salary trends, comparing data year-over-year and identifying patterns.

This dashboard aims to provide city administrators, and financial managers with a clear, interactive way to monitor salary expenditures, ensure budget compliance, and make informed decisions.

## **Plotting Templates Overview:**

**Status:** Very early stages and some generic place holder ideas are in place. 

The Plotting Templates project aims to serve as a reusable source of plots and a style guide for visualizations across various projects. This tool allows users to easily generate consistent, professional-looking plots by simply calling the plotting package and providing basic input, such as the title, x and y axis labels, and plot colors.

**Key features include:**

- Consistent Visualizations: Automatically applies predefined styles, ensuring that all plots within a project have a uniform appearance.

- Simple User Input: Users only need to enter essential details like title, axis labels, and colors, making it easy to generate customized plots.

- Reusable Templates: Provides a library of pre-built plot templates that can be integrated into other projects, saving time and ensuring consistency.

- Potential for External Use: If further developed, this project could serve as a standalone package for external use, offering a consistent plotting solution for various users.

This project is designed to streamline the plotting process and maintain visual consistency across different datasets and projects.

--- 

### Data Sources
The data is sourced from [Louisville Open Data](https://data.louisvilleky.gov/), along with additional datasets obtained via Freedom of Information Act (FOIA) requests.

Refer to the `api_calls` folder to run the api calls for the project you intend to look at. 
The folder contains a `README.md` for running the API calls and which ones to run for each project. 
