import os
import pickle
from Bankapp.card import Card

# User class
class User:
    def __init__(self, uid, name, card):
        self.uid = uid          # ID
        self.name = name        # Full name
        self.card = card        # Bank card

    def __str__(self):
        return 'Full name:{},ID:{},Card number:{}'.format(self.name, self.uid, self.card.cid)

    # Sequential storage of user information
    @staticmethod
    def save_user(userinfo):
        pathname = os.path.join(os.getcwd(), 'userinfo.pkl')
        with open(pathname, 'wb') as fp:
            pickle.dump(userinfo, fp)

    # Loading user information from files
    @staticmethod
    def load_user():
        pathname = os.path.join(os.getcwd(), 'userinfo.pkl')
        # Judging whether it exists
        if os.path.exists(pathname):
            with open(pathname, 'rb') as fp:
                userinfo = pickle.load(fp)
            return userinfo
        return {}

class Accounting():
    def __init__(self, uid, name):
        self.uid = uid          # ID
        self.name = name        # Full name

    
    def __str__(self):
        return 'Full name:{},ID:{}'.format(self.name, self.uid)

    # Sequential storage of user information
    @staticmethod
    def save_staffuser(userinfo):
        pathname = os.path.join(os.getcwd(), 'userinfo_staff.pkl')
        with open(pathname, 'wb') as fp:
            pickle.dump(userinfo, fp)

    # Loading user information from files
    @staticmethod
    def load_staffuser():
        pathname = os.path.join(os.getcwd(), 'userinfo_staff.pkl')
        # Judging whether it exists
        if os.path.exists(pathname):
            with open(pathname, 'rb') as fp:
                userinfo = pickle.load(fp)
            return userinfo
        return {}