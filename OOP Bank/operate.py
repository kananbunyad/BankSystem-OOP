from user import User
from Bankapp.card import Card
from Bankapp.helper import Helper
from getpass import getpass
from program import *
import hashlib


# Operation class
class Operate(User):
    def __init__(self, userinfo={}):
        # Users store all user information
        self.userinfo = userinfo

    # Open account
    def new_user(self):
        name = input('Please enter your name :')
        uid = input('Please enter your ID card :')
        pwd = getpass('Please input a password:')
        # Cipher encryption
        pwd = Helper.generate_password_hash(pwd)
        # Generating Random Card Number
        cid = Helper.generate_cid()
        # Create a Bank Card
        card = Card(cid, pwd)
        # Create user
        user = User(uid, name, card)
        # Save user information
        self.userinfo[cid] = user
        # Save user information to file
        User.save_user(self.userinfo)
        print('Open accounts successfully')

    # Sales Account
    def del_user(self):
        cid = input('Please enter your card number:')
        user = self.userinfo.get(cid)
        if user:
            self.userinfo.pop(cid)
            User.save_user(self.userinfo)
            print('Successful sale')
        else:
            print("Your Card Number is wrong, please try again.")

    # Balance
    def query_money(self):
        cid = input('Please enter your card number:')
        user = self.userinfo.get(cid)
        if user:
            print('Your balance is:', user.card.money)
        else:
            print('Invalid card number')

    # Transfer accounts
    def transfer_money(self):
        cid = input('Please enter your card number :')
        user = self.userinfo.get(cid)
        if user:
            dst_cid = input('Please enter the square card number :')
            dst_user = self.userinfo.get(dst_cid)
            if dst_user:
                money = float(input('Please enter the amount of transfer :'))
                # Judging whether the balance is adequate
                if user.card.money < money:
                    print('Inadequate balance, transfer failure')
                    return
                pwd = getpass('Please input a password:')
                if Helper.check_password_hash(pwd, user.card.pwd):
                    user.card.money -= money
                    dst_user.card.money += money
                    User.save_user(self.userinfo)
                    print('Successful transfer')
                else:
                    print('Wrong password, transfer failure')
            else:
                print('Invalid card number')
        else:
            print('Invalid card number')

    # Deposit
    def save_money(self):
        cid = input('Please enter your card number :')
        user = self.userinfo.get(cid)
        if user:
            # Check whether the user is locked
            if user.card.is_lock:
                print('The card is locked. Please unlock it first.')
                return
            # Record the number of password errors
            count = 0
            while count < 3:
                pwd = getpass('Please input a password:')
                if Helper.check_password_hash(pwd, user.card.pwd):
                    while True:
                        try:
                            money = int(input('Please enter your deposit amount :'))
                            break
                        except:
                            print('Your deposit amount is invalid.(value is not integer)')
                    user.card.money += float(money)
                    User.save_user(self.userinfo)
                    print('Deposit success')
                    break
                else:
                    count += 1
                    print('The password is incorrect. Please re-enter it.')
            else:
                user.card.is_lock = True
                User.save_user(self.userinfo)
                print('The password error has reached the upper limit and the card is locked')
        else:
            print('Invalid card number')

    # Withdraw money
    def get_money(self):
        cid = input('Please enter your card number :')
        user = self.userinfo.get(cid)
        pwd = getpass('Please input a password:')
        if Helper.check_password_hash(pwd, user.card.pwd):
            app.main()
            print('Successful withdrawals')
            user.card.money -= float(app.payment)
        else:
            print("Your password is invalid, please try again")


    # Modify password
    def change_pwd(self):
        cid = input('Please enter your card number:')
        user = self.userinfo.get(cid)
        pwd = getpass('Please input a password:')
        if Helper.check_password_hash(pwd, user.card.pwd):
            newpwd = getpass("Please enter the new password:")
            user.card.pwd=newpwd
            print('Successful password modification')
        else:
            print("Your password is wrong, please try again")

    # Locking
    def lock_user(self):
        cid = input('Please enter your card number:')
        user = self.userinfo.get(cid)
        pwd = getpass('Please input a password:')
        if Helper.check_password_hash(pwd, user.card.pwd):
            user.card.is_lock = True
        print('User locking')

    # Unlock
    def unlock_user(self):
        cid = input('Please enter the card number:')
        user = self.userinfo.get(cid)
        if user:
            user.card.is_lock = False
            User.save_user(self.userinfo)
            print('Unlock success')
        else:
            print('Invalid card number')

    # Display all user information
    def show_users(self):
        for user in self.userinfo.values():
            print(user)