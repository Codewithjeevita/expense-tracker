# EXPENSE TRACKER PROJECT
expenseslist = []  # list of expenses in form of dictionary

while True:
    print("======MENU======")
    print("\n1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

# ADD EXPENSES
    if choice == 1:
        date= input("Enter a date:")
        category= input("Enter category (travel,food,cloth,books): ")
        description= input("Add more Deatails: ")
        amount=float(input("Enter the amount: "))

        expenses={
            "date": date,
            "category": category,
            "description": description,
            "amount": amount,
        }


        expenseslist.append(expenses)
        print("\nDONE BRO, Expenses is added Successfully")

#VIEW ALL EXPENSES

    elif choice == 2:
        if len(expenseslist) == 0:
            print("No Expenses Added. Jao pehle kharcha karo.")
        else:
            print("======= your overall Expenses =======")
            count = 1
            for eachcost in expenseslist:
                print(f"Cost Number {count} -> {eachcost['date']}, {eachcost['category']},{eachcost['description']}, {eachcost['amount']}")
                count += 1

# VIEW TOTAL SPENDING

    elif choice == 3:
        total = 0
        for eachcost in expenseslist:
            total = total + eachcost["amount"]
        print("\nTOTAL COST =", total)

#EXIT

    elif choice == 4:
        print("Thank You For Using System")
        break

    else:
        print("INVALID CHOICE.... TRY AGAIN...")