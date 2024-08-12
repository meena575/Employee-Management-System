

import streamlit as st
import mysql.connector
import pandas as pd
from datetime import datetime
import re

def is_valid_contact_number(contact_number):
    pattern = r"^\d{10}$"
    return bool(re.match(pattern, contact_number))

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def display_employee_dashboard(email_id):
    st.title("Employee Dashboard")
    choice = st.selectbox("Employee Features", ("View Details", "Update Details", "Attendance Records", "Leave Status", "Apply Leave"))
    #email_id = email_id
    mydb = mysql.connector.connect(host="localhost", user="root", password="12345678", database="EMS")
    c = mydb.cursor()

    if choice == "Update Details":
        E_id = st.text_input("Employee ID")
        email = st.text_input("Email ID")
        pwd = st.text_input("Password", type='password')
        c_no = st.text_input("Contact Number")
        address = st.text_input("Address")
        if is_valid_email(email) and E_id != "" and pwd != "" and is_valid_contact_number(c_no) and address != "":
            if st.button("UPDATE"):
                c.execute("UPDATE Employees SET Email=%s, Password=%s, ContactNumber=%s, Address=%s WHERE Employee_ID=%s", (email, pwd, c_no, address, E_id))
                mydb.commit()
                st.write("Updated Successfully")
                st.session_state.email_id = email
        st.write(email_id)

    elif choice == "View Details":
        email_id = st.session_state.email_id
        st.write(email_id)
        c.execute("SELECT e.Employee_Id, e.Email, CONCAT(e.FirstName, ' ', e.LastName) AS FullName, e.Department, e.Date_of_joining, e.Job_Title, e.Salary, e.Role, d.DepartmentName, CONCAT(dh.FirstName, ' ', dh.LastName) AS DepartmentHead FROM Employees e JOIN Departments d ON e.Department = d.DepartmentName JOIN Employees dh ON d.DepartmentHead_ID = dh.Employee_ID WHERE e.Email = %s", (email_id,))
        result = c.fetchall()
        df = pd.DataFrame(result, columns=[column[0] for column in c.description])
        st.write(df)

    elif choice == "Attendance Records":
        c.execute("SELECT a.Attendance_ID, a.Employee_ID, CONCAT(e.FirstName, ' ', e.LastName) AS FullName, a.Date, a.CheckInTime, a.CheckOutTime FROM AttendanceRecords a JOIN Employees e ON a.Employee_ID = e.Employee_ID WHERE Email = %s", (email_id,))
        result = c.fetchall()
        df = pd.DataFrame(result, columns=[column[0] for column in c.description])
        st.write(df)

    elif choice == "Leave Status":
        c.execute("SELECT l.Employee_ID,l.LeaveType,l.LeaveRequest_ID,l.StartDate,l.EndDate,l.Status FROM LeaveRequests l join Employees e on l.Employee_ID=e.Employee_ID  WHERE Email = %s", (email_id,))
        result = c.fetchall()
        df = pd.DataFrame(result, columns=[column[0] for column in c.description])
        st.write(df)
            
    elif choice == "Apply Leave":
        st.title("Leave Request Form")
        E_id = st.text_input("Employee ID")
        leave_type = st.radio("Select Leave Type:", ("Annual Leave", "Sick Leave", "Maternity Leave"))
        start_date = st.date_input("Start Date")
        end_date = st.date_input("End Date")
        btn_apply = st.button("Apply Leave")

        if btn_apply:
            if E_id != "":
                if is_valid_date(str(start_date)):
                    c.execute("INSERT INTO LeaveRequests (Employee_ID, LeaveType, Status, StartDate, EndDate) VALUES (%s, %s, %s, %s, %s)", (E_id, leave_type, "Pending", start_date, end_date))
                    mydb.commit()
                    st.success("Leave request applied successfully.")
                else:
                    st.error("Please enter a valid start date in the format YYYY-MM-DD.")
            else:
                st.warning("Employee ID cannot be empty.")

    c.close()
    mydb.close()


