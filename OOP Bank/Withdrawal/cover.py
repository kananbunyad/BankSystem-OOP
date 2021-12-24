import sys

import Withdrawal.message as msg

class Cover():

    def __init__(self, ltag, lreport, lindex):
        self.tag = msg.tagDict[ltag]
        self.report = msg.reportDict[lreport][lindex]
        self.index = lindex
        self.content = self.tag + self.report

    def __del__(self) -> None:
        pass

    def print(self):
        print(self.content)

    def printr(self):
        print(self.content, sys.exc_info()[1])
