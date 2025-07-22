# SQL DEVELOPER INTERNSHIP PROJECT


# Airline Reservation System

## Introduction
This is a Python + SQLite-based airline reservation system that allows flight searching, seat booking, cancellations, and price-based no-show prediction using machine learning.

## Tools Used
- Python 3.x
- SQLite
- Pandas
- Scikit-learn

## Project Modules
- 'init.py': Initializes tables for flights, bookings, and audit logs.
- 'popdb.py': Populates the tables with the Kaggle Database.
- 'blo.py': Booking and cancellation logic.
- 'model.py': Logistic Regression to predict no-shows based on fare and metadata.
- 'querylogic.py': Search interface by route/date.
- 'audit.py': Booking audit log.
- 'summary.py': Reports bookings per airline.
- 'test.py': Compartmentalize the testing by letting the user decide which aspect they want to test.
- 'run_all.py': Automated code which runs all the code except test.py in a sequential order thereby streamlining the process.

##  Features
- Dynamic seat availability.
- Booking + cancellation flow with audit trail.
- Realistic ML model for predicting flight no-shows.
- Grouped summary via SQL.

##  How to Run
```bash
pip install -r requirements.txt
python run_all.py


# Employee Management and Attendance Tracker

## 📌 Introduction
This project simulates an Employee Management and Attendance Tracking system using Python and PostgreSQL. It supports real-time attendance logging, automated reporting, and attrition prediction using machine learning.

## ⚙️ Tools & Technologies
- Python 3.x
- PostgreSQL 17
- Psycopg2
- Pandas
- Jupyter (optional for data exploration)

##  Project Structure
- 'dbengine.py': Initializes the PostgreSQL engine containing the credentials into a function to use it in the concerned files .
- 'schema.py': Initializes PostgreSQL tables and triggers.
- 'popdata.py': Inserting dummy records using the provided dataset.
- 'attendance.py': Simulates multi-day attendance with Present, Late, and Absent statuses.
- 'totalhours.py': Computes total hours worked based on check-in and check-out times.
- 'report.py': Aggregates attendance data and generates employee-wise ratio reports.
- 'model.py': Uses attendance and HR data to predict attrition.
- 'query.py': Query utilities to filter employees by department.
- 'test.py': Compartmentalize the testing by letting the user decide which aspect they want to test.
- 'run_all.py': Automated code which runs all the code except test.py in a sequential order thereby streamlining the process.

##  Sample Features
- Triggers for auto-status handling.
- Monthly attendance + late arrivals.
- Attrition model with performance metrics.
- Reporting via `GROUP BY`, `HAVING`, and `JOIN`s.

##  How to Run
```bash
pip install -r requirements.txt
python run_all.py
