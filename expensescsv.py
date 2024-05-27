import csv


def makecsv(spending):
    total = 0
    while True:
        try:
            with open('expenses.csv', 'w', newline='') as csvfile:
                field_names = ['Expense', 'Spent(Rs.)']
                writer = csv.DictWriter(csvfile, fieldnames=field_names)
                writer.writeheader()
                for i in spending:
                    description, amount = i.split(': Rs.')
                    writer.writerow(
                        {"Expense": description, "Spent(Rs.)": amount})
                    total += int(amount)

                writer.writerow({"Expense": "Total", "Spent(Rs.)": total})
                break
        except:
            print(
                "The file is already open. Please close the file and run the script again.")
            break
