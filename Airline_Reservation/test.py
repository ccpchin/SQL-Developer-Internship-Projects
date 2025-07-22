from blo import make_booking, cancel_booking
from querylogic import search_flights
import sqlite3

def test_search():
    print("\n🔍 Testing flight search:")
    search_flights("Banglore", "New Delhi", "2019-03-01")

def test_booking():
    print("\n✈️ Testing booking:")
    make_booking(1001, 1, "21B")

def test_cancellation():
    print("\n❌ Testing cancellation:")
    cancel_booking(1)

def main():
    print("=== Airline Reservation Test Menu ===")
    while True:
        print("\nChoose a test to run:")
        print("1. Flight Search")
        print("2. Book a Flight")
        print("3. Cancel a Booking")
        print("4. Run All")
        print("0. Exit")

        choice = input("Enter choice: ")
        if choice == '1':
            test_search()
        elif choice == '2':
            test_booking()
        elif choice == '3':
            test_cancellation()
        elif choice == '4':
            test_search()
            test_booking()
            test_cancellation()
        elif choice == '0':
            print("Exiting test runner.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()