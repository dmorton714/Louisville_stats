import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import numpy as np

# Initialize the app
app = dash.Dash(__name__)

# Sample data for dropdowns and plots
departments = ['Police', 'Fire', 'Public Works', 'Health']
years = [2021, 2022, 2023]

# Example data for the table (use actual data in your case)
salary_data = pd.DataFrame({
    'Employee': ['John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Brown'],
    'Salary': [50000, 60000, 55000, 58000],
    'Deviation': [2000, -1000, 1500, -500]
})

# Example plot (replace with your actual plot)
fig = px.bar(salary_data, x='Employee', y='Salary', title="Salary Spend")

# Layout of the dashboard
app.layout = html.Div([
    html.Div([
        # Logo placeholder
        html.Div("1. logo", style={'width': '10%', 'display': 'inline-block', 'textAlign': 'center'}),
        
        # Title and dropdowns
        html.Div([
            html.H1("2. Louisville Metro Government Salary Tracker", style={'display': 'inline-block', 'padding': '10px'}),
            dcc.Dropdown(
                id='department-dropdown',
                options=[{'label': dept, 'value': dept} for dept in departments],
                placeholder="3. Department",
                style={'width': '200px', 'display': 'inline-block'}
            ),
            dcc.Dropdown(
                id='year-dropdown',
                options=[{'label': str(year), 'value': year} for year in years],
                placeholder="4. Year",
                style={'width': '120px', 'display': 'inline-block'}
            ),
        ], style={'display': 'flex', 'alignItems': 'center'}),
    ], style={'borderBottom': '2px solid #000', 'padding': '10px'}),

    # Salary plots and data
    html.Div([
        html.Div([
            # Placeholder for plot (5)
            dcc.Graph(figure=fig),
        ], style={'width': '50%', 'display': 'inline-block'}),

        html.Div([
            # Salary data (7) - replace with your data
            html.H3("6. Salary Spend"),
            html.Div("Salary data table here (replace with actual data table)"),
            html.H3("9. Actual Salary Spend"),
            html.Div("Actual Salary data here (replace with actual data)"),
        ], style={'width': '50%', 'display': 'inline-block'}),

    ], style={'display': 'flex'}),

    # Department bar plot (11)
    html.Div([
        html.Div([
            # Department horizontal bar plot placeholder
            dcc.Graph(
                figure=px.bar(salary_data, x='Deviation', y='Employee', orientation='h', title="11. Department Salary Deviation")
            ),
        ], style={'width': '50%', 'display': 'inline-block'}),

        html.Div([
            # Top employees salary deviation data (10)
            html.H3("10. Top Employees Salary Deviation"),
            html.Div(salary_data[['Employee', 'Deviation']].to_dict('records')),
        ], style={'width': '50%', 'display': 'inline-block'}),
    ], style={'display': 'flex'}),

])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
