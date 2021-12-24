import Withdrawal.cover as send

class Invoice:

    money = [
        [500, 200, 100],
        [50, 20, 10],
        [5, 2, 1],
        [0.50, 0.20, 0.10],
        [0.05, 0.02, 0.01]
    ]

    def __init__(self, lPrice, lPayment):
        self.price = lPrice
        self.payment = lPayment
        self.budget = lPayment - lPrice
        self.item = f'{self.budget:.2f}'.split('.')
        self.index = 0
        self.numeral = list()
        self.count = 0

    def __del__(self) -> None:
        pass

    def pay(self):
        reList = self.swap()

        if(self.payment >= self.price and self.payment in reList[0:15]):
            self.operator()
            self.show()

            send.Cover('msg', 'invoice', 0).print()
        else:
            send.Cover('msg', 'invoice', 1).print()
  
    def show(self):
        print("\nGet change :", f'{self.budget:.2f}')

        self.check()

        if(float(self.budget) > 0):
            send.Cover('null', 'invoice', 2).print()
        else:
            pass

        for x in range(0, len(self.numeral)):

            for y in range(0, len(self.numeral[x])):
                self.count = self.count + 1

                if self.numeral[x][y] != 0:

                    if(self.count >= 8 and self.count <= 9):
                        print(self.numeral[x][y], "Banknote(s) of "+str(self.money[x][y])+" manat(s).")
                    elif(self.count > 9):
                        print(self.numeral[x][y], "Coin(s) of "+str(f'{self.money[x][y]:.2f}')+" qapik(s).")
                    else:
                        print(self.numeral[x][y], "Banknote(s) of "+str(self.money[x][y])+" manat(s).")
                else:
                    pass

    def check(self):
        if(len(self.money) != len(self.numeral)):
            b = len(self.money) - len(self.numeral)

            for x in range(b):
                self.numeral.insert(0, [0, 0, 0])
        else:
            pass

    def matrix(self):
        add, end, rem = 0, 0, 0

        if(self.index > 5 and self.index < 10):
            end = abs(self.index - 5)
            add = 1
        elif(self.index > 0 and self.index <= 5):
            end = self.index
        else:
            end, rem = 1, 1

        for x in range(1, end + 1, 1):
            c = x - (int(x / 2) * 2)
            b = int(x / 2)
            a = int(x / 5)
            c = c - a - rem
            b = b - a * 2

        return [int(a) + add, int(b), int(c)]

    def operator(self):
        for x in range(len(self.item[0])):
            self.index = int(self.item[0][x])
            self.numeral.append(self.matrix())

        for x in range(len(self.item[1])):
            self.index = int(self.item[1][x])
            self.numeral.append(self.matrix())

    def swap(self):
        rewrite = list()

        for x in range(len(self.money)):

            for y in range(len(self.money[x])):
                rewrite.append(self.money[x][y])

        return rewrite
