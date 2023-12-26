import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Set page configuration for a wider layout
st.set_page_config(
    page_title="Real Estate Investment CRM",
    page_icon="🏠",
    layout="wide",
)

# Initialize selected_customer
selected_customer = ""

# Investment Type-specific call scripts
investment_type_script_mapping = {
    'Tired Landlord': """
    Hello [Customer Name],

    This is [Your Name] from XYZ Real Estate. I understand that being a landlord can be demanding, and I'm reaching out because we specialize in helping tired landlords like yourself.

    [Customized Content for Tired Landlords]

    Could we schedule a brief meeting to discuss your specific situation?

    Thank you for considering us as a partner in your real estate journey.

    Best regards,
    [Your Name]
    """,
    'Foreclosure': """
    Hello [Customer Name],

    This is [Your Name] from XYZ Real Estate. I hope this call finds you well despite the challenging circumstances.

    [Customized Content for Foreclosure Opportunities]

    Are you open to exploring investment opportunities related to foreclosures? I'd love to hear your thoughts.

    Thank you for your time.

    Best regards,
    [Your Name]
    """,
    'Land Acquisition': """
    Hello [Customer Name],

    This is [Your Name] from XYZ Real Estate. We are currently looking for strategic partners interested in land acquisition opportunities.

    [Customized Content for Land Acquisition]

    Could we schedule a meeting to explore potential opportunities in land acquisition?

    Thank you for your time and consideration.

    Best regards,
    [Your Name]
    """,
    'Commercial Property': """
    Hello [Customer Name],

    This is [Your Name] from XYZ Real Estate. Our team is actively involved in commercial real estate ventures, and we are reaching out to potential partners like you.

    [Customized Content for Commercial Property]

    Would you be interested in discussing commercial property investment opportunities further?

    Thank you for your time.

    Best regards,
    [Your Name]
    """,
    'Fix and Flip': """
    Hello [Customer Name],

    This is [Your Name] from XYZ Real Estate. We specialize in fix and flip projects and are looking for individuals interested in participating in these exciting ventures.

    [Customized Content for Fix and Flip]

    Could we schedule a meeting to explore how you can be part of our fix and flip projects?

    Thank you for your time and consideration.

    Best regards,
    [Your Name]
    """,
    'Residential Rental': """
    Hello [Customer Name],

    This is [Your Name] from XYZ Real Estate. With the growing demand for rental properties, we're reaching out to individuals interested in residential rental investments.

    [Customized Content for Residential Rentals]

    Let's discuss how you can benefit from the lucrative residential rental market.

    Thank you for your time.

    Best regards,
    [Your Name]
    """,
    'Vacation Property': """
    Hello [Customer Name],

    This is [Your Name] from XYZ Real Estate. Are you interested in investing in a vacation property for both personal enjoyment and potential income?

    [Customized Content for Vacation Property Investments]

    Let's explore the possibilities and find the perfect vacation property for you.

    Thank you for your time.

    Best regards,
    [Your Name]
    """,
    'Real Estate Crowdfunding': """
    Hello [Customer Name],

    This is [Your Name] from XYZ Real Estate. Real estate crowdfunding is gaining popularity as a way to invest in properties collectively.

    [Customized Content for Real Estate Crowdfunding]

    Would you like to learn more about this innovative investment approach?

    Thank you for your time.

    Best regards,
    [Your Name]
    """,
    'Wholesaling': """
    Hello [Customer Name],

    This is [Your Name] from XYZ Real Estate. Wholesaling involves finding great real estate deals and passing them on to other investors for a fee.

    [Customized Content for Wholesaling Opportunities]

    Let's discuss how you can participate in the wholesaling process.

    Thank you for your time.

    Best regards,
    [Your Name]
    """,
    'Real Estate Development': """
    Hello [Customer Name],

    This is [Your Name] from XYZ Real Estate. Real estate development offers the opportunity to create new properties and transform communities.

    [Customized Content for Real Estate Development]

    Could we explore how you can get involved in exciting development projects?

    Thank you for your time.

    Best regards,
    [Your Name]
    """
}

investment_types = ['Tired Landlord', 'Foreclosure', 'Land Acquisition', 'Commercial Property', 'Fix and Flip',
                    'Residential Rental', 'Vacation Property', 'Real Estate Crowdfunding', 'Wholesaling', 'Real Estate Development']

def add_customer_sidebar():
    # ... (same as before)

def display_customer_info_main(customer_data):
    # ... (same as before)

def display_investment_type_script(selected_customer, customer_data):
    # ... (same as before)

def display_additional_features_sidebar(customer_data):
    # ... (same as before)

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
    'Investment Type': ['Tired Landlord', 'Foreclosure', 'Land Acquisition', 'Commercial Property', 'Fix and Flip',
                        'Residential Rental', 'Vacation Property', 'Real Estate Crowdfunding', 'Wholesaling', 'Real Estate Development'],
    'Budget': [100000, 50000, 200000, 300000, 150000, 120000, 250000, 50000, 75000, 400000],
    'Preferred Location': ['City', 'Suburb', 'Rural', 'Urban', 'Coastal', 'Mountainous', 'Island', 'Countryside', 'Downtown', 'Industrial'],
    'Follow-up Reminder': [True, False, True, False, True, False, True, False, True, False],
    'Follow-up Date': [datetime.now() + timedelta(days=7), None, datetime.now() + timedelta(days=5),
                       datetime.now() + timedelta(days=10), None, datetime.now() + timedelta(days=3),
                       datetime.now() + timedelta(days=8), None, datetime.now() + timedelta(days=6),
                       None],
    'Lead Source': ['Website', 'Referral', 'Advertisement', 'Social Media', 'Event', 'Cold Call', 'Networking', 'Online Listing', 'Direct Mail', 'Walk-in'],
    'Last Interaction Date': [datetime.now() - timedelta(days=10), datetime.now() - timedelta(days=5), datetime.now() - timedelta(days=3),
                              datetime.now() - timedelta(days=7), datetime.now() - timedelta(days=12), datetime.now() - timedelta(days=6),
                              datetime.now() - timedelta(days=4), datetime.now() - timedelta(days=8), datetime.now() - timedelta(days=5),
                              datetime.now() - timedelta(days=9)],
    'Interested in Newsletter': [True, True, False, True, False, True, False, True, False, True],
    'Contact Status': ['New', 'Active', 'Closed', 'New', 'Active', 'Closed', 'New', 'Active', 'Closed', 'New'],
    'Preferred Contact Days': [['Monday', 'Wednesday', 'Friday'], ['Tuesday', 'Thursday'], ['Monday', 'Tuesday'],
                              ['Wednesday', 'Thursday', 'Friday'], ['Monday', 'Wednesday', 'Thursday'],
                              ['Tuesday', 'Friday'], ['Monday', 'Wednesday'], ['Tuesday', 'Thursday', 'Friday'],
                              ['Monday', 'Tuesday', 'Thursday'], ['Wednesday', 'Thursday']],
    'Satisfaction Level': [8, 6, 9, 7, 8, 5, 9, 6, 7, 8]
})

# Sidebar for adding new customers
st.sidebar.header("Add New Customer")
new_customer = add_customer_sidebar()

if new_customer is not None:
    customer_data = pd.concat([customer_data, new_customer], ignore_index=True)
    st.sidebar.success("Customer added successfully!")

# Main content area
selected_customer = display_customer_info_main(customer_data)  # Update selected_customer

# Display Investment Type-specific call script on the main content area
st.header("Investment Type-specific Call Script")
display_investment_type_script(selected_customer, customer_data)

# Additional features
display_additional_features_sidebar(customer_data)

# Call System
st.sidebar.header("Call System")
call_button = st.sidebar.button("Initiate Call System")

if call_button:
    st.success("Call system initiated. Dialing numbers...")

# Run the app
