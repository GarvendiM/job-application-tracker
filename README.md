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
Open your terminal and use the command
```
mkdir job_tracker
```

## Step 2
On your terminal, make your way to the job_tracker folder using:
```
cd job_tracker
```

## Step 3
Go to the file database.py and input your MySQL password in the assigned spot  
Download the Schema.sql, app.py, and database.py and input all 3 files into the folder using either the command
```
Copy-Item "Path is usually C:\Users\Your username\Downloads\file name" .
```
Or manually drag the files into the folder  
Note: do not forget the period at the end of the command  
Use the command below to check that the files are there and you are in the folder
```
ls
```

## Step 4
Now install dependencies using:
```
  python -m pip install Flask mysql-connector-python
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
