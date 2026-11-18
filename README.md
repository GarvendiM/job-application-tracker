# Job Application Tracker
A web application to help track job applications during the job
search process.

## Features
- Track companies and job listings
- Record application submissions
- Manage interview schedules
- Store contact information

## Technologies
- MySQL Database
- Python with Flask
- HTML/CSS for the web interface

## Prerequisites
Make sure you have the following installed on your system before starting
- Python (v3.15 or compatible modern release)
- MySQL Server (MySQL Workbench preferrably)

## Step 1
Open your terminal and create your project directory
```
      mkdir job_tracker
      cd job_tracker
```
## Step 2
Login to your MySQL server
Then create the database and import the schema using 
```
  CREATE DATABASE job_tracker;
  USE job_tracker;
```
Then copy the code from Schema.sql into the workbench and execute all code using the lightning bolt

## Step 3
Return to the terminal and install dependencies using:
```
  pip install Flask mysql-connector-python
```
## Step 4
Create a file named database.py in your root folder
```
New-Item -Path "database.py" -ItemType "File"
```
Then open the file using notebook
```
notepad database.py
```
Lastly copy and paste the code below into the notebook and save with Ctrl + S
(Remember to input your own password)
```
import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='your_mysql_password',  # Update with your MySQL password
        database='job_tracker'
    )
```
## Step 5
Run the application using
```
python app.py
```
and finally open your web browser and input
```
http://127.0.0.1:5000
```
