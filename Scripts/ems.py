import streamlit as st
import streamlit.components.v1 as stc
import base64
import re
valid_username = "meena123@gmail.com"
valid_password = "password"
# Define session state class
class SessionState:
    def __init__(self):
        self.logged_in = False

# Initialize session state
session_state = SessionState()

# Custom CSS styling for the sidebar
sidebar_style = """
.sidebar .sidebar-content {
    background-color: #f0f2f6;
    padding-top: 50px;
    padding-bottom: 50px;
}
"""

# Apply custom CSS styling
stc.html(sidebar_style)

# Function to add sidebar image
def sidebar_image(image, caption):
    st.sidebar.image(image, caption=caption, use_column_width=True)

# Function to add sidebar components
def sidebar_components():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Login", "Employee"])
    return page

# Function to display login page
def login_page():
    st.title("Login Page")
    email = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if is_valid_email(email) and email==valid_username:
            if password==valid_password:
                session_state.logged_in = True
                st.success("Logged in successfully!")
                st.write(session_state.logged_in)
            
            else:
                st.error("Invalid username or password")
        else:
            st.error("Invalid username or password")
# Function to display employee page
def employee_page():
    st.title("Employee Page")
    st.write("Welcome to the employee page.")


def is_valid_email(email):
    # Define a regular expression pattern for email validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    # Use the re.match function to check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False



if __name__ == "__main__":
    # Load sidebar image
    image="https://as2.ftcdn.net/v2/jpg/02/40/77/87/1000_F_240778787_MCHAVaEKiDZcMmMsgElqSiGmgXrQ2l7F.jpg"
    image_width=150
    st.sidebar.markdown(
        f'<div style="text-align: center;">'
        f'<img src="{image}" style="width: {image_width}px; vertical-align: top;">'
        '</div>',
        unsafe_allow_html=True
    )
    # Get selected page from sidebar
    selected_page = sidebar_components()

    # Display selected page
    if selected_page == "Login":
        login_page()
    elif selected_page == "Employee":
        if session_state.logged_in:
            employee_page()
        else:
            st.error("You need to login first.")
