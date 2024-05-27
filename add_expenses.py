
def add_expenses():
    invalid = True
    while invalid:
        name = input("    Expense name: ")
        amount = input("    Amount: ")
        if amount.isdigit():
            invalid = False
            print("\n   Expense tracked successfully.\n")

        else:
            print("\n    Invalid. Please add again.")
    return f"{name}: Rs.{amount}"
