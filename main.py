from spending_history import show_spending_history
from add_expenses import add_expenses
from option import choose_option
from expensescsv import makecsv

csv_file = 'expenses.csv'
spending_history = []
total = 0


def main():
    global total

    while True:
        print("\n     Expense Tracker")
        print("1: Show spending history")
        print("2: Add expense")
        print("3: Make expenses.csv.")
        print("4: Quit program.")

        option = choose_option()

        if option == 1:
            show_spending_history(spending_history, total)

        elif option == 2:
            expense = add_expenses()
            spending_history.append(expense)
            amount = int(expense.split(': Rs.')[1])
            total += amount

        elif option == 3:
            makecsv(spending_history)

        elif option == 4:
            print("\n   See you later!!")
            exit()

        else:
            print("    Your input is invalid!")


main()