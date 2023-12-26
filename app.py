# Import necessary libraries
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Set page configuration for a wider layout
st.set_page_config(
    page_title="Real Estate Investment CRM",
    page_icon="🏠",
    layout="wide",
)

# Sample data for investment types and revenue
investment_revenue_data = pd.DataFrame({
    'Investment Type': ['Tired Landlord', 'Foreclosure', 'Land Acquisition', 'Commercial Property', 'Fix and Flip'],
    'Revenue': [150000, 80000, 200000, 300000, 120000]
})

# Investment type script mapping (replace with actual scripts)
investment_type_script_mapping = {
    'Tired Landlord': "Script for Tired Landlord",
    'Foreclosure': "Script for Foreclosure",
    'Land Acquisition': "Script for Land Acquisition",
    'Commercial Property': "Script for Commercial Property",
    'Fix and Flip': "Script for Fix and Flip"
}

# Function to add/edit investment types
def add_edit_investment_types():
    st.header("Add/Edit Investment Types")

    # Display existing investment types and revenue
    st.subheader("Existing Investment Types and Revenue")
    st.table(investment_revenue_data)

    # Input fields for adding/editing investment types
    new_investment_type = st.text_input("New Investment Type", key="new_investment_type")
    new_revenue = st.number_input("Revenue ($)", min_value=0, key="new_revenue")

    add_investment_type_button = st.button("Add/Edit Investment Type")

    if add_investment_type_button and new_investment_type != "":
        # Check if the investment type already exists
        if new_investment_type in investment_revenue_data['Investment Type'].values:
            # Update the revenue for the existing investment type
            investment_revenue_data.loc[investment_revenue_data['Investment Type'] == new_investment_type, 'Revenue'] = new_revenue
            st.success(f"Updated revenue for {new_investment_type}")
        else:
            # Add a new investment type
            new_investment = pd.DataFrame({
                'Investment Type': [new_investment_type],
                'Revenue': [new_revenue]
            })
            investment_revenue_data = pd.concat([investment_revenue_data, new_investment], ignore_index=True)
            st.success(f"Added new investment type: {new_investment_type}")

# Streamlit app layout
st.title("Real Estate Investment CRM")

# Initialize a DataFrame to store customer data
customer_data = pd.DataFrame({
    'Name': ['John Doe', 'Jane Smith', 'Bob Johnson'],
    'Phone Number': ['123-456-7890', '987-654-3210', '555-123-4567'],
    'Email': ['john@example.com', 'jane@example.com', 'bob@example.com'],
    'Address': ['123 Main St', '456 Oak St', '789 Pine St'],
    'Company': ['ABC Corp', 'XYZ Inc', '123 Industries'],
    'Preferred Contact Method': ['Phone', 'Email', 'Phone'],
    'Notes': ['Interested in buying', 'Call back next week', 'Needs more information'],
    'Investment Type': ['Tired Landlord', 'Foreclosure', 'Land Acquisition'],
    'Budget': [100000, 50000, 200000],
    'Preferred Location': ['City', 'Suburb', 'Rural'],
    'Follow-up Reminder': [True, False, True],
    'Follow-up Date': [datetime.now() + timedelta(days=7), None, datetime.now() + timedelta(days=5)],
    'Lead Source': ['Website', 'Referral', 'Advertisement'],
    'Last Interaction Date': [datetime.now() - timedelta(days=10), datetime.now() - timedelta(days=5), datetime.now() - timedelta(days=3)],
    'Interested in Newsletter': [True, True, False],
    'Contact Status': ['New', 'Active', 'Closed'],
    'Preferred Contact Days': ['Monday, Wednesday, Friday', 'Tuesday, Thursday', 'Monday, Tuesday'],
    'Satisfaction Level': [8, 6, 9]
})

investment_types = ['Tired Landlord', 'Foreclosure', 'Land Acquisition', 'Commercial Property', 'Fix and Flip']

# Initialize selected_customer
selected_customer = ""

# Sidebar for adding new customers
st.sidebar.header("Add New Customer")
new_customer = add_customer_sidebar()

if new_customer is not None:
    customer_data = pd.concat([customer_data, new_customer], ignore_index=True)
    st.sidebar.success("Customer added successfully!")

# Sidebar for adding/editing investment types
st.sidebar.header("Manage Investment Types")
add_edit_investment_types()

# Main content area
selected_customer = display_customer_info_main(customer_data)  # Update selected_customer

# Display Investment Type-specific call script on the main content area
st.header("Investment Type-specific Call Script")
display_investment_type_script(selected_customer, customer_data)

# Additional features
display_additional_features_sidebar(customer_data)

# Run the app
