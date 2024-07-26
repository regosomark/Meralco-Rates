import streamlit as st
import pandas as pd

# Load the Excel file
file_path = 'C:/Users/MARK/Meralco History Rates/Historical MERALCO Schedule of Rates.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')

# Streamlit application
st.title("Excel Data Filter")

# Dropdown for Customer Class
customer_classes = df['Customer Class'].unique().tolist()
selected_class = st.selectbox("Select Customer Class", customer_classes)

# Filter by selected Customer Class
df_class = df[df['Customer Class'] == selected_class]

# Dropdown for Customer Subclass
customer_subclasses = df_class['Customer Subclass'].unique().tolist()
selected_subclass = st.selectbox("Select Customer Subclass", customer_subclasses)

# Filter by selected Customer Subclass
df_subclass = df_class[df_class['Customer Subclass'] == selected_subclass]

# Create Demand Range options
demand_columns = ['Lower Limit Demand', 'Upper Limit Demand', 'Lower Limit Consumption', 'Upper Limit Consumption']
df_subclass['Combined Demand'] = df_subclass[demand_columns].astype(str).agg(' '.join, axis=1)
demands = df_subclass['Combined Demand'].unique().tolist()
selected_demand = st.selectbox("Select Demand Range", demands)

# Filter by selected Demand Range
df_demand = df_subclass[df_subclass['Combined Demand'].str.contains(selected_demand)]

# Dropdown for Supply Period
supply_periods = df_demand['Supply Period'].unique().tolist()
selected_period = st.selectbox("Select Supply Period", supply_periods)

# Filter by selected Supply Period
df_period = df_demand[df_demand['Supply Period'] == selected_period]

# Dropdown for Supply Period Start and End
start_dates = df_period['Supply Period Start'].unique().tolist()
end_dates = df_period['Supply Period End'].unique().tolist()
selected_start = st.selectbox("Select Supply Period Start", start_dates)
selected_end = st.selectbox("Select Supply Period End", end_dates)

# Filter by selected Supply Period Start and End
filtered_df = df_period[
    (df_period['Supply Period Start'] == selected_start) &
    (df_period['Supply Period End'] == selected_end)
]

# Display the filtered table
if st.button("Submit"):
    if not filtered_df.empty:
        st.write("Filtered Data", filtered_df[['Customer Class', 'Customer Subclass', 'Supply Period', 'Supply Period Start', 'Supply Period End', 'Generation Charge kWh', 'Transmission Charge kWh', 'Distribution Charge kWh', 'Transmission Charge kW', 'Distribution Charge kW', 'Total per kW']])
    else:
        st.write("No data available for the selected criteria.")
