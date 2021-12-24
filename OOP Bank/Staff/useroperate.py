from getpass import getpass
from accounting import Accounting


class Useroperate:
    def __init__(self, staffinfo={}):
        # Users store all user information
        self.staffinfo = staffinfo


    # Resign staff
    def resignation(self,staffinfo = {}):
        cid = input('Please enter your staff number:')
        user = self.staffinfo.get(cid)
        if user:
            self.staffinfo.pop(cid)
            user.save_user(self.staffinfo)
            print('Successful resignation')
        else:
            print("Your staff Number is wrong, please try again.")
        
        # Open account
    def new_user(self):
        name = input('Please enter your name :')
        uid = input('Please enter your ID card :')
        pwd = getpass('Please input a password:')
        user = Accounting(uid, name)
        # Save user information
        self.staffinfo[uid] = user
        # Save user information to file
        Accounting.save_staffinfo(self.staffinfo)
        print('Open accounts successfully')

        # Display all user information
    def display_staff(self):
        for staff in self.staffinfo.values():
            print(staff)
class Staff:
    def __init__(self, uid, name,pwd):
        self.uid = uid          # ID
        self.name = name        # Full name
        self.__pwd = pwd        # Password

    def get_pwd(self):
        return self.__pwd

    def set_pwd(self):
        self.__pwd = input("Set staff password:")
    