import hashlib
from random import randint

# Helper function class
class Helper:
    # Generate Bank Card Number
    @staticmethod
    def generate_cid(length=8):
        cid = ''
        for i in range(length):
            cid += str(randint(0, 9))
        return cid

    # Encryption cipher
    @staticmethod
    def generate_password_hash(password):
        # Creating Encrypted Objects
        m = hashlib.md5()
        # Setting Encrypted String
        m.update(password.encode('utf-8'))
        # Returns an encrypted string
        return m.hexdigest()

    # Test password
    @staticmethod
    def check_password_hash(pwd, pwd_hash):
        m = hashlib.md5()
        m.update(pwd.encode('utf-8'))
        return m.hexdigest() == pwd_hash