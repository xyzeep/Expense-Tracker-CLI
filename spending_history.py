def show_spending_history(spending_history, total_spending):
    if spending_history:
        print("\n   Spending History: ")

        j = 1
        for i in spending_history:
            print(f"        {j}. {i}")

            j += 1
        print(f"\n            Total: Rs.{total_spending}")

    else:
        print("\n    Spending History: ")
        print("        (empty)\n")