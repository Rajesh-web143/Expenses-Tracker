#Expenses Tracker Project

expenses = [] # list of expenses in form of dictionary
print("Welcome to Expenses Tracker")

while True:
    print("====MENU====")
    print("1. Add Expenses")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Exit")
    
    choice = int(input("Enter Your Choice : "))

# ADD EXPENSES
    if(choice == 1):
        Date = input("Enter the date of expenses(dd-mm-yyyy) : ")
        Category = input("Enter the category : ")
        Description = input("Enter the details : ")
        Amount = float(input("Enter the amount : "))
        
        expense = {
            "date" : Date,
            "category" : Category,
            "description" : Description,
            "amount" : Amount
        }
        
        expenses.append(expense)
        print(" \n Done, Expenses added succesfully.")

# VIEW ALL EXPENSES    
    elif(choice == 2):
        if(len(expenses) == 0) :
            print("No Expenses Added.")
        else:
            print("==== VIEW YOUR ALL EXPENSES ====")
            count = 1
            for eachexpense in expenses:
                print(f"Expense Number {count} :  {eachexpense["date"]}, {eachexpense["category"]}, {eachexpense["description"]}, {eachexpense["amount"]}")
                count += 1 
    
# VIEW TOTAL EXPENSES
    elif(choice == 3):
        total = 0 
        for eachexpense in expenses:
            total += eachexpense["amount"]
        print(" \n TOTAL EXPENSES : " , total)
        
# EXIT
    elif(choice == 4):
        print("==== THANK YOU ====")
        break
    
    else :
        print("Invalid Choice, Try Again....")
