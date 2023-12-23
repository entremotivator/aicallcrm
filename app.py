import streamlit as st
import pandas as pd

def add_customer():
    new_name = st.sidebar.text_input("Name", key="new_name")
    new_phone = st.sidebar.text_input("Phone Number", key="new_phone")
    new_notes = st.sidebar.text_area("Notes", key="new_notes")
    investment_type = st.sidebar.selectbox("Investment Type", investment_types, key="investment_type")
    add_customer_button = st.sidebar.button("Add Customer")

    if add_customer_button and new_name != "" and new_phone != "":
        new_customer = pd.DataFrame({
            'Name': [new_name],
            'Phone Number': [new_phone],
            'Notes': [new_notes],
            'Investment Type': [investment_type]
        })
        return new_customer
    return None

def display_customer_info(customer_data):
    st.header("Customer List")
    st.table(customer_data)

    selected_customer = st.selectbox("Select a customer to call", customer_data['Name'])
    call_button = st.button("Call")

    if call_button:
        st.success(f"Calling {selected_customer} at {customer_data.loc[customer_data['Name'] == selected_customer, 'Phone Number'].values[0]}")

    st.header("Notes")
    selected_notes = customer_data.loc[customer_data['Name'] == selected_customer, 'Notes'].values[0]
    updated_notes = st.text_area("Notes", selected_notes, key="updated_notes")
    customer_data.loc[customer_data['Name'] == selected_customer, 'Notes'] = updated_notes

    return selected_customer  # Return selected customer

# Streamlit app layout
st.title("Real Estate Investment CRM")

# Initialize a DataFrame to store customer data
customer_data = pd.DataFrame({
    'Name': ['John Doe', 'Jane Smith', 'Bob Johnson'],
    'Phone Number': ['123-456-7890', '987-654-3210', '555-123-4567'],
    'Notes': ['Interested in buying', 'Call back next week', 'Needs more information'],
    'Investment Type': ['Tired Landlord', 'Foreclosure', 'Land Acquisition']
})

investment_types = ['Tired Landlord', 'Foreclosure', 'Land Acquisition', 'Commercial Property', 'Fix and Flip']

# Initialize selected_customer
selected_customer = ""

# Sidebar for adding new customers
st.sidebar.header("Add New Customer")
new_customer = add_customer()

if new_customer is not None:
    customer_data = pd.concat([customer_data, new_customer], ignore_index=True)
    st.sidebar.success("Customer added successfully!")

# Main content area
selected_customer = display_customer_info(customer_data)  # Update selected_customer

# Investment Type-specific call script
st.sidebar.header("Investment Type-specific Call Script")

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
    """
}

# Check if selected_customer is not empty before using it
if selected_customer:
    selected_investment_type = customer_data.loc[customer_data['Name'] == selected_customer, 'Investment Type'].values[0]
    investment_script = investment_type_script_mapping.get(selected_investment_type, "")
    customized_script = st.sidebar.text_area("Script", investment_script, key="customized_script")

# Run the app
