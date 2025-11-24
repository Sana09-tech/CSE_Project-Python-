import csv
import os
from datetime import date

# File to store the data
FILE_NAME = "my_expenses.csv"

def initialize_file():
    """Check if the CSV file exists. If not, create it with headers."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])

def add_expense():
    print("\n--- Add New Expense ---")
    
    # Get today's date automatically
    today = str(date.today())
    
    # Get user input
    category = input("Category (Food, Transport, Bills, etc.): ")
    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Error: Please enter a valid number for the amount.")
        return

    description = input("Short Description: ")

    # Append data to the CSV file using mode 'a' (append)
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([today, category, amount, description])
    
    print("Success: Expense saved!")

def view_summary():
    print("\n--- Expense Summary ---")
    if not os.path.exists(FILE_NAME):
        print("No records found. Add an expense first!")
        return

    total_spent = 0
    
    # Read the file using mode 'r' (read)
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        
        # Skip the header row
        next(reader)
        
        print(f"{'Date':<12} {'Category':<15} {'Amount':<10} {'Description'}")
        print("-" * 50)
        
        for row in reader:
            # row[2] is the amount column
            print(f"{row[0]:<12} {row[1]:<15} ₹{row[2]:<10} {row[3]}")
            total_spent += float(row[2])
            
    print("-" * 50)
    print(f"TOTAL SPENT: ₹{total_spent:.2f}")

def main():
    initialize_file()
    
    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        
        choice = input("Enter choice (1-3): ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_summary()
        elif choice == '3':
            print("Goodbye! Saving data...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()