import Withdrawal.invoice as process

class Bank(process.Invoice):

    def __init__(self, lprice, lPayment):
        super().__init__(lprice, lPayment)

    def __del__(self) -> None:
        pass
