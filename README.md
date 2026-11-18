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
- MySQL Server (MySQL Workbench)
- Windows Powershell

## Step 1
Download the files as a ZIP folder and extract all

## Step 2
Open the folder and right click on database.py.  
Press edit by notepad.   
From there input your own MySQL root password and save it (Ctrl + S).

## Step 3 
Open your MySQL Workbench and type into the Query connected to your server
```
CREATE DATABASE IF NOT EXISTS job_tracker;
USE job_tracker;
```
Then open the Schema.sql and copy/paste it into the Query and run it.

## Step 4
Open your terminal and navigate to the extracted zip folder using: 
```
cd "find the folder and copy the path to here"
```
You should see all files within the folder (Schema.sql, app.py, etc.) when using
```
ls
```

## Step 5
While in this folder through the terminal, install dependencies using:  
```
python -m pip install Flask mysql-connector-python
``` 

## Step 6
Run the application using
```
python app.py
```
and finally press Ctrl + left click in the terminal on 
```
http://127.0.0.1:5000
```
or open a new tab on your web browser and input the link
