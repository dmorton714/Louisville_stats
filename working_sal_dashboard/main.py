import streamlit as st
import pandas as pd
from datetime import datetime
from utils.data_processor import process_salary_data, get_metrics, get_top_deviations
from utils.visualizations import create_gauge_chart, create_department_comparison

# Page config
st.set_page_config(
    page_title="Louisville Metro Salary Tracker",
    page_icon="LMG",
    layout="wide"
)

# Load custom CSS
with open('working_sal_dashboard/assets/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Header
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.markdown("<h1 style='text-align: left; white-space: nowrap;'>Louisville Metro Government Salary Tracker</h1>", unsafe_allow_html=True)

# Load and process data
@st.cache_data
def load_data():
    data = pd.read_csv("data2/salary.csv")
    return process_salary_data(data, datetime.now().strftime("%B %d, %Y"))

try:
    data = load_data()
    
    # Filters
    col1, col2 = st.columns(2)
    with col1:
        selected_year = st.selectbox(
            "Select Year",
            options=sorted(data['CalYear'].unique()),
            index=len(data['CalYear'].unique())-1
        )
    with col2:
        # Filter to only departments with data for the selected year
        year_filtered_data = data[data['CalYear'] == selected_year]
        available_departments = sorted(year_filtered_data['Department'].dropna().unique().tolist())
        department_options = ['All'] + available_departments
        selected_dept = st.selectbox("Select Department", department_options)

    # Filter data based on selections
    filtered_data = data[data['CalYear'] == selected_year]
    if selected_dept != 'All':
        filtered_data = filtered_data[filtered_data['Department'] == selected_dept]

    # Get metrics
    metrics = get_metrics(filtered_data, selected_year)

    # Display metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Salary Spend", f"${metrics['total_spend']:,.2f}")
    with col2:
        st.metric("Salary Budget", f"${metrics['total_budget']:,.2f}")
    with col3:
        st.metric("Budget Variance", f"{metrics['variance_pct']:+.2f}%")

    # Main visualizations
    col1, col2 = st.columns([3, 2])
    with col1:
        st.plotly_chart(
            create_gauge_chart(
                metrics['total_spend'],
                metrics['total_budget'],
                selected_year
            ),
            use_container_width=True
        )
    with col2:
        st.plotly_chart(
            create_department_comparison(filtered_data, selected_year),
            use_container_width=True
        )

    # Top deviations table
    st.subheader("Top Salary Deviations")
    top_dev = get_top_deviations(filtered_data, selected_year)
    st.dataframe(
        top_dev.style.format({
            'YTD_Total': '${:,.2f}',
            'Salary_Total': '${:,.2f}',
            'Annual_Rate': '${:,.2f}',
            'Deviation': '${:,.2f}',
            'Deviation_Pct': '{:,.2f}%'
        }),
        use_container_width=True
    )

except Exception as e:
    st.error(f"An error occurred: {str(e)}")
    st.error("Please check your data source and try again.")
