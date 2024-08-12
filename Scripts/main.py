import streamlit as st
import mysql.connector
import pandas as pd
import re
st.markdown("<h1 style='text-align: center;'>Employee Management System</h1>", unsafe_allow_html=True)

st.sidebar.title("Navigation")
choice=st.sidebar.radio("My Menu",("Home","Login"))
def is_valid_email(email):
    # Define a regular expression pattern for email validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    # Use the re.match function to check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False   

if(choice=="Home"):
         # Load the image
    image="https://www.pockethrms.com/wp-content/uploads/2022/01/Happy-Workforce.jpg"    
    # Get the width of the image
    image_width = 500
    
    # Calculate the left margin to center the image
    #left_margin = (st.sidebar.columns[0].width - image_width) / 2
    
    # Center the image using Streamlit layout options
    st.markdown(
        f'<div style="text-align:center;">'
        f'<img src="{image}" style="width:500px">'
        '</div>',
        unsafe_allow_html=True
    )
    #st.image("https://global-uploads.webflow.com/625d567276661e857102867d/63cd55af57b94e9886e36427_A%20Beginners%20Guide%20to%20Employee%20Management%20System.png",width=400)
    st.write("This is a web Application developed by Meena Reddimpalli")



elif(choice=="Login"):
    login_type= st.radio("Select User Type",
                     ['Employee', 'Department Head',"Admin"])
    if(login_type=="Employee"):
        st.write("Emplyee Login Page:")
        
        if 'login' not in st.session_state:
            st.session_state['login']=False
        email_id=st.text_input("Email ID") 
        pwd=st.text_input("Password")
        btn=st.button("Login")
        if btn:
            mydb = mysql.connector.connect(host="localhost", user="root", password="12345678", database="EMS")
            c = mydb.cursor()
            c.execute("SELECT Email, Password FROM Employees WHERE Role='Employee'")
            for (email, password) in c:
                if is_valid_email(email_id) and email_id==email :
                    if pwd == password:
                        st.session_state.logged_in = True
                        st.success("Logged in successfully!")
                        st.write(st.session_state.logged_in)
                         
                        break  # Exit the loop if the password matches
                    else:
                        st.error("Invalid username or password")
                        break  # Exit the loop if the password does not match
            else:
                st.error("Invalid username or password")
    elif(login_type=="Department Head"):
        st.write("Department Head Login Page:")
        
        if 'login' not in st.session_state:
            st.session_state['login']=False
        email_id=st.text_input("UserName(Your Email_ID)") 
        pwd=st.text_input("Password")
        btn=st.button("Login")
        if btn:
            mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="EMS")
            c=mydb.cursor()
            c.execute("SELECT Email , Password FROM Employees INNER JOIN Departments ON Employee_ID=DepartmentHead_ID")
            for r in c:
                if(r[0]==email_id and r[1]==pwd):
                    st.session_state['login']=True
                    break
            if(not st.session_state['login']):
                st.write("Incorrect ID or Password")
        if(st.session_state['login']):
            st.write("Login Successfull")
        st.write(st.session_state['login'])
        st.session_state['redirect'] = True
        if st.session_state.get('redirect', False):
            st.title("Head Dashboard")
    elif(login_type=="Admin"):
        st.write("Admin Login Page")
        
        if 'login' not in st.session_state:
            st.session_state['login']=False
        email_id=st.text_input("UserName(Your Email_ID)") 
        pwd=st.text_input("Password")
        btn=st.button("Login")
        if btn:
            mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="EMS")
            c=mydb.cursor()
            c.execute("SELECT Email , Password FROM Employees WHERE Role='Admin'")
            for r in c:
                if(r[0]==email_id and r[1]==pwd):
                    st.session_state['login']=True
                    break
            if(not st.session_state['login']):
                st.write("Incorrect ID or Password")
        if(st.session_state['login']):
            st.write("Login Successfull")
        st.write(st.session_state['login'])
        st.session_state['redirect'] = True
        # Admin dashboard page
        if st.session_state.get('redirect', False):
            st.title("Admin Dashboard")
            choice1=st.selectbox("Admin Features",("None","Departments","Employees","EmployeeQualification","AttendanceRecords","LeaveRequests","PerformanceEvaluations"))
            if(choice1=="Departments"):
                dep_f=st.selectbox("Department",("None","Add Department","View Departments","Update Departments","Delete Department"))
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
                            c.execute("UPDATE Departments SET DepartmentName=%s, DepartmentHead_ID=%s,DescriptionS=%s WHERE Department_ID=%s",(d_name,d_head_id,dsc,d_id))
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
            elif(choice1=="Employees"):
                emp_f=st.selectbox("Employees",("None","Add Employee","View Employee","Update Employee","Delete Employee",))
                if(emp_f=="Add Employee"):
                    e_id=st.text_input("Employee ID")
                    ef_name=st.text_input("First Name")
                    el_name=st.text_input("Last Name")
                    date_of_birth=st.text_input("Date_Of_Birth")
                    gender=st.text_input("Gender")
                    c_no=st.text_input("ContactNumber")
                    email=st.text_input("Email ID")
                    address=st.text_input("Address")
                    depart=st.text_input("Department")
                    j_title=st.text_input("Job Title")
                    d_of_join=st.text_input("Date of Joining")
                    salary=st.text_input("Salary")
                    pwd=st.text_input("Password",type='password')
                    st.write("Role:")
                    is_employee = st.checkbox('Employee')
                    is_admin = st.checkbox('Admin')
                    is_department_head = st.checkbox('Department Head')
                    if(is_employee):
                        role="Employee"
                    elif(is_admin):
                        role="Admin"
                    elif(is_department_head):
                        role="Department Head"
                    
                    if(e_id!="" and ef_name!="" and el_name!="" and date_of_birth!="" and gender!="" and c_no!="" and email!="" and address!="" and depart!="" and
                       j_title!="" and d_of_join!="" and salary!="" and pwd!="" and role!=""  ):
                        AD_btn=st.button("Add")
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
            elif(choice1=="EmployeeQualification"):
                empq_f=st.selectbox("Department",("None","Add","View","Update","Delete"))
                if(empq_f=="Add"):
                    q_id=st.text_input("Qualifications ID")
                    e_id=st.text_input("Employee ID")
                    Q_name=st.text_input("QualificationName")
                    inst=st.text_input("Institution")
                    c_date=st.text_input("Completion_Date")
                    if(q_id!="" and e_id!="" and Q_name!="" and inst!="" and c_date!=""):
                        AQ_btn=st.button("Add")
                        if(AQ_btn):
                            mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="EMS")
                            c=mydb.cursor()
                            c.execute("INSERT INTO EmployeeQualification VALUES(%s,%s,%s,%s,%s)",(q_id,e_id,Q_name,inst,c_date))
                            mydb.commit()
                            c.close()
                            st.write("Added  Successfully")
                elif(empq_f=="View"):
                    mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="EMS")
                    df=pd.read_sql("SELECT * FROM EmployeeQualification",mydb)
                    st.dataframe(df)
                elif(empq_f=="Update"):
                    d_id=st.text_input("Department ID")
                    d_name=st.text_input("Departmet Name")
                    d_head_id=st.text_input("department Head ID")
                    dsc=st.text_input("Description")

                    if(d_id!="" and d_name!="" and d_head_id!="" and dsc!=""):
                        ED_btn=st.button("Update")
                        if(ED_btn):
                            mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="EMS")
                            c=mydb.cursor()
                            c.execute("UPDATE Departments SET DepartmentName=%s, DepartmentHead_ID=%s,DescriptionS=%s WHERE Department_ID=%s",(d_name,d_head_id,dsc,d_id))
                            mydb.commit()
                            c.close()
                            st.write("Updated Department Successfully")
                elif(empq_f=="Delete Department"):
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
            elif(choice1=="TrainingRecords"):
                TR_btn=st.button("Display")
            elif(choice1=="PerformanceEvaluations"):
                PE_btn=st.button("Display")
            elif(choice1=="AttendanceRecords"):
                AR_btn=st.button("Display")
            elif(choice1=="LeaveRequests"):
                LR_btn=st.button("Display")


        



            

