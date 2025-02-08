# %%
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.graph_objects as go
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# %% [markdown]
# <pre>
# +---------------------------------------------------------------------------------------------------------+
# |+-------------------------------------------------------------------------------------------------------+|
# ||[1. logo] 2. Louisville Metro Government Salary tracker   [3. Department drop down][ 4. year drop down]|| 
# |+-------------------------------------------------------------------------------------------------------+|
# |+--------+     6. salary spend 8. actual salary spend +-----+     +-------------------------------------+|
# ||5. plot |     7. salary data  9. salary data         |12. %|     |  11. horizontal bar plot department || 
# ||        |                                            +-----+     |                                     || 
# |+--------+                                                        |                                     || 
# |                                                                  |                                     || 
# |+---------------------------------------------------------------+ |                                     || 
# || 10. Top employees salary deviation data frame                 | |                                     || 
# ||                                                               | |                                     || 
# ||                                                               | |                                     || 
# ||                                                               | |                                     || 
# ||                                                               | |                                     || 
# ||                                                               | |                                     || 
# ||                                                               | |                                     || 
# |+---------------------------------------------------------------+ +-------------------------------------+|
# +---------------------------------------------------------------------------------------------------------+
# </pre>
# 

# %%
def check_data_updated():
    '''
    This function checks when the salary data was last updated
    to calculate 2024 salary data later.
    '''
    # Set up Selenium WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # URL of the page containing the data update info
    url = "https://data.louisvilleky.gov/datasets/8bd82421c9b94c37925fb37edaa1c5e8_0/explore"

    # Open the URL with Selenium
    driver.get(url)

    # Give some time for the page to load
    driver.implicitly_wait(5)

    # Targeting the specific list item that contains the "Data Updated" date and label
    data_updated_item = driver.find_element(By.CSS_SELECTOR, "li.metadata-item[data-test='modified']")

    # Extract both the date and label text
    date_div = data_updated_item.find_elements(By.TAG_NAME, 'div')[0].text
    label_div = data_updated_item.find_elements(By.TAG_NAME, 'div')[1].text

    # Print the extracted information
    print(f"Data Updated Date: {date_div}")
    print(f"Label: {label_div}")

    # Close the driver
    driver.quit()

# Call the function to check data update information
check_data_updated()


# %%
data = pd.read_csv("data/salary.csv")

# %%
date_div = 'November 27, 2024'

# %%
def process_salary_data(data, date_div):
    '''
    This function processes the salary data by performing several transformations:
    - Drops unnecessary columns
    - Calculates total expected salary
    - Fills missing values with 0
    - Merges department names
    - Calculates total weekly hours worked
    - Converts date to datetime and computes week and year for adjustments
    - Adjusts the annual rate for the specified year and week

    Args:
        data (pd.DataFrame): The input DataFrame with salary data
        date_div (str): The date string (from the check_data_updated function) to determine the week and year

    Returns:
        pd.DataFrame: The processed salary data
    '''
    # Drops columns we don't need
    cols_to_drop = ['jobTitle', 'Other', 'ObjectId']
    data = data.drop(columns=cols_to_drop)

    # Calculates total expected salary
    data['Salary_Total'] = data['Annual_Rate'] + data['Incentive_Allowance']

    # Filling missing data with 0
    data = data.fillna(0)

    # Merging the departments together
    data['Department'] = data['Department'].replace('Louisville Metro Police', 'Louisville Metro Police Department')
    data['Department'] = data['Department'].replace('Department of Corrections', 'Metro Corrections')

    # Calculates total weekly hours worked
    data['Hr_Rate'] = data['Regular_Rate'] / 2080
    data['Ot_Rate'] = data['Hr_Rate'] * 1.5
    data['Hr_Worked'] = data['Overtime_Rate'] / data['Ot_Rate'] / 52 + 40
    data.replace([np.inf, -np.inf], 40, inplace=True)

    # Convert the string to a datetime object
    date_object = datetime.strptime(date_div, "%B %d, %Y")

    # Get the week number of the calendar year
    week = date_object.isocalendar()[1]

    # Get the calendar year
    c_year = date_object.year

    # Check if there are any rows where the CalYear is equal to the specified c_year
    if (data['CalYear'] == c_year).any():
        # Convert Annual_Rate to weekly rate by dividing by 52
        data.loc[data['CalYear'] == c_year, 'Annual_Rate'] = data.loc[data['CalYear'] == c_year, 'Annual_Rate'] / 52

        # Scale the weekly rate for the specific week
        data.loc[data['CalYear'] == c_year, 'Annual_Rate'] = data.loc[data['CalYear'] == c_year, 'Annual_Rate'] * week

    return data


# %%
data = process_salary_data(data, date_div)
data.head()

# %% [markdown]
# # code for 5
# 
# 

# %%
# Code for 5
def plot_info(year, data) -> None:
    gauge = data.groupby(['CalYear'])[['YTD_Total', 'Salary_Total']].sum().reset_index()
    # Filter the data for the given year
    year_filter = gauge[gauge['CalYear'] == year]
    
    # Extract actual and expected values
    actual = year_filter['YTD_Total'].iloc[0]
    expected = year_filter['Salary_Total'].iloc[0]

    # Create the gauge plot
    steps = [
        {'range': [0, expected], 'color': '#004080'}  # Dark blue for expected salary
    ]
    
    # Add yellow step if actual exceeds expected
    if actual > expected:
        steps.append({'range': [expected, actual], 'color': 'yellow'})  # Yellow for actual salary
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=actual,
        delta={
            'reference': expected,
            'increasing': {'color': "red"},
            'decreasing': {'color': "green"}
        },
        gauge={
            'axis': {'range': [0, expected * 1.1]},  
            'bar': {'color': 'rgba(0,0,0,0)'},
            'steps': steps,
            'threshold': {
                'line': {'color': "red", 'width': 4},  
                'thickness': .95,
                'value': actual  # Place the red line at the actual
            }
        },
        title={'text': f"{year} Budgeted Salary Spend vs. Salary Spend Actual", 'font': {'size': 20}},
    ))

    fig.update_layout(
        title_font={'size': 20},  # Set font size for the overall layout title
    )

    # Show the figure
    fig.show()


# Example usage:
plot_info(2025, data)


# %%
# Example usage:
plot_info(2022, data)

# %%
# code for 7
def calculate_total_spend(year, data) -> str:
    # Filter the data for the specified year
    year_filter = data[data['CalYear'] == year]
    
    # Calculate the sum of 'YTD_Total' for the filtered data
    total_spend = year_filter['YTD_Total'].sum().round(2)

    # Formats thousands separators
    total_spend = "{:,.2f}".format(total_spend)
    
    # Return the total spend as a float
    return str(total_spend)

# %%
# code for 9 
def calculate_total_budget(year, data) -> str:
    # Filter the data for the specified year
    year_filter = data[data['CalYear'] == year]
    
    # Calculate the sum of 'Salary_Total' for the filtered data
    total_spend = year_filter['Salary_Total'].sum().round(2)

    # Formats thousands separators
    total_spend = "{:,.2f}".format(total_spend)
    
    # Return the total spend as a float
    return str(total_spend)

# %%
#code for 12
def calculate_budget_difference(year, data) -> str:
    # Filter the data for the specified year
    year_filter = data[data['CalYear'] == year]
    
    if year_filter.empty:
        return "No data for the specified year."
    
    # Extract actual and expected values
    actual_spend = year_filter['YTD_Total'].sum()
    budgeted_salary = year_filter['Salary_Total'].sum()

    # Calculate the percentage difference
    difference = ((actual_spend - budgeted_salary) / budgeted_salary) * 100
    
    # Format the difference with a '+' or '-' and thousands separators
    return f"{difference:+,.2f}%"



# %%
# Call the function for 7
total_sal_spend = calculate_total_spend(2024, data)

print(f'Total Salary Spend: {total_sal_spend}')

# %%
# Call the function for 9
total_sal_budget = calculate_total_budget(2024, data)

print(f'Total Salary Budgeted: {total_sal_budget}')

# %%
# Call the function for 12 
budget_difference = calculate_budget_difference(2024, data)
print(budget_difference)

# %%
# code for 10
def top_emp_dev(year, data):
    # we had to avoid division by zero and only calculate Discrepancy_Percent for employees with Salary_Total >= 20k
    # Filter the data for the given year
    top_employee = data[data['CalYear'] == year].copy()

    # Calculate the discrepancy and discrepancy ratio
    top_employee['Deviation'] = top_employee['YTD_Total'] - top_employee['Salary_Total']

    # Avoid division by zero and handle Salary_Total < 20k
    top_employee.loc[:, 'Discrepancy_Percent'] = top_employee.apply(
        lambda row: (row['Deviation'] / row['Salary_Total']) * 100 if row['Salary_Total'] >= 20000 and row['Salary_Total'] != 0 else None, axis=1
    )

    # Round the Discrepancy_Percent to 2 decimal places
    top_employee['Discrepancy_Percent'] = top_employee['Discrepancy_Percent'].round(2)

    # Sort the DataFrame by 'Discrepancy_Percent' in descending order
    top_employee = top_employee.sort_values(by='Discrepancy_Percent', ascending=False)

    # Keep only the specified columns
    top_employee = top_employee[['CalYear', 'Employee_Name', 'Department', 
                                 'YTD_Total', 'Salary_Total', 'Deviation', 
                                 'Discrepancy_Percent']]
    
    # Reset index and drop the old index column
    top_employee.reset_index(drop=True, inplace=True)

    return top_employee.head(10)


# %%
# Example usage for 10:
top_employee_result = top_emp_dev(2024, data)
top_employee_result

# %%
# code for 11
def department_discrepancy(year, data):
    # Group by 'CalYear' and 'Department', summing 'YTD_Total' and 'Salary_Total'
    department = data.groupby(['CalYear', 'Department'])[['YTD_Total', 'Salary_Total']].sum().reset_index()

    # Filter the data by the given year
    department = department[department['CalYear'] == year]

    # Calculate the percentage difference: ((YTD_Total - Salary_Total) / Salary_Total) * 100
    department['Discrepancy_Percent'] = ((department['YTD_Total'] - department['Salary_Total']) / department['Salary_Total']) * 100

    # Round the Discrepancy_Percent to 2 decimal places
    department['Discrepancy_Percent'] = department['Discrepancy_Percent'].round(2)

    # Sort the DataFrame by 'Discrepancy_Percent' in ascending order
    department = department.sort_values(by='Discrepancy_Percent', ascending=False)

    # Format 'YTD_Total' and 'Salary_Total' with thousands separators
    department['YTD_Total'] = department['YTD_Total'].apply(lambda x: f"{x:,.2f}")
    department['Salary_Total'] = department['Salary_Total'].apply(lambda x: f"{x:,.2f}")

    # Rename columns for final output
    department = department.rename(columns={
        'YTD_Total': 'Total Salary Spend',
        'Salary_Total': 'Salary Budget',
        'Discrepancy_Percent': 'Discrepancy Percent'
    })

    # Return the result
    return department


# %%
# Example usage:
department_result = department_discrepancy(2024, data)
department_result


