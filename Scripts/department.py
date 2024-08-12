import streamlit as st
import mysql.connector
import pandas as pd
from datetime import datetime
import re

def display_department_dashboard(email_id, department):
    st.title("Department Dashboard")
    st.write(f"Welcome, {department} Department Head!")

    choice = st.selectbox("Department Head Features", ["Leave Approval", "Performance Evaluation", "Training and Development"])

    if choice == "Leave Approval":
        display_leave_approval(email_id, department)
    elif choice == "Performance Evaluation":
        display_performance_evaluation(email_id, department)
    elif choice == "Training and Development":
        display_training_sessions()


def display_leave_approval(email_id, department):
    st.header("Leave Approval")

    pending_leave_requests = get_pending_leave_requests(department)

    if pending_leave_requests:
        st.subheader("Pending Leave Requests:")
        leave_requests_df = pd.DataFrame(pending_leave_requests, columns=["Employee ID", "Leave Request ID", "EmployeeName","Leave Type", "Start Date", "End Date", "Status"])
        st.dataframe(leave_requests_df)

        for index, row in leave_requests_df.iterrows():
            leave_request_id = row["Leave Request ID"]
            if st.button(f"Approve Leave Request {leave_request_id}"):
                approve_leave_request(leave_request_id)
                st.success(f"Leave Request {leave_request_id} Approved!")

            if st.button(f"Reject Leave Request {leave_request_id}"):
                reject_leave_request(leave_request_id)
                st.warning(f"Leave Request {leave_request_id} Rejected.")
    else:
        st.write("No pending leave requests for your department.")


def confirm_action(action):
    confirmed = st.sidebar.checkbox(f"Confirm {action} Action")
    if not confirmed:
        st.warning(f"Please confirm the {action} action.")
    return confirmed

def get_pending_leave_requests(department_name):
    mydb = mysql.connector.connect(host="localhost", user="root", password="12345678", database="EMS")
    c = mydb.cursor()
    c.execute("SELECT l.Employee_ID,l.LeaveRequest_ID, CONCAT(e.FirstName, ' ', e.LastName) AS EmployeeName, l.LeaveType, l.StartDate, l.EndDate, l.Status FROM Employees e JOIN LeaveRequests l ON e.Employee_ID = l.Employee_ID WHERE e.Department = %s AND l.Status = 'Pending'", (department_name,))
    return c.fetchall()

def get_employee_name(employee_id):
    mydb = mysql.connector.connect(host="localhost", user="root", password="12345678", database="EMS")
    c = mydb.cursor()
    c.execute("SELECT CONCAT(FirstName, ' ', LastName) AS EmployeeName FROM Employees WHERE Employee_ID = %s", (employee_id,))
    result = c.fetchone()
    return result[0] if result else ""

def approve_leave_request(leave_request_id):
    mydb = mysql.connector.connect(host="localhost", user="root", password="12345678", database="EMS")
    c = mydb.cursor()
    c.execute("UPDATE LeaveRequests SET Status = 'Approved' WHERE LeaveRequest_ID = %s", (leave_request_id,))
    mydb.commit()

def reject_leave_request(leave_request_id):
    mydb = mysql.connector.connect(host="localhost", user="root", password="12345678", database="EMS")
    c = mydb.cursor()
    c.execute("UPDATE LeaveRequests SET Status = 'Rejected' WHERE LeaveRequest_ID = %s", (leave_request_id,))
    mydb.commit()


def display_performance_evaluation(email_id, department):
    st.header("Performance Evaluation")
    
    # Retrieve employee data for the department
    employee_data = get_employee_data(department)
    
    if employee_data is not None:
        # Display the employee data
        st.dataframe(employee_data)
        
        # Allow department head to submit performance evaluations
        st.title("Performance Evaluation")

    # Employee ID
        employee_id = st.text_input("Employee ID")

        # Evaluation Date
        evaluation_date = st.date_input("Evaluation Date", value=datetime.today())

        # Performance metrics
        productivity = st.slider("Productivity", min_value=1, max_value=10)
        teamwork = st.slider("Teamwork", min_value=1, max_value=10)
        communication = st.slider("Communication Skills", min_value=1, max_value=10)
        problem_solving = st.slider("Problem Solving", min_value=1, max_value=10)
        quality_of_work = st.slider("Quality of Work", min_value=1, max_value=10)
        attendance_punctuality = st.slider("Attendance Punctuality", min_value=1, max_value=10)

        # Overall Rating (calculated as the average of all metrics)
        overall_rating = (productivity + teamwork + communication + problem_solving + quality_of_work + attendance_punctuality) / 6.0
        comments = st.text_area("Comments")
        if st.button("Submit Evaluation"):
            try:
        # Connect to the database
                mydb = mysql.connector.connect(host="localhost", user="root", password="12345678", database="EMS")
                c = mydb.cursor()

                # Insert evaluation into PerformanceEvaluations table
                sql = "INSERT INTO PerformanceEvaluations (Employee_ID, Evaluation_Date, Productivity, Teamwork, Communication_Skills, Problem_Solving, Quality_of_Work, Attendance_Punctuality, Overall_Rating, Comments) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                values = (employee_id, evaluation_date, productivity, teamwork, communication, problem_solving, quality_of_work, attendance_punctuality, overall_rating, comments)
                c.execute(sql, values)

                # Commit the transaction
                mydb.commit()
                st.success("Performance evaluation submitted successfully!")

            except mysql.connector.Error as err:
                st.error(f"Error: {err}")

            finally:
                # Close the database connection
                c.close()
                mydb.close()
        

def get_employee_data(department_name):
    # Connect to the database and retrieve employee data for the department
    mydb = mysql.connector.connect(host="localhost", user="root", password="12345678", database="EMS")
    c = mydb.cursor()
    c.execute("SELECT Employee_ID, CONCAT(FirstName, ' ', LastName) AS FullName, Department FROM Employees WHERE Department = %s", (department_name,))
    employee_data = c.fetchall()
    if employee_data:
        columns = ["Employee ID", "Employee Name", "Department"]
        return pd.DataFrame(employee_data, columns=columns)
    else:
        return None

def display_training_sessions():
    st.title("Training and Development")
    st.header("Upcoming Training Sessions")

    # Connect to the database and fetch upcoming training sessions
    mydb = mysql.connector.connect(host="localhost", user="root", password="12345678", database="EMS")
    c = mydb.cursor()
    c.execute("SELECT * FROM TrainingRecords WHERE Date >= CURDATE()")
    training_sessions = c.fetchall()

    # Display training sessions in a DataFrame
    if training_sessions:
        columns = ["Session ID", "Session Name", "Description", "Date", "Duration", "Trainer"]
        df = pd.DataFrame(training_sessions, columns=columns)
        st.dataframe(df)
    else:
        st.write("No upcoming training sessions.")



