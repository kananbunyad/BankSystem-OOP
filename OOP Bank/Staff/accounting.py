import os
import pickle

class Accounting():
    def __init__(self, uid, name):
        self.uid = uid          # ID
        self.name = name        # Full name

    
    def __str__(self):
        return 'Full name:{},ID:{}'.format(self.name, self.uid)

    # Sequential storage of user information
    @staticmethod
    def save_staffuser(staffinfo):
        pathname = os.path.join(os.getcwd(), 'staffinfo_staff.pkl')
        with open(pathname, 'wb') as fp:
            pickle.dump(staffinfo, fp)

    # Loading user information from files
    @staticmethod
    def load_staffuser():
        pathname = os.path.join(os.getcwd(), 'staffinfo_staff.pkl')
        # Judging whether it exists
        if os.path.exists(pathname):
            with open(pathname, 'rb') as fp:
                staffinfo = pickle.load(fp)
            return staffinfo
        return {}