import streamlit as st
import mysql.connector
import pandas as pd


# Function to fetch data from the database table
def view_data(table_name):
    mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="EMS")
    df=pd.read_sql("SELECT * FROM Departments",mydb)
    st.dataframe(df)
    return df
def add_data(table_name, data):
    mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="EMS")
    c=mydb.cursor()
    c.execute("INSERT INTO Departments VALUES(%s,%s,%s,%s)",(d_id,d_name,d_head_id,dsc))
    mydb.commit()
    c.close()
    
# Streamlit app
def main():
    st.title("Employee Management System")
choice=st.sidebar.selectbox("My Menu",("Home","Login"))
if(choice=="Home"):
    st.image("https://global-uploads.webflow.com/625d567276661e857102867d/63cd55af57b94e9886e36427_A%20Beginners%20Guide%20to%20Employee%20Management%20System.png")
    st.write("This is a web Application developed by Meena Reddimpalli")
elif(choice=="Login"):
    login_type= st.selectbox("Select User Type",
                     ['Employee', 'Department Head',"Admin"])
    if(login_type=="Employee"):
        st.write("Emplyee Login Page:")
        
        if 'login' not in st.session_state:
            st.session_state['login']=False
        email_id=st.text_input("UserName(Your Email_ID)") 
        pwd=st.text_input("Password")
        btn=st.button("Login")
        if btn:
            mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="EMS")
            c=mydb.cursor()
            c.execute("SELECT Email ,Password From Employees")
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
            st.title("Employee Dashboard")
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
            ganesh@pkrstechsolutions.com
       
if __name__ == '__main__':
    main()

    # Button to fetch data
    if st.sidebar.button('View Data'):
        if table_name:
            data = view_data(table_name)
            st.write('Data from table:', table_name)
            
        else:
            st.error('Please enter a table name.')
