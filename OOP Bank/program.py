import os

import Withdrawal.message as msg
import Withdrawal.cover as send
import Withdrawal.bank as machine

class Program():

    def __init__(self):
        self.run = 1

    def __del__(self) -> None:
        send.Cover('msg', 'action', 0).print()

    def status(self):
        step = input(msg.reportDict['request'][2])

        clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

        if(step == "Yes"):
            self.run = 0
        elif(step == "No"):
            clear()
        else:
            send.Cover('msg', 'action', 1).print()
            self.status()

    def main(self):

        while self.run == 1:

            try:
                price = input(msg.reportDict['request'][0])
                self.payment = input(msg.reportDict['request'][1])

                invoice = machine.Bank(float(price), float(self.payment))
                invoice.pay()

            except:
                send.Cover('null', 'error', 0).printr()
                
            finally:
                self.status()

app = Program()