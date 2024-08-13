# Employee Management System (EMS)

## Overview
The Employee Management System (EMS) is a web application designed to manage employee records, track attendance, monitor performance, handle leave requests, and maintain training records. The backend is built using MySQL and Python, while the frontend is developed with Streamlit.
<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiSz-l4jEaioUmplfsHHWSkIVzdljJURHQfx_zIgUXJrHhURbnYG_ctj_ywdBZ06dSbRi21EnqsRn0qvEYk71qbFN_Q5BltcivQzhl5SludhY2KXGStxDaikrQzqrv6YCiEZTRph8rY1Cw/s600/Employee+Management+System+Project.webp">
## Features
- **Employee Management:** Add, view, and manage employee details such as personal information, job title, department, and salary.
- **Department Management:** Manage departments and assign department heads.
- **Qualification Tracking:** Record and manage employee qualifications.
- **Training Records:** Maintain a log of training sessions including session details, date, and trainer.
- **Performance Evaluations:** Evaluate employee performance based on various criteria such as productivity, teamwork, communication skills, and more.
- **Attendance Tracking:** Track employee attendance with check-in and check-out times.
- **Leave Management:** Handle employee leave requests with status tracking.
## Project Demo Video
[Watch the video](https://drive.google.com/uc?export=view&id=1inVt-L9cpTl90Vgwbug2NNAEFH-O8ATy)

<img src="[https://drive.google.com/file/d/1inVt-L9cpTl90Vgwbug2NNAEFH-O8ATy/view?usp=drive_link](https://drive.google.com/file/d/1inVt-L9cpTl90Vgwbug2NNAEFH-O8ATy/view?usp=sharing)">
## Technologies Used
- **Backend:** MySQL, SQL, Python
- **Frontend:** Streamlit

## Database Schema
<img src="schema.png">

## Prerequisites

Before running the project, make sure you have the following installed:

- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **MySQL Server**: [Download MySQL](https://dev.mysql.com/downloads/mysql/)
- **Streamlit**: [Streamlit Documentation](https://docs.streamlit.io)

## Installation and Setup

Follow these steps to set up and run the project:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/EMS.git
   cd EMS
2. **Set Up the Virtual Environment:**

   ```bash
      python -m venv venv
      source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install the Required Dependencies:**

   ```bash
      pip install -r requirements.txt
4. **Set Up the Database:**

   Create the database and tables using the provided SQL schema in your MySQL environment.

   ```sql
      -- Use the correct database
      USE your_database_name;
      
      -- Drop and recreate tables if needed
      DROP TABLE IF EXISTS Departments;
      Table Departments {
       Department_ID VARCHAR [pk]
       DepartmentName VARCHAR
       DepartmentHead_ID VARCHAR
       DescriptionS VARCHAR
      }
5. **Run the Application:**

   ```bash
      streamlit run scripts/app.py
6. **Access the application:**

   The application will open in your default web browser. If not, navigate to http://localhost:8501 in your       browser.
## Usage
- **Manage Employees:** Add, update, view, and delete employee records.
- **Track Attendance:** Log and monitor employee attendance.
- **Evaluate Performance:** Conduct and record employee performance evaluations.
- **Manage Leave Requests:** Submit and approve leave requests.
- **Record Training Sessions:** Track employee training sessions.
