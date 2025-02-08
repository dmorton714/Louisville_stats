import pandas as pd
import numpy as np
from datetime import datetime

def process_salary_data(data, date_div):
    '''
    Process salary data with transformations and calculations
    '''
    # Filling missing data with 0
    data = data.fillna(0)

    # Merging the departments together for consistency
    data['Department'] = data['Department'].replace({
        'Louisville Metro Police': 'Louisville Metro Police Department',
        'Department of Corrections': 'Metro Corrections'
    })

    # Convert the string to a datetime object
    date_object = datetime.strptime(date_div, "%B %d, %Y")
    week = date_object.isocalendar()[1]
    c_year = date_object.year

    # Adjust annual rate for current year data
    if (data['CalYear'] == c_year).any():
        data.loc[data['CalYear'] == c_year, 'Annual_Rate'] = (
            data.loc[data['CalYear'] == c_year, 'Annual_Rate'] / 52 * week
        )

    return data

def get_metrics(data, year):
    '''
    Calculate key metrics for the dashboard
    '''
    year_data = data[data['CalYear'] == year]
    total_spend = year_data['YTD_Total'].sum()
    total_budget = year_data['Annual_Rate'].sum() + year_data['Incentive_Allowance'].sum()
    variance_pct = ((total_spend - total_budget) / total_budget) * 100 if total_budget != 0 else 0

    return {
        'total_spend': total_spend,
        'total_budget': total_budget,
        'variance_pct': variance_pct
    }

def get_top_deviations(data, year, limit=10):
    '''
    Get top salary deviations
    '''
    year_data = data[data['CalYear'] == year].copy()
    budget = year_data['Annual_Rate'] + year_data['Incentive_Allowance']
    year_data['Deviation'] = year_data['YTD_Total'] - budget
    year_data['Deviation_Pct'] = (year_data['Deviation'] / budget * 100).round(2)
    year_data['Annual_Rate'] = year_data['Annual_Rate'].round(2)

    return year_data.nlargest(limit, 'Deviation_Pct')[
        ['Employee_Name', 'Department', 'YTD_Total', 'Annual_Rate', 'Deviation', 'Deviation_Pct']
    ]