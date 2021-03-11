from MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import *
import operator

FREE = 0
BUSY = 1


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_0.clicked.connect(lambda: self.input_number(0))
        self.ui.pushButton_1.clicked.connect(lambda: self.input_number(1))
        self.ui.pushButton_2.clicked.connect(lambda: self.input_number(2))
        self.ui.pushButton_3.clicked.connect(lambda: self.input_number(3))
        self.ui.pushButton_4.clicked.connect(lambda: self.input_number(4))
        self.ui.pushButton_5.clicked.connect(lambda: self.input_number(5))
        self.ui.pushButton_6.clicked.connect(lambda: self.input_number(6))
        self.ui.pushButton_7.clicked.connect(lambda: self.input_number(7))
        self.ui.pushButton_8.clicked.connect(lambda: self.input_number(8))
        self.ui.pushButton_9.clicked.connect(lambda: self.input_number(9))

        self.ui.pushButton_add.clicked.connect(lambda: self.operation(operator.add))
        self.ui.pushButton_sub.clicked.connect(lambda: self.operation(operator.sub))
        self.ui.pushButton_mul.clicked.connect(lambda: self.operation(operator.mul))
        self.ui.pushButton_div.clicked.connect(lambda: self.operation(operator.truediv))

        self.ui.pushButton_equal.clicked.connect(self.equals)
        self.ui.pushButton_clear.clicked.connect(self.reset)

        self.state = FREE
        self.stack = [0]
        self.last_operation = None
        self.current_operation = None

        self.reset()
        self.show()

    def display(self):
        self.ui.lcdNumber.display(self.stack[-1])

    def reset(self):
        self.state = FREE
        self.stack = [0]
        self.last_operation = None
        self.current_operation = None
        self.display()

    def input_number(self, v):
        if self.state == FREE:
            self.state = BUSY
            self.stack[-1] = v
        else:
            self.stack[-1] = self.stack[-1] * 10 + v
        self.display()

    def operation(self, op):
        if self.current_operation:
            self.equals()
        self.stack.append(0)
        self.state = BUSY
        self.current_operation = op

    def equals(self):
        if self.state == FREE and self.last_operation:
            s, self.current_operation = self.last_operation
            self.stack.append(s)

        if self.current_operation:
            self.last_operation = self.stack[-1], self.current_operation

            try:
                self.stack = [self.current_operation(*self.stack)]
            except Exception:
                self.lcdNumber.display('Err')
                self.stack = [0]
            else:
                self.current_operation = None
                self.state = FREE
                self.display()


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Calculator")
    window = MainWindow()
    app.exec_()
