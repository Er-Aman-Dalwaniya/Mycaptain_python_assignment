import json
import os
from datetime import datetime

# Global variables
expense_data = {}  # Dictionary to store expense data
categories = ["Foods", "Patrol", "Football Matches", "Football/Patrol"]  # Predefined expense categories

# File to store persistent data
data_file = "expense_data.json"

def load_data():
    """Load expense data from a file if it exists."""
    global expense_data
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            expense_data = json.load(file)

def save_data():
    """Save expense data to a file."""
    with open(data_file, "w") as file:
        json.dump(expense_data, file)

def display_menu():
    """Display the main menu options."""
    print("\nExpense Recording System")
    print("1. Add Expense")
    print("2. View Summary")
    print("3. Exit")

def add_expense():
    """Allow the user to input a new expense."""
    amount = float(input("Enter the amount spent: Rs"))
    description = input("Enter a brief description: ")
    
    print("Select a category:")
    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

    category_choice = input("Enter the category number or add a new category: ")
    if category_choice.isdigit() and 1 <= int(category_choice) <= len(categories):
        category = categories[int(category_choice) - 1]
    else:
        category = category_choice.lower()
        if category not in categories:
            categories.append(category)

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    expense_data[date] = {"amount": amount, "description": description, "category": category}
    save_data()
    print("Expense added successfully!")

def view_summary():
    """Display a summary of the user's expenses."""
    total_amount = 0
    category_summary = {}

    for date, expense in expense_data.items():
        total_amount += expense["amount"]
        category = expense["category"]
        category_summary[category] = category_summary.get(category, 0) + expense["amount"]

    print("\nExpense Summary")
    print("Total Amount Spent: $", total_amount)

    print("\nBreakdown by Category:")
    for category, amount in category_summary.items():
        print(f"{category}: ${amount}")

def main():
    load_data()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            save_data()
            print("Exiting the Expense Recording System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()