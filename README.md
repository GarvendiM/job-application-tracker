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
- Windows Powershell (optional)

## Step 1
Download the files as a ZIP folder and extract all

## Step 2
Right click on database.py and open it using notebook.   
From there input your MySQL root password and save it (Ctrl + S).

## Step 2 
Open your MySQL Workbench and type into the Query
```
USE job_tracker;
```
## Step 3
Open your terminal (Windows Powershell preferred) and install dependencies using:  
```
python -m pip install Flask mysql-connector-python
``` 

## Step 4
Run the application using
```
python app.py
```
and finally open a new tab on your web browser and input
```
http://127.0.0.1:5000
```
