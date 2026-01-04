class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})
    
    def withdraw(self, amount, description=""):
        if (self.check_funds(amount)):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction['amount']

        return balance

    def transfer(self, amount, destination):
        if (self.check_funds(amount)): 
            self.withdraw(amount, f"Transfer to {destination.name}")
            destination.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        return False if (amount > self.get_balance()) else True        

    def __str__(self):
        final_str = ""
        star_amount = (30 - len(self.name))//2
        final_str += '*' * star_amount + self.name + '*' * star_amount + '\n'
        
        for transaction in self.ledger:
            final_str += f"{transaction['description'][:23]:<23}"

            final_str += f"{float(transaction['amount']):>7.2f}\n"

        final_str += f"Total: {self.get_balance():.2f}"

        return final_str

def create_spend_chart(categories):
    # 100 = total_spent, percentage = category_spent
    total_spent = 0
    categories_loss = []
    for category in categories:
        category_spent = 0
        for transaction in category.ledger:
            if transaction['amount'] < 0:
                total_spent += transaction['amount']
                category_spent += transaction['amount']
        categories_loss.append(category_spent)

    categories_percentage = []
    for idx in range(0, len(categories_loss)):
        raw_percentage = categories_loss[idx] * 100/total_spent
        percentage = round(raw_percentage / 10 * 10)
        categories_percentage.append(percentage)
    
    final_str = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        if i == 100:
            final_str += f"{i}|"
        elif i >= 10:
            final_str += f" {i}|"
        else:
            final_str += f"  {i}|"
        for percentage_idx in range(0, len(categories_percentage)):
            if (categories_percentage[percentage_idx] >= i):
                final_str += " o "
            else:
                final_str += "   "
        final_str += ' \n'
    
    final_str +=' ' * 4 + ('-' * ((3 * len(categories)) + 1)) + '\n'
    cat_lens = [len(cat.name) for cat in categories]
    max_len = max(cat_lens)

    idx = 0
    while (idx < max_len):
        final_str += "    "
        for i in range(0, len(categories)):
            if (idx < cat_lens[i]):
                final_str += " " + categories[i].name[idx] + " "
            else:
                final_str += "   "

        final_str += ' '
        if (idx < max_len-1):
            final_str += '\n'
        idx += 1

    return final_str
