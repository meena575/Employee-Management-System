import mysql.connector
import datetime
mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="EMS")
print(mydb)
#To Retrive data from database
#cursor-its an entity which user to run sql commands
print("Table:Employees")
c=mydb.cursor()
c.execute("SELECT * FROM Employees")
#To see the data
for r in c:
    print(r)
print("Table:Departments")
c2=mydb.cursor()
c2.execute("SELECT * FROM Departments")
for r in c2:
    print(r)
#To insert data from database into Department table
##D_ID=input("Enter the Id of department:")
##D_Name=input("Ente the name of department:")
##D_head_ID=input("Entet the id of head of the department:")
##Des=input("Enter the description about department:")
##c=mydb.cursor()
##c.execute("INSERT INTO Departments VALUES(%s,%s,%s,%s)",(D_ID,D_Name,D_head_ID,Des))
##mydb.commit()
##print("Added Department Successfully")


import streamlit as st
import sqlite3

# Function to add data to the database table
def add_data(table_name, data):
    conn = sqlite3.connect('database.db')  # Connect to the SQLite database
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO {table_name} VALUES (?, ?, ?, ?)", data)  # SQL query to insert data into the specified table
    conn.commit()  # Commit the transaction
    conn.close()  # Close the database connection

# Streamlit app
def main():
    st.title('Add Data to Table')

    # Sidebar input for table name
    table_name = st.sidebar.text_input('Enter Table Name')

    # Input fields for data
    if table_name:
        st.write(f'Enter data for table: {table_name}')
        l=["Department ID","Departmet Name","department Head ID","Description"]
        data = [st.text_input(f'{column}:') for column in l]  # Assuming 4 columns, modify as needed

        # Button to add data
        if st.button('Add Data'):
            if all(data):
                add_data(table_name, data)
                st.success('Data added successfully.')
            else:
                st.error('Please fill in all fields.')

if __name__ == '__main__':
    main()
















