import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Set page configuration for a wider layout
st.set_page_config(
    page_title="Real Estate Investment CRM",
    page_icon="🏠",
    layout="wide",
)

# Sample data for investment types, revenue, and call scripts
investment_data = pd.DataFrame({
    'Investment Type': ['Tired Landlord', 'Foreclosure', 'Land Acquisition', 'Commercial Property', 'Fix and Flip',
                        'Residential Rental', 'Vacant Land Development', 'Real Estate Crowdfunding', 'Wholesaling',
                        'Commercial Lease'],
    'Revenue': [150000, 80000, 200000, 300000, 120000,
                100000, 250000, 180000, 90000, 220000],
    'Call Script': [
        "Hello, this is [Your Name] from XYZ Real Estate. I noticed you have a property listed for a while. Are you tired of managing it?",
        "Hi, I'm calling about your property in foreclosure. We specialize in helping homeowners navigate these situations.",
        "Good day! We are interested in acquiring land for development. Do you have any available properties?",
        "Hello, this is [Your Name] from ABC Commercial Realty. We have excellent opportunities for commercial property investment.",
        "Hi, I'm calling regarding your interest in fix and flip properties. We have some great opportunities for you.",
        "Greetings! We specialize in residential rentals. Are you looking for a reliable tenant for your property?",
        "Hello, we are interested in vacant land development. Do you have any land parcels available for sale?",
        "Hi, I'm calling from Real Estate Crowdfunding. We have exciting investment opportunities. Would you like to learn more?",
        "Good day! We are interested in wholesaling real estate. Do you have properties available for wholesale?",
        "Hello, this is [Your Name] from Commercial Lease Solutions. We can assist you in finding the perfect commercial space."
    ]
})

# Function to add/edit investment types
def add_edit_investment_types():
    st.header("Manage Investment Types")

    # Display existing investment types, revenue, and call scripts
    st.subheader("Existing Investment Types, Revenue, and Call Scripts")
    st.table(investment_data)

    # Input fields for adding/editing investment types
    new_investment_type = st.text_input("New Investment Type", key="new_investment_type")
    new_revenue = st.number_input("Revenue ($)", min_value=0, key="new_revenue")
    new_call_script = st.text_area("Call Script", key="new_call_script")

    add_investment_type_button = st.button("Add/Edit Investment Type")

    if add_investment_type_button and new_investment_type != "":
        # Check if the investment type already exists
        if new_investment_type in investment_data['Investment Type'].values:
            # Update the revenue and call script for the existing investment type
            investment_data.loc[investment_data['Investment Type'] == new_investment_type, 'Revenue'] = new_revenue
            investment_data.loc[investment_data['Investment Type'] == new_investment_type, 'Call Script'] = new_call_script
            st.success(f"Updated information for {new_investment_type}")
        else:
            # Add a new investment type
            new_investment = pd.DataFrame({
                'Investment Type': [new_investment_type],
                'Revenue': [new_revenue],
                'Call Script': [new_call_script]
            })
            investment_data = pd.concat([investment_data, new_investment], ignore_index=True)
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

# Add more investment types
investment_types = list(investment_data['Investment Type'])

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
selected_investment_type = customer_data.loc[customer_data['Name'] == selected_customer, 'Investment Type'].values[0]
selected_call_script = investment_data.loc[investment_data['Investment Type'] == selected_investment_type, 'Call Script'].values[0]
updated_call_script = st.text_area("Call Script", selected_call_script, key="updated_call_script")
investment_data.loc[investment_data['Investment Type'] == selected_investment_type, 'Call Script'] = updated_call_script

# Additional features
display_additional_features_sidebar(customer_data)

# Run the app
