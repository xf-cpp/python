

class Bank():
    def __init__(self):
        self.accounts = {}

    def creat_account(self, account_number, account_holder, initial_balance):
        print(f'账户{account_number}创建成功， 持有人：{account_holder}， 余额：{initial_balance}')
        account = BankAccount(account_number, account_holder, initial_balance)
        self.accounts[account_number] = account

    def get_account(self, account_number):
        # print(f'name: {self.accounts[account_number].name}')
        # print(f'balance: {self.accounts[account_number].balance}')
        return self.accounts[account_number]


class BankAccount(Bank):
    def __init__(self, account_number, account_holder, initial_balance = 0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f'存款成功，存款{amount}元， 余额为{self.balance}元')

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print('余额不足， 取款失败')
            return False
        else:
            print(f'取款成功， 取款{amount}元')
            self.balance = self.balance - amount
            return True

    def get_balance(self):
        print(f'该账户{self.account_holder}余额为：{self.balance} 元')

    def transfer(self, target_account, amount):
        flag = self.withdraw(amount)
        if flag is True:
            target_account.deposit(amount)
            print(f'成功向 {target_account.account_number} 转账 {amount}元')
            return True
        if flag is False:
            print('账户余额不足，转账失败')
            return False







