# Bank card
class Card:
    def __init__(self, cid, pwd):
        self.cid = cid          # Card number
        self.pwd = pwd          # Password
        self.money = 0          # Amount of money
        self.is_lock = False    # Is it locked?