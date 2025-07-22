from query import find_by_department
from report import *
from totalhours import *
import psycopg2
from dbengine import get_connection

def test_department_query():
    print("\n🔍 Testing query by department:")
    find_by_department("Sales")

def test_attendance_report():
    print("\n📊 Testing attendance report:")
    # Assuming the logic is moved into a function in report.py
    generate_attendance_report()

def test_work_hours():
    print("\n🕒 Testing total work hours per employee:")
    calculate_total_work_hours()

def main():
    print("=== Employee Management Test Menu ===")
    while True:
        print("\nChoose a test to run:")
        print("1. Department-wise Employee Listing")
        print("2. Attendance Summary")
        print("3. Total Work Hours")
        print("4. Run All")
        print("0. Exit")

        choice = input("Enter choice: ")
        if choice == '1':
            test_department_query()
        elif choice == '2':
            test_attendance_report()
        elif choice == '3':
            test_work_hours()
        elif choice == '4':
            test_department_query()
            test_attendance_report()
            test_work_hours()
        elif choice == '0':
            print("Exiting test runner.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()