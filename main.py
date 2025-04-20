import streamlit as st
import pandas as pd
import plotly.express as px
import json
import os

# Set the default page configuration for the Streamlit app
st.set_page_config(page_title="Simple Finance App", page_icon="💰", layout="wide")

# Define the filename for storing category mappings
category_file = "categories.json"

# Initialize the 'categories' in the session state if it doesn't exist
if "categories" not in st.session_state:
    st.session_state.categories = {
        "Uncategorized": [],
    }

# Load existing categories from the JSON file if it exists
if os.path.exists(category_file):
    with open(category_file, "r") as f:
        st.session_state.categories = json.load(f)

# Function to save the current state of categories to the JSON file
def save_categories():
    with open(category_file, "w") as f:
        json.dump(st.session_state.categories, f, indent=4) # Added indent for better readability

# Function to categorize transactions based on keywords in the 'Details' column
def categorize_transactions(df):
    # Initialize a 'Category' column with 'Uncategorized' for all transactions
    df["Category"] = "Uncategorized"

    # Iterate through the defined categories and their associated keywords
    for category, keywords in st.session_state.categories.items():
        # Skip the 'Uncategorized' category or categories with no keywords
        if category == "Uncategorized" or not keywords:
            continue

        # Convert keywords to lowercase and remove leading/trailing whitespace for case-insensitive matching
        lowered_keywords = [keyword.lower().strip() for keyword in keywords]

        # Iterate through each row of the DataFrame
        for idx, row in df.iterrows():
            # Convert the transaction 'Details' to lowercase and remove leading/trailing whitespace
            details = row["Details"].lower().strip()
            # Check if the transaction 'Details' matches any of the keywords for the current category
            if details in lowered_keywords:
                # Assign the current category to the transaction
                df.at[idx, "Category"] = category

    return df

# Function to load transactions from a CSV file
def load_transactions(file):
    try:
        # Read the CSV file into a Pandas DataFrame
        df = pd.read_csv(file)
        # Strip any leading/trailing whitespace from column names
        df.columns = [col.strip() for col in df.columns]
        # Clean and convert the 'Amount' column to numeric, handling commas
        df["Amount"] = df["Amount"].str.replace(",", "").astype(float)
        # Convert the 'Date' column to datetime objects with the specified format
        df["Date"] = pd.to_datetime(df["Date"], format="%d %b %Y")

        # Categorize the loaded transactions
        return categorize_transactions(df)
    except Exception as e:
        # Display an error message if there's an issue processing the file
        st.error(f"Error processing file: {str(e)}")
        return None

# Function to add a new keyword to a specific category
def add_keyword_to_category(category, keyword):
    # Remove leading/trailing whitespace from the keyword
    keyword = keyword.strip()
    # Check if the keyword is not empty and not already in the category's keyword list
    if keyword and keyword not in st.session_state.categories[category]:
        # Add the new keyword to the category
        st.session_state.categories[category].append(keyword)
        # Save the updated categories to the JSON file
        save_categories()
        return True # Indicate that the keyword was successfully added

    return False # Indicate that the keyword was not added (either empty or already exists)

# Main function to run the Streamlit application
def main():
    # Set the title of the application
    st.title("Simple Finance Dashboard")

    # File uploader widget to allow users to upload their transaction CSV file
    uploaded_file = st.file_uploader("Upload your transaction CSV file", type=["csv"])

    # Process the uploaded file if one is provided
    if uploaded_file is not None:
        # Load and categorize transactions from the uploaded file
        df = load_transactions(uploaded_file)

        # If the DataFrame was loaded successfully
        if df is not None:
            # Separate debit (expenses) and credit (payments) transactions
            debits_df = df[df["Debit/Credit"] == "Debit"].copy()
            credits_df = df[df["Debit/Credit"] == "Credit"].copy()

            # Store the debits DataFrame in the session state for potential modifications
            st.session_state.debits_df = debits_df.copy()

            # Create two tabs for displaying expenses and payments
            tab1, tab2 = st.tabs(["Expenses (Debits)", "Payments (Credits)"])
            with tab1:
                # Input field for adding a new expense category
                new_category = st.text_input("New Category Name")
                # Button to add the new category
                add_button = st.button("Add Category")

                # Handle the addition of a new category
                if add_button and new_category:
                    if new_category not in st.session_state.categories:
                        st.session_state.categories[new_category] = []
                        save_categories()
                        st.rerun() # Rerun the app to update the category list in the selectbox

                # Display the expenses DataFrame with editing capabilities
                st.subheader("Your Expenses")
                edited_df = st.data_editor(
                    st.session_state.debits_df[["Date", "Details", "Amount", "Category"]],
                    column_config={
                        "Date": st.column_config.DateColumn("Date", format="DD/MM/YYYY"),
                        "Amount": st.column_config.NumberColumn("Amount", format="%.2f AED"),
                        "Category": st.column_config.SelectboxColumn(
                            "Category",
                            options=list(st.session_state.categories.keys())
                        )
                    },
                    hide_index=True,
                    use_container_width=True,
                    key="category_editor" # Unique key for the data editor widget
                )

                # Button to apply changes made in the data editor
                save_button = st.button("Apply Changes", type="primary")
                if save_button:
                    # Iterate through the edited DataFrame to update categories and keywords
                    for idx, row in edited_df.iterrows():
                        new_category = row["Category"]
                        # Check if the category has been changed
                        if new_category == st.session_state.debits_df.at[idx, "Category"]:
                            continue # Skip if the category is the same

                        details = row["Details"]
                        # Update the category in the session state's DataFrame
                        st.session_state.debits_df.at[idx, "Category"] = new_category
                        # Add the transaction detail as a keyword to the new category
                        add_keyword_to_category(new_category, details)

                    # Optionally, you could add a success message here
                    st.success("Changes applied!")

                # Display the expense summary by category
                st.subheader('Expense Summary')
                category_totals = st.session_state.debits_df.groupby("Category")["Amount"].sum().reset_index()
                category_totals = category_totals.sort_values("Amount", ascending=False)

                # Display the category-wise expense totals in a DataFrame
                st.dataframe(
                    category_totals,
                    column_config={
                        "Amount": st.column_config.NumberColumn("Amount", format="%.2f AED")
                    },
                    use_container_width=True,
                    hide_index=True
                )

                # Create and display a pie chart of expenses by category
                fig = px.pie(
                    category_totals,
                    values="Amount",
                    names="Category",
                    title="Expenses by Category"
                )
                st.plotly_chart(fig, use_container_width=True)

            with tab2:
                # Display the payments summary
                st.subheader("Payments Summary")
                total_payments = credits_df["Amount"].sum()
                st.metric("Total Payments", f"{total_payments:,.2f} AED")
                # Display the raw payments DataFrame
                st.write(credits_df)

# Run the main function when the script is executed
if __name__ == "__main__":
    main()