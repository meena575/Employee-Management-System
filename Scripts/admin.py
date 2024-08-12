import streamlit as st
import mysql.connector
import pandas as pd
import re
from datetime import datetime
def display_admin_dashboard():
    st.title("Employee Management System - Admin Panel")

    st.title("Admin Dashboard")
    choice1=st.selectbox("Admin Features",("None","Department Management","User Managemnet","Employee Qualifications","Attendance Management","Performance Evaluation","Training Records Management"))
    if(choice1=="Department Management"):
        dep_f=st.radio("Department",("None","Add Department","View Departments","Update Departments","Delete Department"))
        if(dep_f=="Add Department"):
            d_id=st.text_input("Department ID")
            d_name=st.text_input("Departmet Name")
            d_head_id=st.text_input("department Head ID")
            dsc=st.text_input("Description")
            
            if(d_id!="" and d_name!="" and d_head_id!="" and dsc!=""):
                AD_btn=st.button("Add")
                if(AD_btn):
                    mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="EMS")
                    c=mydb.cursor()
                    c.execute("INSERT INTO Departments VALUES(%s,%s,%s,%s)",(d_id,d_name,d_head_id,dsc))
                    mydb.commit()
                    c.close()
                    st.write("Added Department Successfully")
        elif(dep_f=="View Departments"):
            mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="EMS")
            df=pd.read_sql("SELECT * FROM Departments",mydb)
            st.dataframe(df)
        elif(dep_f=="Update Departments"):
            d_id=st.text_input("Department ID")
            d_name=st.text_input("Departmet Name")
            d_head_id=st.text_input("department Head ID")
            dsc=st.text_input("Description")

            if(d_id!="" and d_name!="" and d_head_id!="" and dsc!=""):
                ED_btn=st.button("Update")
                if(ED_btn):
                    mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="EMS")
                    c=mydb.cursor()
                    c.execute("UPDATE Departments SET Department_ID=%s,DepartmentName=%s, DepartmentHead_ID=%s,DescriptionS=%s WHERE Department_ID=%s",(d_id,d_name,d_head_id,dsc,d_id))
                    mydb.commit()
                    c.close()
                    st.write("Updated Department Successfully")
        elif(dep_f=="Delete Department"):
            d_id=st.text_input("Department ID")
            if(d_id!=""):
                RD_btn=st.button("Delete")
                if(RD_btn):
                    mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="EMS")
                    c=mydb.cursor()
                    c.execute("DELETE FROM Departments WHERE Department_ID=%s",(d_id,))
                    mydb.commit()
                    c.close()
                    st.write("Deleted Department Successfully")
    elif(choice1=="User Managemnet"):
        emp_f=st.radio("Employees",("None","Add Employee","View Employee","Update Employee","Delete Employee",))
        if(emp_f=="Add Employee"):
            e_id=st.text_input("Employee ID")
            ef_name=st.text_input("First Name")
            el_name=st.text_input("Last Name")
            date_of_birth=st.date_input("Date_Of_Birth")
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            c_no=st.text_input("ContactNumber")
            email=st.text_input("Email ID")
            address=st.text_input("Address")
            depart=st.text_input("Department")
            j_title=st.text_input("Job Title")
            d_of_join=st.date_input("Date of Joining")
            salary=st.text_input("Salary")
            pwd=st.text_input("Password",type='password')
            role = st.selectbox("Role", ["Employee", "Admin", "Department Head"])
            
            if(e_id!="" and ef_name!="" and el_name!="" and date_of_birth!="" and gender!="" and c_no!="" and email!="" and address!="" and depart!="" and
               j_title!="" and d_of_join!="" and salary!="" and pwd!="" and role!="" and is_valid_email(email) and is_valid_contact_number(c_no)):
                AD_btn=st.button("Add Employee")
                if(AD_btn):
                    mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="EMS")
                    c=mydb.cursor()
                    c.execute("INSERT INTO Employees VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(e_id,ef_name,el_name,date_of_birth,gender,c_no,
                                    email,address,depart,j_title,d_of_join,salary,pwd,role))
                                                                                
                    mydb.commit()
                    c.close()
                    st.write("Added Employee Successfully")
            
        elif(emp_f=="View Employee"):
            mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="EMS")
            df=pd.read_sql("SELECT * FROM Employees",mydb)
            st.dataframe(df)
        
        elif(emp_f=="Update Employee"):
            E_id=st.text_input("Employee ID")
            email=st.text_input("Email ID")
            pwd=st.text_input("Password",type='password')
            c_no=st.text_input("ContactNumber")
            address=st.text_input("Address")

            if(E_id!="" and email!="" and c_no!="" and address!=""):
                EU_btn=st.button("UPDATE")
                if(EU_btn):
                    mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="EMS")
                    c=mydb.cursor()
                    c.execute("UPDATE Employees SET Email=%s,Password=%s, ContactNumber=%s,Address=%s WHERE Employee_ID=%s",(email,pwd,c_no,address,E_id))
                    mydb.commit()
                    c.close()
                    st.write("Updated Successfully")
        elif(emp_f=="Delete Employee"):
            E_id=st.text_input("Employee ID")
            if(E_id!=""):
                RE_btn=st.button("Delete")
                if(RE_btn):
                    mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="EMS")
                    c=mydb.cursor()
                    c.execute("DELETE FROM employees WHERE Employee_ID=%s",(E_id,))
                    mydb.commit()
                    c.close()
                    st.write("Deleted Employee Successfully")
    elif(choice1=="Employee Qualifications"):
        emp_f=st.radio("Employees Qualifications",("None","Add Qualifications","View Qualifications","Update Qualifications","Delete Qualifications",))

        if(emp_f=="Add Qualifications"):
            #q_id=st.text_input("Qualifications ID")
            e_id=st.text_input("Employee ID")
            Q_name=st.text_input("QualificationName")
            inst=st.text_input("Institution")
            c_date=st.date_input("Completion_Date")
            if( e_id and Q_name and inst and c_date):
                AQ_btn=st.button("Add")
                if AQ_btn:
                    try:
                        mydb = mysql.connector.connect(host="localhost", user="root", password="12345678", database="EMS")
                        c = mydb.cursor()
                        
                        c.execute("SELECT * FROM Employees WHERE Employee_ID = %s", (e_id,))
                        employee = c.fetchone()
                        
                        if employee:
                            # Employee_ID exists, proceed with insertion
                            c.execute("INSERT INTO EmployeeQualification (Employee_ID, QualificationName, Institution, Completion_Date) VALUES (%s, %s, %s, %s)", (e_id, Q_name, inst, c_date))
                            mydb.commit()
                            st.write("Added Successfully")
                        else:
                            st.error("Employee ID does not exist")
                        
                        c.close()
                        mydb.close()
                    except mysql.connector.Error as err:
                        st.error(f"Error: {err}")
        elif(emp_f=="View Qualifications"):
            mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="EMS")
            df=pd.read_sql("SELECT * FROM EmployeeQualification",mydb)
            st.dataframe(df)
        
        elif(emp_f=="Update Qualifications"):
            #q_id=st.text_input("Qualifications ID")
            e_id=st.text_input("Employee ID")
            Q_name=st.text_input("QualificationName")
            inst=st.text_input("Institution")
            c_date=st.date_input("Completion_Date")

            if( e_id and Q_name and inst and c_date):
                UQ_btn=st.button("Update")
                if UQ_btn:
                    try:
                        mydb = mysql.connector.connect(host="localhost", user="root", password="12345678", database="EMS")
                        c = mydb.cursor()
                        
                        c.execute("SELECT * FROM Employees WHERE Employee_ID = %s", (e_id,))
                        employee = c.fetchone()
                        
                        if employee:
                            mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="EMS")
                            c=mydb.cursor()
                            c.execute("UPDATE EmployeeQualification SET QualificationName=%s,Institution=%s,Completion_Date=%s WHERE  Employee_ID=%s",(Q_name,inst,c_date,e_id))
                            mydb.commit()
                            c.close()
                            st.write("Updated  Successfully")
                        else:
                            st.error("Employee ID does not exist")
                        
                        c.close()
                        mydb.close()
                    except mysql.connector.Error as err:
                        st.error(f"Error: {err}")
        elif(emp_f=="Delete Qualifications"):
            e_id=st.text_input("Employee ID")
            if(e_id!=""):
                RD_btn=st.button("Delete")
                if(RD_btn):
                    mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="EMS")
                    c=mydb.cursor()
                    c.execute("DELETE FROM EmployeeQualification WHERE Employee_ID=%s",(e_id,))
                    mydb.commit()
                    c.close()
                    st.write("Deleted Employee Qualification Successfully")
 


    elif choice1 == "Attendance Management":
        emp_f = st.radio("Attendance Records", ("None", "Add", "View", "Update", "Delete"))

        if emp_f == "Add":
            employee_id = st.text_input("Employee ID")
            date = st.date_input("Date")
            check_in_time = st.time_input("Check-in Time")
            check_out_time = st.time_input("Check-out Time")

            if employee_id and date and check_in_time and check_out_time:
                try:

                    mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="EMS")
                    c=mydb.cursor()
                    c.execute("SELECT * FROM employees WHERE Employee_ID = %s", (employee_id,))
                    employee_exists = c.fetchone()

                    if employee_exists:
                        if(st.button("Add")):
                            c.execute("INSERT INTO AttendanceRecords (Employee_ID, Date, CheckInTime, CheckOutTime) VALUES (%s, %s, %s, %s)",
                                            (employee_id, date, check_in_time, check_out_time))
                            mydb.commit()
                            c.close()
                            st.write("Added Successfully")
                    else:
                        st.error("Employee ID does not exist")
                except mysql.connector.Error as err:
                    st.error(f"Error: {err}")

        elif emp_f == "View":
            try:
                mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="EMS")
                c=mydb.cursor()
                df = pd.read_sql("SELECT * FROM AttendanceRecords", mydb)
                st.dataframe(df)
            except mysql.connector.Error as err:
                st.error(f"Error: {err}")

        elif emp_f == "Update":
            attendance_id = st.text_input("Attendance ID")
            date = st.date_input("Date")
            check_in_time = st.time_input("Check-in Time")
            check_out_time = st.time_input("Check-out Time")

            if attendance_id and date and check_in_time and check_out_time:
                try:
                    if(st.button("Update")):
                        mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="EMS")
                        c=mydb.cursor()
                        c.execute("UPDATE AttendanceRecords SET Date=%s, CheckInTime=%s, CheckOutTime=%s WHERE Attendance_ID=%s",
                                        (date, check_in_time, check_out_time, attendance_id))
                        mydb.commit()
                        c.close()
                        st.write("Updated Successfully")
                except mysql.connector.Error as err:
                    st.error(f"Error: {err}")

        elif emp_f == "Delete":
            A_id = st.text_input("Attendance ID")
            if A_id:
                try:
                    if(st.button("Delete")):
                        mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="EMS")
                        c=mydb.cursor()
                        c.execute("DELETE FROM AttendanceRecords WHERE Attendance_ID=%s", (A_id,))
                        mydb.commit()
                        c.close()
                        st.write("Deleted Successfully")
                except mysql.connector.Error as err:
                    st.error(f"Error: {err}")
    elif(choice1=="Performance Evaluation"):
        option = st.selectbox("Select Feature:", ["View Performance Metrics", "Generate Performance Report", "Conduct Performance Review"])
        if(option=="View Performance Metrics"):
            try:
                mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="EMS")
                c=mydb.cursor()
                c.execute("SELECT Employee_ID, Attendance_Punctuality, Productivity FROM PerformanceEvaluations")
                performance_data = c.fetchall()
                

                if performance_data:
                    df = pd.read_sql("SELECT * FROM PerformanceEvaluations", mydb)
                    st.dataframe(df)
                    mydb.close()
                else:
                    st.write("No performance data available.")
            except mysql.connector.Error as err:
                st.error(f"Error: {err}")
        elif(option=="Generate Performance Report"):
            try:
                mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="EMS")
                c=mydb.cursor()
                c.execute("SELECT Employee_ID, Attendance_Punctuality, Productivity FROM PerformanceEvaluations")
                performance_data = c.fetchall()
                mydb.close()

                if performance_data:
                    df = pd.DataFrame(performance_data, columns=['Employee ID', 'Attendance', 'Productivity'])
                    st.write("Performance Report:")
                    st.write(df)

                    st.bar_chart(df.set_index('Employee ID'))
                else:
                    st.write("No performance data available.")
            except mysql.connector.Error as err:
                st.error(f"Error: {err}")
        elif(option=="Conduct Performance Review"):
            employee_id = st.text_input("Enter Employee ID:")
            employee_data = get_employee_data(employee_id)
    
            if employee_data is not None:
                st.dataframe(employee_data)
                
                st.title("Performance Evaluation")

                employee_id = st.text_input("Employee ID")

                evaluation_date = st.date_input("Evaluation Date", value=datetime.today())
                productivity = st.slider("Productivity", min_value=1, max_value=10)
                teamwork = st.slider("Teamwork", min_value=1, max_value=10)
                communication = st.slider("Communication Skills", min_value=1, max_value=10)
                problem_solving = st.slider("Problem Solving", min_value=1, max_value=10)
                quality_of_work = st.slider("Quality of Work", min_value=1, max_value=10)
                attendance_punctuality = st.slider("Attendance Punctuality", min_value=1, max_value=10)
                overall_rating = (productivity + teamwork + communication + problem_solving + quality_of_work + attendance_punctuality) / 6.0
                comments = st.text_area("Comments")
                if st.button("Submit Evaluation"):
                    try:
                        mydb = mysql.connector.connect(host="localhost", user="root", password="12345678", database="EMS")
                        c = mydb.cursor()

                        sql = "INSERT INTO PerformanceEvaluations (Employee_ID, Evaluation_Date, Productivity, Teamwork, Communication_Skills, Problem_Solving, Quality_of_Work, Attendance_Punctuality, Overall_Rating, Comments) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                        values = (employee_id, evaluation_date, productivity, teamwork, communication, problem_solving, quality_of_work, attendance_punctuality, overall_rating, comments)
                        c.execute(sql, values)

                        mydb.commit()
                        st.success("Performance evaluation submitted successfully!")

                    except mysql.connector.Error as err:
                        st.error(f"Error: {err}")

                    finally:
                        c.close()
                        mydb.close()
        

    elif(choice1=="Training Records Management"):
        option1 = st.selectbox("Select Feature:", ["Add Training Session", "View Training Sessions"])
        if(option1=="Add Training Session"):
            st.subheader("Add New Training Session")
            session_name = st.text_input("Session Name")
            description = st.text_area("Description")
            date = st.date_input("Date")
            duration = st.number_input("Duration (in minutes)", min_value=0)
            trainer = st.text_input("Trainer")

            if st.button("Add Session"):
                if session_name and date and duration and trainer:
                    try:
                        mydb, cursor = get_cursor()
                        cursor.execute("INSERT INTO TrainingRecords (Session_Name, Description, Date, Duration, Trainer) VALUES (%s, %s, %s, %s, %s)",
                                       (session_name, description, date, duration, trainer))
                        mydb.commit()
                        mydb.close()
                        st.success("Training session added successfully.")
                    except mysql.connector.Error as err:
                        st.error(f"Error: {err}")
            else:
                st.warning("Please fill in all required fields.")
        elif(option1=="View Training Sessions"):
            st.subheader("View Training Sessions")
            try:
                mydb, cursor = get_cursor()
                cursor.execute("SELECT Session_ID, Session_Name, Description, Date, Duration, Trainer FROM TrainingRecords")
                training_data = cursor.fetchall()
                mydb.close()

                if training_data:
                    df = pd.DataFrame(training_data, columns=['Session ID', 'Session Name', 'Description', 'Date', 'Duration', 'Trainer'])
                    st.dataframe(df)
                else:
                    st.write("No training sessions available.")
            except mysql.connector.Error as err:
                st.error(f"Error: {err}")
def get_employee_data(employee_id):
    mydb = mysql.connector.connect(host="localhost", user="root", password="12345678", database="EMS")
    c = mydb.cursor()
    c.execute("SELECT Employee_ID, CONCAT(FirstName, ' ', LastName) AS FullName, Department FROM Employees WHERE Employee_ID = %s", (employee_id,))
    employee_data = c.fetchall()
    if employee_data:
        columns = ["Employee ID", "Employee Name", "Department"]
        return pd.DataFrame(employee_data, columns=columns)
    else:
        return None
def get_cursor():
    mydb = mysql.connector.connect(host="localhost", user="root", password="12345678", database="EMS")
    return mydb, mydb.cursor()
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False
def is_valid_contact_number(contact_number):
    pattern = r"^\d{10}$"
    return bool(re.match(pattern, contact_number))
