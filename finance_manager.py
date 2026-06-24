class Transaction:
    def __init__(self, title, amount, category, transaction_type):
        self.title = title
        self.amount = amount
        self.category = category
        self.transaction_type = transaction_type
    
    def display(self):
        return f"Title : {self.title} | Amount : {self.amount} | Category : {self.category} | Transaction Type : {self.transaction_type.capitalize()}"
    
class FinanceManager:
    def __init__(self):
        self.transactions = []
    
    def add_transaction(self, title, amount, category, transaction_type):
        transaction = Transaction(title, amount, category, transaction_type)
        self.transactions.append(transaction)
        return "Transaction Recorded Successfully!"
    
    def view_transactions(self):
        if len(self.transactions) == 0:
            print("No Transactions Recorded Yet.")
            return
        
        for transaction in self.transactions:
            print(transaction.display())
    
    def total_income(self):
        if len(self.transactions) == 0:
            return "No Transactions Recorded Yet."
        
        income = 0
        for transaction in self.transactions:
            if transaction.transaction_type == "income":
                income += transaction.amount
        
        return income
    
    def total_expense(self):
        if len(self.transactions) == 0:
            return "No Transactions Recorded Yet."
        
        expense = 0
        for transaction in self.transactions:
            if transaction.transaction_type == "expense":
                expense += transaction.amount
        
        return expense
    
    def balance(self):
        if len(self.transactions) == 0:
            return 0

        income = 0
        expense = 0

        for t in self.transactions:
            if t.transaction_type == "income":
                income += t.amount
            else:
                expense += t.amount

        return income - expense
    
    def category_wise_expense_report(self):
        if len(self.transactions) == 0:
            return "No Transactions Recorded Yet."
        
        report = {}

        for transaction in self.transactions:
            if transaction.transaction_type == "expense":
                cat = transaction.category
                amt = transaction.amount

                if cat in report:
                    report[cat] += amt
                else:
                    report[cat] = amt
        
        return report
    
    def highest_transaction(self):
        if len(self.transactions) == 0:
            return "No Transactions Recorded Yet."
        
        highest = self.transactions[0]
        for transaction in self.transactions:
            if transaction.amount > highest.amount:
                highest = transaction
        
        return highest
    
    def summary_report(self):
        if len(self.transactions) == 0:
            return "No Transactions Recorded Yet."
        
        report = {
            "total_income" : 0,
            "total_expenses" : 0,
            "balance" : 0,
            "highest_transaction" : None,
            "categories" : []
        }

        for transaction in self.transactions:
            if transaction.transaction_type == "income":
                report["total_income"] += transaction.amount
            
            if transaction.transaction_type == "expense":
                report["total_expenses"] += transaction.amount

            if report["highest_transaction"] is None or report["highest_transaction"].amount < transaction.amount:
                report["highest_transaction"] = transaction
            
            if transaction.category not in report["categories"]:
                report["categories"].append(transaction.category)
        
        report["balance"] = report["total_income"] - report["total_expenses"]
        
        return report

manager = FinanceManager()
while True:
    print("\nFINANCE MANAGEMENT SYSTEM")
    print("1. Add Transaction\n2. View Transactions\n3. Total Income\n4. Total Expenses\n5. Balance\n6. Category Wise Expense Report\n7. Highest Transaction\n8. Summary Report\n9. Exit")
    choice = int(input("Enter Choice of Operation: "))

    if choice == 9:
        print("Thank You")
        break

    elif choice == 1:
        title = input("Enter Title: ")
        amount = float(input("Enter Amount: "))
        category = input("Enter Category: ")
        transaction_type = input("Enter Transaction Type (income / expense): ")
        print(manager.add_transaction(title, amount, category, transaction_type))
    
    elif choice == 2:
        manager.view_transactions()
    
    elif choice == 3:
        print(manager.total_income())
    
    elif choice == 4:
        print(manager.total_expense())
    
    elif choice == 5:
        print(manager.balance())
    
    elif choice == 6:
        print(manager.category_wise_expense_report())
    
    elif choice == 7:
        print(manager.highest_transaction().display())
    
    elif choice == 8:
        summary = manager.summary_report()

        for key, value in summary.items():
            if key == "highest_transaction":
                print(f"{key}: {value.display()}")
            else:
                print(f"{key}: {value}")