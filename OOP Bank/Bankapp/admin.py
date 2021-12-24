from getpass import getpass


# Administrators class
class Admin:
    def __init__(self, account='admin', password='123456'):
        self.account = account
        self.password = password

    # Display welcome information
    def welcome(self):
        print('*' * 30)
        print('Welcome to use Kapital Bank Management System\n')
        print('*' * 30)

    # Login page
    def login(self):
        account = input('Please enter your account number :')
        password = getpass('Please input a password:')
        if account == self.account and password == self.password:
            return True
        return False

    # Operation menu
    def menu(self):
        print('*' * 30)
        print('Open account[1]\nSales Account[2]\nBalance[3]\nDeposit[4]')
        print('Withdraw money[5]\nTransfer accounts[6]\nModify password[7]\nLocking[8]')
        print('Unlock[9]\nSign out[0]\nDisplay all users[10]')
        print('*' * 30)


