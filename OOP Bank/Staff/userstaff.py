from accounting import Accounting
from getpass import getpass


class Userstaff():
    def __init__(self, account='admin', password='123456'):
        self.account = account
        self.password = password

    # Display welcome information
    def welcome(self):
        print('*' * 30)
        print('Welcome to use Kapital Bank Userstaff System\n')
        print('*' * 30)

    # Login page
    def login(self):
        account = input('Please enter your staff number :')
        password = getpass('Please input a password:')
        if account == self.account and password == self.password:
            return True
        return False

    # Operation menu
    def menu(self):
        print('*' * 30)
        print('Open account[1]\nSales Account[2]\nDisplay all users[3]')
        print('*' * 30)
