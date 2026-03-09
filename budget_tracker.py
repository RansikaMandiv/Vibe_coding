def main():
    # Task 01: Ask for total monthly budget
    try:
        total_budget_input = input("Enter your total monthly budget (LKR): ")
        total_budget = float(total_budget_input)
    except ValueError:
        print("Invalid input. Please enter a numerical value for the budget.")
        return

    total_expenses = 0.0

    # Task 03: Extend the program to enter expenses multiple times
    print("\nEnter your expenses one by one. Type 'done' to finish.")
    
    while True:
        entry = input("Enter expense amount (or type 'done'): ").strip().lower()
        
        if entry == 'done':
            break
        
        try:
            expense = float(entry)
            total_expenses += expense
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")

    # Task 01: Subtract expenses and calculate remaining balance
    remaining_balance = total_budget - total_expenses

    # Task 01: Display remaining balance
    print(f"\n--- Budget Summary ---")
    print(f"Total Budget:    {total_budget:,.2f} LKR")
    print(f"Total Expenses:  {total_expenses:,.2f} LKR")
    print(f"Remaining:       {remaining_balance:,.2f} LKR")

    # Task 02: Add Warning Message
    if remaining_balance < 500:
        print("Warning: Low Funds")

if __name__ == "__main__":
    main()
