# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from practice import BankAccount, Bank



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bank = Bank()
    bank.creat_account('640471562', 'lsy', 999999999)
    lsy = bank.get_account('640471562')
    lsy.deposit(500)
    lsy.get_balance()
    lsy.withdraw(200)
    lsy.get_balance()
    bank.creat_account('497243778', 'lsq', 0)
    lsq = bank.get_account('497243778')
    lsq.get_balance()
    lsy.withdraw(2000)
    lsy.get_balance()
    lsq.get_balance()