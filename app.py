import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Define investment_types before using it in the add_customer_sidebar function
investment_types = ['Tired Landlord', 'Foreclosure', 'Land Acquisition', 'Commercial Property', 'Fix and Flip',
                    'Residential Rental', 'Vacation Property', 'Real Estate Crowdfunding', 'Wholesaling', 'Real Estate Development']

# Set page configuration for a wider layout
st.set_page_config(
    page_title="Real Estate Investment CRM",
    page_icon="🏠",
    layout="wide",
)

def add_customer_sidebar():
    new_name = st.sidebar.text_input("Name", key="new_name")
    new_phone = st.sidebar.text_input("Phone Number", key="new_phone")
    new_email = st.sidebar.text_input("Email", key="new_email")
    new_address = st.sidebar.text_area("Address", key="new_address")
    new_company = st.sidebar.text_input("Company", key="new_company")
    preferred_contact_method = st.sidebar.radio("Preferred Contact Method", ["Phone", "Email"], key="preferred_contact_method")
    new_notes = st.sidebar.text_area("Notes", key="new_notes")
    investment_type = st.sidebar.selectbox("Investment Type", investment_types, key="investment_type")
    budget = st.sidebar.number_input("Budget ($)", min_value=0, key="budget")
    preferred_location = st.sidebar.text_input("Preferred Location", key="preferred_location")
    follow_up_reminder = st.sidebar.checkbox("Set Follow-up Reminder", key="follow_up_reminder")

    if follow_up_reminder:
        follow_up_date = st.sidebar.date_input("Follow-up Date", datetime.now() + timedelta(days=7), key="follow_up_date")
    else:
        follow_up_date = None

    lead_source = st.sidebar.text_input("Lead Source", key="lead_source")
    last_interaction_date = st.sidebar.date_input("Last Interaction Date", key="last_interaction_date")
    interested_in_newsletter = st.sidebar.checkbox("Interested in Newsletter", key="interested_in_newsletter")

    # Additional Fields
    contact_status = st.sidebar.selectbox("Contact Status", ["New", "Active", "Closed"], key="contact_status")
    preferred_contact_days = st.sidebar.multiselect("Preferred Contact Days", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], key="preferred_contact_days")
    satisfaction_level = st.sidebar.slider("Satisfaction Level", min_value=0, max_value=10, step=1, key="satisfaction_level")

    add_customer_button = st.sidebar.button("Add Customer")

    if add_customer_button and new_name != "" and new_phone != "":
        new_customer = pd.DataFrame({
            'Name': [new_name],
            'Phone Number': [new_phone],
            'Email': [new_email],
            'Address': [new_address],
            'Company': [new_company],
            'Preferred Contact Method': [preferred_contact_method],
            'Notes': [new_notes],
            'Investment Type': [investment_type],
            'Budget': [budget],
            'Preferred Location': [preferred_location],
            'Follow-up Reminder': [follow_up_reminder],
            'Follow-up Date': [follow_up_date],
            'Lead Source': [lead_source],
            'Last Interaction Date': [last_interaction_date],
            'Interested in Newsletter': [interested_in_newsletter],
            'Contact Status': [contact_status],
            'Preferred Contact Days': [", ".join(preferred_contact_days)],
            'Satisfaction Level': [satisfaction_level]
        })
        return new_customer
    return None

def display_customer_info_main(customer_data):
    st.header("Customer List")
    st.table(customer_data)

    selected_customer = st.selectbox("Select a customer to call", customer_data['Name'])
    call_button = st.button("Call")

    if call_button:
        st.success(f"Calling {selected_customer} at {customer_data.loc[customer_data['Name'] == selected_customer, 'Phone Number'].values[0]}")

    st.header("Customer Details")
    selected_customer_data = customer_data.loc[customer_data['Name'] == selected_customer]
    st.write(selected_customer_data)

    st.header("Notes")
    selected_notes = customer_data.loc[customer_data['Name'] == selected_customer, 'Notes'].values[0]
    updated_notes = st.text_area("Notes", selected_notes, key="updated_notes")
    customer_data.loc[customer_data['Name'] == selected_customer, 'Notes'] = updated_notes

    return selected_customer  # Return selected customer

def display_investment_type_script(selected_customer, customer_data):
    selected_investment_type = customer_data.loc[customer_data['Name'] == selected_customer, 'Investment Type'].values[0]
    investment_script = investment_type_script_mapping.get(selected_investment_type, "")
    st.text_area("Script", investment_script, key="customized_script")

def display_additional_features_sidebar(customer_data):
    st.sidebar.header("Additional Features")
    # Additional features go here
    # ...

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

# Main content area
selected_customer = display_customer_info_main(customer_data)  # Update selected_customer

# Display Investment Type-specific call script on the main content area
st.header("Investment Type-specific Call Script")
display_investment_type_script(selected_customer, customer_data)
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

# Additional features
display_additional_features_sidebar(customer_data)

# Run the app
