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
Open your File Explorer and create a new folder called job_tracker

## Step 2
Go to the file database.py and input your MySQL password in the assigned spot
Download the Schema.sql, app.py, and database.py and input all 3 files into the folder

## Step 3
Open your terminal and make your way to the job_tracker folder using:
```
cd # copy and paste the path of the folder here
```

Use the command below to check that the files are there and you are in the folder
```
ls
```

## Step 4
Now install dependencies using:
```
  pip install Flask mysql-connector-python
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
