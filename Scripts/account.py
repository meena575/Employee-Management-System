import streamlit as st
import mysql.connector
import pandas as pd
import re

from streamlit_option_menu import option_menu
from employee import display_employee_dashboard
from admin import display_admin_dashboard
from department import display_department_dashboard
def app1():
    """
    Main function for user authentication and login.

    This function handles user authentication based on the selected user type (Employee, Department Head, Admin).
    If the user is authenticated successfully, it displays the respective dashboard.
    """
    if 'email_id' not in st.session_state:  
        st.session_state.email_id = None
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'department' not in st.session_state:  
        st.session_state.department = None
    login_type = st.radio("Select User Type", ['Employee', 'Department Head', "Admin"])

    if st.session_state.logged_in:
        if login_type == "Employee":
            display_employee_dashboard(st.session_state.email_id)
        elif login_type == "Department Head":
            display_department_dashboard(st.session_state.email_id,st.session_state.department)
        elif login_type == "Admin":
            display_admin_dashboard()
        
        if st.button("Logout"):
            st.session_state.logged_in = False
    else:
        if login_type == "Employee":
            st.write("Employee Login Page:")
            # Employee login logic here
            email_id = st.text_input("Email ID") 
            pwd = st.text_input("Password", type="password")
            btn = st.button("Login")

            if btn:
                mydb = mysql.connector.connect(host="localhost", user="root", password="12345678", database="EMS")
                c = mydb.cursor()
                c.execute("SELECT Email, Password FROM Employees")
                for (email, password) in c:
                    if is_valid_email(email_id) and email_id == email:
                        if pwd == password:
                            st.session_state.logged_in = True
                            st.session_state.email_id=email_id
                            
                            st.success("Logged in successfully!")
                            
                            break
                        else:
                            st.error("Invalid username or password")
                            break
                else:
                    st.error("Invalid username or password")
        elif login_type == "Department Head":
            #st.write("Department Head Login Page:")
            st.write("<h2>Department Head Login Page:</h2>", unsafe_allow_html=True)
            # Department Head login logic here
            
            email_id = st.text_input("Email ID") 
            pwd = st.text_input("Password", type="password")
            btn = st.button("Login")

            if btn:
                mydb = mysql.connector.connect(host="localhost", user="root", password="12345678", database="EMS")
                c = mydb.cursor()
                c.execute("SELECT Email , Password,Department FROM Employees INNER JOIN Departments ON Employee_ID=DepartmentHead_ID where role='Head'")
                for (email, password,Department) in c:
                    if is_valid_email(email_id) and email_id == email:
                        if pwd == password:
                            st.session_state.logged_in = True
                            st.session_state.email_id=email_id
                            st.session_state.department = Department
                            st.success("Logged in successfully!")
                            break
                        else:
                            st.error("Invalid username or password")
                            break
                else:
                    st.error("Invalid username or password")
        elif login_type == "Admin":
            #st.write("Admin Login Page")
            st.write("<h2>Admin Login Page</h2>", unsafe_allow_html=True)
            # Admin  login logic here
            email_id = st.text_input("Email ID") 
            pwd = st.text_input("Password", type="password")
            btn = st.button("Login")

            if btn:
                mydb = mysql.connector.connect(host="localhost", user="root", password="12345678", database="EMS")
                c = mydb.cursor()
                c.execute("SELECT Email , Password FROM Employees WHERE Role='Admin'")
                for (email, password) in c:
                    if is_valid_email(email_id) and email_id == email:
                        if pwd == password:
                            st.session_state.logged_in = True
                            st.success("Logged in successfully!")
                            break
                        else:
                            st.error("Invalid username or password")
                            break
                else:
                    st.error("Invalid username or password")

        if st.session_state.logged_in:
            if login_type == "Employee":
                display_employee_dashboard(st.session_state.email_id)
            elif login_type == "Department Head":
                display_department_dashboard(st.session_state.email_id,st.session_state.department)
            elif login_type == "Admin":
                display_admin_dashboard()

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False


