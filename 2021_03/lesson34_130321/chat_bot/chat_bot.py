import sys
from PyQt5 import QtWidgets
import ui_chat_bot


class ChatBotApp(QtWidgets.QMainWindow, ui_chat_bot.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.click_button)

    def click_button(self):
        message = self.lineEdit.text()
        self.plainTextEdit.appendPlainText(message)
        self.lineEdit.clear()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ChatBotApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

