
from PyQt5.QtWidgets import QMainWindow, QPushButton


class Main(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

    def init_ui(self):
        zero = QPushButton("0", self)
        one = QPushButton("1", self)
        two = QPushButton("2", self)
        three = QPushButton("3", self)
        four = QPushButton("4", self)
        five = QPushButton("5", self)
        six = QPushButton("6", self)
        seven = QPushButton("7", self)
        eight = QPushButton("8", self)
        nine = QPushButton("9", self)

        nums = [zero, one, two, three, four, five, six, seven, eight, nine]

        for num in nums:
            num.setStyleSheet("color:blue;")
            num.clicked.connect(self.Nums)

        plus = QPushButton("+", self)
        minus = QPushButton("-", self)
        mult = QPushButton("*", self)
        div = QPushButton("/", self)

        equal = QPushButton("=", self)
        equal.clicked.connect(self.Equal)

        c = QPushButton("C", self)
        c.clicked.connect(self.C)

        ops = [c, div, mult, minus, plus, equal]

        for op in ops:
            op.setStyleSheet("color:red;")

        for i in ops[1:5]:
            i.clicked.connect(self.Operator)

        squared = QPushButton("x^2", self)
        squared.clicked.connect(self.Squared)

        sqrt = QPushButton("√", self)
        sqrt.clicked.connect(self.Sqrt)

        switch = QPushButton("+/-", self)
        switch.clicked.connect(self.Switch)

        dot = QPushButton(".", self)
        dot.clicked.connect(self.pointClicked)

        rest = [switch, squared, sqrt, dot]





